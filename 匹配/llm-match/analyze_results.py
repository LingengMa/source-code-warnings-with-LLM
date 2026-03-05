"""
结果分析脚本
对 LLM 分类结果 JSON 文件进行全面分析，输出 Markdown 格式报告。

用法：
    python analyze_results.py <results.json> [output_report.md]

若未指定输出路径，报告将保存在与输入文件同目录下，文件名为 <input_stem>_report.md
"""

import json
import os
import sys
import argparse
from collections import defaultdict
from datetime import datetime


LABEL_VALUES     = ["TP", "FP"]
LLM_LABEL_VALUES = ["TP", "FP", "Unknown"]


import re as _re


def _strip_version(project_name_with_version: str) -> str:
    """从 project_name_with_version 中去除末尾版本号，返回 project_name_without_version。
    例如：'ffmpeg-6.1.1' -> 'ffmpeg', 'openssl-3.0.0' -> 'openssl'
    """
    return _re.sub(r'[-_]\d+(\.\d+)*$', '', project_name_with_version)


def analyze_file(filepath: str) -> dict:
    """
    分析单个结果文件，返回统计数据及各分类条目列表。
    只统计同时具有 id、label、llm_label 三个字段的有效条目。
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 过滤有效条目
    valid = [
        item for item in data
        if item.get("id") is not None
        and item.get("label") in LABEL_VALUES
        and item.get("llm_label") in LLM_LABEL_VALUES
    ]

    total   = len(valid)
    skipped = len(data) - total

    # label × llm_label 交叉计数及条目列表
    # cross_counts[label][llm_label] = count
    # cross_items[label][llm_label]  = [item, ...]
    cross_counts = defaultdict(lambda: defaultdict(int))
    cross_items  = defaultdict(lambda: defaultdict(list))

    # 按 (tool_name, project_name_without_version, rule_id) 联合分组统计
    # combo_counts[combo_key] = {"total": n, "llm_label": {"TP": n, "FP": n, "Unknown": n}}
    combo_counts = defaultdict(lambda: defaultdict(int))

    for item in valid:
        lbl = item["label"]
        llm = item["llm_label"]
        cross_counts[lbl][llm] += 1
        cross_items[lbl][llm].append(item)

        tool    = item.get("tool_name", "")
        proj_nv = _strip_version(item.get("project_name_with_version", ""))
        rule    = item.get("rule_id", "")
        key     = (tool, proj_nv, rule)
        combo_counts[key]["total"] += 1
        combo_counts[key][llm]     += 1

    # 各 label 小计
    label_totals = {lbl: sum(cross_counts[lbl].values()) for lbl in LABEL_VALUES}

    # 一致性指标（仅 TP/FP 两类，排除 Unknown）
    decided  = [item for item in valid if item["llm_label"] != "Unknown"]
    n_decided  = len(decided)
    n_unknown  = total - n_decided
    n_correct  = sum(1 for item in decided if item["label"] == item["llm_label"])
    accuracy   = n_correct / n_decided if n_decided > 0 else None

    # 精确率 / 召回率（针对 TP 类）
    tp_as_tp = cross_counts["TP"]["TP"]
    fp_as_tp = cross_counts["FP"]["TP"]
    tp_as_fp = cross_counts["TP"]["FP"]
    fp_as_fp = cross_counts["FP"]["FP"]

    precision = tp_as_tp / (tp_as_tp + fp_as_tp) if (tp_as_tp + fp_as_tp) > 0 else None
    recall    = tp_as_tp / (tp_as_tp + tp_as_fp) if (tp_as_tp + tp_as_fp) > 0 else None
    f1        = (2 * precision * recall / (precision + recall)
                 if precision is not None and recall is not None
                 and (precision + recall) > 0 else None)

    # 将 combo_counts 转换为可序列化的结构，并按 total 降序排列
    # combo_stats: list of {"tool_name", "project_name_without_version", "rule_id", "total", "TP", "FP", "Unknown"}
    combo_stats = []
    for (tool, proj_nv, rule), counts in combo_counts.items():
        combo_stats.append({
            "tool_name":                    tool,
            "project_name_without_version": proj_nv,
            "rule_id":                      rule,
            "total":                        counts["total"],
            "TP":                           counts.get("TP", 0),
            "FP":                           counts.get("FP", 0),
            "Unknown":                      counts.get("Unknown", 0),
        })
    combo_stats.sort(key=lambda x: (-x["total"], x["tool_name"], x["project_name_without_version"], x["rule_id"]))

    return {
        "total":        total,
        "skipped":      skipped,
        "cross_counts": {k: dict(v) for k, v in cross_counts.items()},
        "cross_items":  {k: {kk: vv for kk, vv in v.items()} for k, v in cross_items.items()},
        "label_totals": label_totals,
        "n_unknown":    n_unknown,
        "unknown_rate": n_unknown / total if total > 0 else None,
        "n_decided":    n_decided,
        "n_correct":    n_correct,
        "n_incorrect":  n_decided - n_correct,
        "accuracy":     accuracy,
        "precision":    precision,
        "recall":       recall,
        "f1":           f1,
        # 各分类条目列表（方便报告输出）
        "tp_tp":        cross_items["TP"]["TP"],   # 算法=TP, LLM=TP  (一致)
        "fp_fp":        cross_items["FP"]["FP"],   # 算法=FP, LLM=FP  (一致)
        "tp_fp":        cross_items["TP"]["FP"],   # 算法=TP, LLM=FP  (误判)
        "fp_tp":        cross_items["FP"]["TP"],   # 算法=FP, LLM=TP  (误判)
        "tp_unknown":   cross_items["TP"]["Unknown"],
        "fp_unknown":   cross_items["FP"]["Unknown"],
        # (tool_name, project_name_without_version, rule_id) 联合分组统计
        "combo_stats":      combo_stats,
        "n_combo_types":    len(combo_stats),
    }


def fmt_pct(value, decimals=1):
    if value is None:
        return "N/A"
    return f"{value * 100:.{decimals}f}%"


def item_summary_row(item: dict) -> str:
    """生成单条目的 Markdown 表格行"""
    id_     = item.get("id", "")
    proj    = item.get("project_name_with_version", "")
    func    = item.get("function_name", "")
    rule    = item.get("rule_id", "")
    line    = item.get("line_number", "")
    label   = item.get("label", "")
    llm     = item.get("llm_label", "")
    reason  = item.get("llm_label_reason", "").replace("\n", " ").replace("|", "｜")
    # 截断过长 reason
    if len(reason) > 120:
        reason = reason[:117] + "..."
    return f"| {id_} | {proj} | {func} | {rule} | {line} | {label} | {llm} | {reason} |"


def build_item_table(items: list) -> list:
    """构建条目 Markdown 表格，返回行列表"""
    if not items:
        return ["*（无）*", ""]
    lines = [
        "| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in items:
        lines.append(item_summary_row(item))
    lines.append("")
    return lines


def generate_markdown_report(filepath: str, stats: dict) -> str:
    """生成完整的 Markdown 报告字符串"""
    lines = []
    filename = os.path.basename(filepath)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 标题
    lines += [
        f"# LLM 分类结果分析报告",
        "",
        f"- **分析文件**：`{filename}`",
        f"- **完整路径**：`{filepath}`",
        f"- **生成时间**：{now}",
        "",
        "---",
        "",
    ]

    # 1. 总览
    lines += [
        "## 1. 数据总览",
        "",
        f"| 指标 | 数值 |",
        f"|---|---|",
        f"| 数据总条数 | {stats['total'] + stats['skipped']} |",
        f"| 有效条目数（含 label / llm_label） | {stats['total']} |",
        f"| 跳过条目数（字段缺失或无效） | {stats['skipped']} |",
        f"| Unknown 条目数 | {stats['n_unknown']} |",
        f"| Unknown 比率 | {fmt_pct(stats['unknown_rate'])} |",
        f"| 已判定条目数（非 Unknown） | {stats['n_decided']} |",
        f"| 判定一致数 | {stats['n_correct']} |",
        f"| 判定不一致数 | {stats['n_incorrect']} |",
        "",
    ]

    # 2. label 分布
    lines += [
        "## 2. 算法标注（label）分布",
        "",
        "| label | 数量 | 占比 |",
        "|---|---|---|",
    ]
    for lbl in LABEL_VALUES:
        cnt = stats["label_totals"].get(lbl, 0)
        pct = fmt_pct(cnt / stats["total"]) if stats["total"] > 0 else "N/A"
        lines.append(f"| {lbl} | {cnt} | {pct} |")
    lines.append("")

    # 3. label × llm_label 交叉矩阵
    lines += [
        "## 3. label × llm_label 交叉矩阵",
        "",
        "| label \\ llm_label | " + " | ".join(LLM_LABEL_VALUES) + " | **合计** |",
        "|---|" + "---|" * (len(LLM_LABEL_VALUES) + 1),
    ]
    for lbl in LABEL_VALUES:
        row = stats["cross_counts"].get(lbl, {})
        cells = " | ".join(str(row.get(v, 0)) for v in LLM_LABEL_VALUES)
        total_lbl = stats["label_totals"].get(lbl, 0)
        lines.append(f"| **{lbl}** | {cells} | **{total_lbl}** |")
    # 列合计
    col_sums = []
    for llm in LLM_LABEL_VALUES:
        col_sums.append(sum(stats["cross_counts"].get(lbl, {}).get(llm, 0) for lbl in LABEL_VALUES))
    col_cells = " | ".join(str(s) for s in col_sums)
    lines.append(f"| **合计** | {col_cells} | **{stats['total']}** |")
    lines.append("")

    # 4. 汇总指标
    lines += [
        "## 4. 汇总指标",
        "",
        "> 以下指标仅基于**已判定（非 Unknown）**条目计算。",
        "",
        "| 指标 | 数值 |",
        "|---|---|",
        f"| 准确率（Accuracy） | {fmt_pct(stats['accuracy'])} |",
        f"| 精确率（Precision，以 TP 为正类） | {fmt_pct(stats['precision'])} |",
        f"| 召回率（Recall，以 TP 为正类） | {fmt_pct(stats['recall'])} |",
        f"| F1 分数（以 TP 为正类） | {fmt_pct(stats['f1'])} |",
        "",
    ]

    # 5. 各分类详细列表
    lines += ["## 5. 各分类条目详情", ""]

    # 5.1 一致-TP
    tp_tp = stats["tp_tp"]
    lines += [
        f"### 5.1 一致：算法=TP，LLM=TP（共 {len(tp_tp)} 条）",
        "",
        "> 算法与 LLM 均判定为真阳性（True Positive）。",
        "",
    ]
    lines += build_item_table(tp_tp)

    # 5.2 一致-FP
    fp_fp = stats["fp_fp"]
    lines += [
        f"### 5.2 一致：算法=FP，LLM=FP（共 {len(fp_fp)} 条）",
        "",
        "> 算法与 LLM 均判定为假阳性（False Positive）。",
        "",
    ]
    lines += build_item_table(fp_fp)

    # 5.3 不一致：算法=TP，LLM=FP
    tp_fp = stats["tp_fp"]
    lines += [
        f"### 5.3 不一致：算法=TP，LLM=FP（共 {len(tp_fp)} 条）",
        "",
        "> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。",
        "",
    ]
    lines += build_item_table(tp_fp)

    # 5.4 不一致：算法=FP，LLM=TP
    fp_tp = stats["fp_tp"]
    lines += [
        f"### 5.4 不一致：算法=FP，LLM=TP（共 {len(fp_tp)} 条）",
        "",
        "> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。",
        "",
    ]
    lines += build_item_table(fp_tp)

    # 5.5 Unknown：算法=TP
    tp_unk = stats["tp_unknown"]
    lines += [
        f"### 5.5 Unknown：算法=TP，LLM=Unknown（共 {len(tp_unk)} 条）",
        "",
        "> 算法判定为 TP，LLM 无法判定。",
        "",
    ]
    lines += build_item_table(tp_unk)

    # 5.6 Unknown：算法=FP
    fp_unk = stats["fp_unknown"]
    lines += [
        f"### 5.6 Unknown：算法=FP，LLM=Unknown（共 {len(fp_unk)} 条）",
        "",
        "> 算法判定为 FP，LLM 无法判定。",
        "",
    ]
    lines += build_item_table(fp_unk)

    # 6. (tool_name, project_name_without_version, rule_id) 联合分组统计
    combo_stats  = stats["combo_stats"]
    n_combo_types = stats["n_combo_types"]
    lines += [
        f"## 6. 按 (tool_name, project_name_without_version, rule_id) 联合分组统计",
        "",
        f"> 共 **{n_combo_types}** 种不同组合（种类），按条目数降序排列。",
        "",
        "| # | tool_name | project_name_without_version | rule_id | 总计 | TP | FP | Unknown |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for idx, row in enumerate(combo_stats, 1):
        lines.append(
            f"| {idx} | {row['tool_name']} | {row['project_name_without_version']} "
            f"| {row['rule_id']} | {row['total']} | {row['TP']} | {row['FP']} | {row['Unknown']} |"
        )
    lines.append("")

    # 尾注
    lines += [
        "---",
        "",
        f"*报告由 `analyze_results.py` 自动生成，生成时间：{now}*",
        "",
    ]

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="分析 LLM 分类结果 JSON 文件，输出详细 Markdown 报告",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        type=str,
        help="待分析的 JSON 结果文件路径",
    )
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        default=None,
        help="输出 Markdown 报告路径（可选，默认与输入文件同目录，文件名为 <input_stem>_report.md）",
    )
    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"错误：输入文件不存在：{input_path}", file=sys.stderr)
        sys.exit(1)

    # 确定输出路径
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        stem = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(os.path.dirname(input_path), f"{stem}_report.md")

    print(f"正在分析：{input_path}")
    stats = analyze_file(input_path)

    print(f"正在生成报告：{output_path}")
    report = generate_markdown_report(input_path, stats)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    # 同时打印简要摘要到控制台
    print()
    print("─" * 50)
    print(f"  有效条目数  : {stats['total']}  （跳过 {stats['skipped']} 条）")
    print(f"  Unknown     : {stats['n_unknown']}  ({fmt_pct(stats['unknown_rate'])})")
    print(f"  已判定      : {stats['n_decided']}")
    print(f"  准确率      : {fmt_pct(stats['accuracy'])}")
    print(f"  精确率(TP)  : {fmt_pct(stats['precision'])}")
    print(f"  召回率(TP)  : {fmt_pct(stats['recall'])}")
    print(f"  F1(TP)      : {fmt_pct(stats['f1'])}")
    print(f"  联合分组种类: {stats['n_combo_types']}  (tool × project × rule_id)")
    print("─" * 50)
    print(f"\n✅ 报告已保存至：{output_path}")


if __name__ == "__main__":
    main()
