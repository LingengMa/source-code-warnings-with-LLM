#!/usr/bin/env python3
"""
差集分析脚本

计算 results_filtered.json 与 data.json（忽略 function_name/label 字段）的差集，
并输出详细的数量统计与分布分析。同时将差集条目保存为独立 JSON 文件。

用法:
    python3 diff_analysis.py
    python3 diff_analysis.py -r results_filtered.json -d data.json -o diff_output.json
    python3 diff_analysis.py --no-save   # 仅分析，不保存差集文件
"""

import json
import argparse
from pathlib import Path
from collections import Counter


# data.json 中相对于 results_filtered.json 多出的字段，比较时忽略
EXTRA_FIELDS = ("function_name", "label")


def entry_to_key(entry: dict, exclude: tuple = EXTRA_FIELDS) -> tuple:
    """将条目转换为可哈希的比较键（忽略 exclude 中的字段）。"""
    return (
        entry.get("tool_name"),
        entry.get("project_name"),
        entry.get("project_name_with_version"),
        entry.get("project_version"),
        entry.get("file_path"),
        entry.get("line_number"),
        entry.get("rule_id"),
        tuple(sorted(entry.get("cwe") or [])),
        entry.get("message"),
        entry.get("severity"),
    )


def load_json(path: str) -> list:
    print(f"  读取: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compute_diff(rf: list, dj: list) -> tuple[set, set, set]:
    """
    返回 (only_in_rf, only_in_dj, in_both) 三个 key 集合。
    """
    rf_set = set(entry_to_key(e) for e in rf)
    dj_set = set(entry_to_key(e) for e in dj)
    return rf_set - dj_set, dj_set - rf_set, rf_set & dj_set


def print_section(title: str) -> None:
    print()
    print("=" * 62)
    print(f"  {title}")
    print("=" * 62)


def analyze(rf_file: str, dj_file: str, output_file: str | None) -> None:
    print_section("加载数据")
    rf = load_json(rf_file)
    dj = load_json(dj_file)

    # ── 计算差集 ──────────────────────────────────────────────────
    only_in_rf, only_in_dj, in_both = compute_diff(rf, dj)

    rf_set = set(entry_to_key(e) for e in rf)
    dj_set = set(entry_to_key(e) for e in dj)

    # ── 总体统计 ──────────────────────────────────────────────────
    print_section("总体数量统计（全字段精确匹配，忽略 function_name/label）")
    rows = [
        (f"{rf_file} 原始条目数",       len(rf)),
        (f"{rf_file} 去重后",           len(rf_set)),
        (f"{dj_file} 原始条目数",       len(dj)),
        (f"{dj_file} 去重后",           len(dj_set)),
        ("两者共同存在",                 len(in_both)),
        (f"只在 {rf_file} 中",          len(only_in_rf)),
        (f"只在 {dj_file} 中",          len(only_in_dj)),
        ("差集总数",                     len(only_in_rf) + len(only_in_dj)),
    ]
    col_w = max(len(r[0]) for r in rows) + 2
    for label, val in rows:
        print(f"  {label:<{col_w}}: {val}")

    # ── 只在 rf 中的条目分布 ──────────────────────────────────────
    only_rf_entries = [e for e in rf if entry_to_key(e) in only_in_rf]
    only_dj_entries = [e for e in dj if entry_to_key(e) in only_in_dj]

    if only_rf_entries:
        print_section(f"只在 {rf_file} 中的条目 — 按 tool / project 分布")
        cnt = Counter((e["tool_name"], e.get("project_name", "")) for e in only_rf_entries)
        _print_counter(cnt, ("tool", "project"))

        print_section(f"只在 {rf_file} 中的条目 — 按 tool 汇总")
        tool_cnt = Counter(e["tool_name"] for e in only_rf_entries)
        for tool, n in tool_cnt.most_common():
            print(f"  {tool:<12}: {n}")

    if only_dj_entries:
        print_section(f"只在 {dj_file} 中的条目 — 按 tool / project 分布")
        cnt2 = Counter((e["tool_name"], e.get("project_name", "")) for e in only_dj_entries)
        _print_counter(cnt2, ("tool", "project"))

    # ── 差集中 CWE 分布 ───────────────────────────────────────────
    all_diff = only_rf_entries + only_dj_entries
    if all_diff:
        print_section("差集条目中 CWE 分布（Top 20）")
        cwe_cnt = Counter()
        for e in all_diff:
            for cwe in (e.get("cwe") or []):
                cwe_cnt[cwe] += 1
        for cwe, n in cwe_cnt.most_common(20):
            print(f"  {cwe:<12}: {n}")

        print_section("差集条目中 rule_id 分布（Top 20）")
        rule_cnt = Counter(e.get("rule_id", "") for e in all_diff)
        for rule, n in rule_cnt.most_common(20):
            print(f"  {rule:<50}: {n}")

    # ── 保存差集文件 ──────────────────────────────────────────────
    if output_file is not None and only_rf_entries:
        out_path = Path(output_file)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(only_rf_entries, f, ensure_ascii=False, indent=4)
        print()
        print(f"✓ 差集条目（共 {len(only_rf_entries)} 条）已保存至: {out_path}")


def _print_counter(cnt: Counter, col_names: tuple) -> None:
    """格式化打印二元组 Counter。"""
    for keys, n in cnt.most_common():
        parts = "  ".join(f"{name}={val:<20}" for name, val in zip(col_names, keys))
        print(f"  {parts}: {n}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="计算两个 JSON 结果文件的差集并输出分布分析"
    )
    parser.add_argument(
        "-r", "--results",
        default="results_filtered.json",
        help="结果文件路径（默认: results_filtered.json）",
    )
    parser.add_argument(
        "-d", "--data",
        default="data.json",
        help="基准数据文件路径（默认: data.json）",
    )
    parser.add_argument(
        "-o", "--output",
        default="diff_only_in_results_filtered.json",
        help="差集输出文件路径（默认: diff_only_in_results_filtered.json）",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="仅分析，不保存差集文件",
    )
    args = parser.parse_args()

    try:
        analyze(
            rf_file=args.results,
            dj_file=args.data,
            output_file=None if args.no_save else args.output,
        )
    except FileNotFoundError as e:
        print(f"错误: 找不到文件 — {e}")
        return 1
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 — {e}")
        return 1
    except Exception as e:
        print(f"错误: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
