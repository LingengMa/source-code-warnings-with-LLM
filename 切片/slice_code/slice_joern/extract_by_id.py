#!/usr/bin/env python3
"""
从 data copy.json 中按 id 提取指定条目，覆盖写入 data.json
用法：
    python extract_by_id.py 1 2 3
    python extract_by_id.py 1-10
    python extract_by_id.py 1 5 10-20 23
"""

import json
import os
import sys

SOURCE_FILE = os.path.join(os.path.dirname(__file__), "slice_input", "data copy.json")
TARGET_FILE = os.path.join(os.path.dirname(__file__), "slice_input", "data.json")


def parse_id_args(args: list[str]) -> list[int]:
    """
    解析命令行 id 参数，支持：
      - 单个 id：  23
      - 范围：     1-10  （含两端）
      - 混合：     1 5 10-20 23
    """
    ids = []
    for arg in args:
        if '-' in arg:
            parts = arg.split('-', 1)
            try:
                start, end = int(parts[0]), int(parts[1])
                ids.extend(range(start, end + 1))
            except ValueError:
                print(f"[警告] 无法解析范围参数: {arg!r}，已跳过")
        else:
            try:
                ids.append(int(arg))
            except ValueError:
                print(f"[警告] 无法解析 id 参数: {arg!r}，已跳过")
    return ids


def main():
    if len(sys.argv) < 2:
        print("用法: python extract_by_id.py <id [id ...]>")
        print("示例: python extract_by_id.py 1 2 3")
        print("      python extract_by_id.py 1-10")
        print("      python extract_by_id.py 1 5 10-20 23")
        sys.exit(1)

    target_ids = set(parse_id_args(sys.argv[1:]))
    if not target_ids:
        print("[错误] 未解析到任何有效 id")
        sys.exit(1)

    print(f"[信息] 目标 id 集合（共 {len(target_ids)} 个）: {sorted(target_ids)}")

    # 读取源文件
    print(f"[信息] 读取源文件: {SOURCE_FILE}")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print("[错误] 源文件格式不是 JSON 数组")
        sys.exit(1)

    # 过滤
    result = [item for item in data if item.get("id") in target_ids]

    # 检查哪些 id 未找到
    found_ids = {item.get("id") for item in result}
    missing = target_ids - found_ids
    if missing:
        print(f"[警告] 以下 id 在源文件中不存在: {sorted(missing)}")

    print(f"[信息] 提取到 {len(result)} 条记录")

    # 覆盖写入目标文件
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"[完成] 已写入: {TARGET_FILE}")


if __name__ == "__main__":
    main()
