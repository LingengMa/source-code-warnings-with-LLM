#!/usr/bin/env python3
"""
重复性分析脚本

重复判定标准：
  1. tool_name 相同
  2. project_name_without_version 相同（从 project_name_with_version 中提取）
  3. rule_id 相同
  4. file_path 相同
  5. full_file_path 所指文件中，line_number 行的内容完全一致
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

INPUT_FILE = "input/llm_results.json"
OUTPUT_FILE = "duplicate_analysis.json"

# ──────────────────────────────────────────────
# 工具函数
# ──────────────────────────────────────────────

def get_project_name_without_version(project_name_with_version: str) -> str:
    """
    从 'ffmpeg-6.1.1' 提取 'ffmpeg'
    从 'openssl-openssl-3.2.1' 提取 'openssl-openssl'
    规则：去掉末尾的 '-数字...' 部分
    """
    return re.sub(r'-[\d][^-]*$', '', project_name_with_version)


def read_line(full_file_path: str, line_number: int) -> str | None:
    """读取文件指定行内容，返回去除首尾空白后的字符串；文件不存在返回 None"""
    if not full_file_path or not line_number:
        return None
    if not os.path.exists(full_file_path):
        return None
    try:
        with open(full_file_path, 'r', encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, start=1):
                if i == line_number:
                    return line.rstrip('\n')
    except Exception:
        return None
    return None


# ──────────────────────────────────────────────
# 主逻辑
# ──────────────────────────────────────────────

def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"总记录数: {len(data)}")

    # 1. 为每条记录附加辅助字段
    missing_file = 0
    for item in data:
        item['_project_no_ver'] = get_project_name_without_version(
            item.get('project_name_with_version', '')
        )
        line_content = read_line(item.get('full_file_path', ''), item.get('line_number'))
        item['_line_content'] = line_content
        if line_content is None:
            missing_file += 1

    print(f"无法读取源文件行内容的记录数: {missing_file}")

    # 2. 按 (tool_name, project_no_ver, rule_id, file_path, line_content) 分组
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for item in data:
        key = (
            item.get('tool_name', ''),
            item['_project_no_ver'],
            item.get('rule_id', ''),
            item.get('file_path', ''),
            item['_line_content'],   # None 表示文件不存在，单独成组
        )
        groups[key].append(item)

    # 3. 统计
    dup_groups = {k: v for k, v in groups.items() if len(v) > 1}
    total_in_dup = sum(len(v) for v in dup_groups.values())
    unique_count = len(groups)

    print(f"\n======= 重复性分析结果 =======")
    print(f"去重后唯一警告组数:        {unique_count}")
    print(f"存在重复的分组数:          {len(dup_groups)}")
    print(f"属于重复组的记录总数:      {total_in_dup}")
    print(f"重复记录数（多出的副本）:  {total_in_dup - len(dup_groups)}")
    print(f"重复率（占全量）:          {total_in_dup / len(data) * 100:.2f}%")

    # 4. 按重复数量分布
    size_dist: dict[int, int] = defaultdict(int)
    for v in dup_groups.values():
        size_dist[len(v)] += 1
    print(f"\n重复组大小分布（组内记录数 -> 组数）:")
    for size in sorted(size_dist):
        print(f"  {size} 条重复  ->  {size_dist[size]} 组")

    # 5. 各项目重复情况
    proj_stats: dict[str, dict] = defaultdict(lambda: {'total': 0, 'dup': 0})
    for item in data:
        proj = item['_project_no_ver']
        proj_stats[proj]['total'] += 1
    for v in dup_groups.values():
        proj = v[0]['_project_no_ver']
        proj_stats[proj]['dup'] += len(v)

    print(f"\n各项目重复情况:")
    print(f"  {'项目':<30} {'总数':>6} {'重复记录数':>10} {'重复率':>8}")
    print(f"  {'-'*58}")
    for proj in sorted(proj_stats):
        st = proj_stats[proj]
        rate = st['dup'] / st['total'] * 100 if st['total'] else 0
        print(f"  {proj:<30} {st['total']:>6} {st['dup']:>10} {rate:>7.2f}%")

    # 6. 详细重复组输出（去掉大字段，便于查阅）
    dup_details = []
    for key, items in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
        dup_details.append({
            "group_key": {
                "tool_name": key[0],
                "project_name_without_version": key[1],
                "rule_id": key[2],
                "file_path": key[3],
                "line_content": key[4],
            },
            "count": len(items),
            "records": [
                {
                    "id": it["id"],
                    "project_name_with_version": it["project_name_with_version"],
                    "line_number": it.get("line_number"),
                    "label": it.get("label"),
                    "llm_label": it.get("llm_label"),
                    "full_file_path": it.get("full_file_path"),
                }
                for it in items
            ],
        })

    result = {
        "summary": {
            "total_records": len(data),
            "unique_groups": unique_count,
            "duplicate_groups": len(dup_groups),
            "records_in_duplicate_groups": total_in_dup,
            "redundant_copies": total_in_dup - len(dup_groups),
            "duplicate_rate_pct": round(total_in_dup / len(data) * 100, 2),
            "missing_file_records": missing_file,
        },
        "size_distribution": {str(k): v for k, v in sorted(size_dist.items())},
        "project_stats": {
            proj: {
                "total": st["total"],
                "dup_records": st["dup"],
                "dup_rate_pct": round(st["dup"] / st["total"] * 100, 2) if st["total"] else 0,
            }
            for proj in sorted(proj_stats)
        },
        "duplicate_groups": dup_details,
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n详细结果已保存至: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
