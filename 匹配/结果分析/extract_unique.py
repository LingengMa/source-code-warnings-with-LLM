#!/usr/bin/env python3
"""
从 llm_results.json 中提取 649 条去重后的唯一警告。

去重策略：
  - 重复判定标准与 analyze_duplicates.py 一致：
    tool_name / project_name_without_version / rule_id / file_path / line_content 均相同
  - 同一重复组内，保留 id 最小的那条（最早出现的版本）
"""

import json
import os
import re

INPUT_FILE  = "input/llm_results.json"
OUTPUT_FILE = "input/unique_warnings.json"


def get_project_name_without_version(name: str) -> str:
    return re.sub(r'-[\d][^-]*$', '', name)


def read_line(full_file_path: str, line_number: int) -> str | None:
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


def main():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"原始记录数: {len(data)}")

    # 按去重 key 分组，每组保留 id 最小的记录
    seen: dict[tuple, dict] = {}

    for item in data:
        proj_no_ver = get_project_name_without_version(
            item.get('project_name_with_version', '')
        )
        line_content = read_line(item.get('full_file_path', ''), item.get('line_number'))

        key = (
            item.get('tool_name', ''),
            proj_no_ver,
            item.get('rule_id', ''),
            item.get('file_path', ''),
            line_content,
        )

        if key not in seen or item['id'] < seen[key]['id']:
            seen[key] = item

    unique = sorted(seen.values(), key=lambda x: x['id'])

    # 清理临时辅助字段（如有）
    for item in unique:
        item.pop('_project_no_ver', None)
        item.pop('_line_content', None)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)

    print(f"去重后记录数: {len(unique)}")
    print(f"结果已保存至: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
