#!/usr/bin/env python3
"""
结果过滤器

此脚本用于过滤 results.json 文件中的条目,过滤条件:
  1. 去除 file_path 以 "test/" 开头的测试文件
  2. 仅保留 CWE Top 25 的条目
  3. 去除各项目最新版本的条目
  4. 去除源码行内容为 #include 的条目
"""

import json
import argparse
from pathlib import Path
from packaging.version import Version

# CWE Top 25 (2024) 编号集合
CWE_TOP25 = {
    "CWE-79",  "CWE-89",  "CWE-352", "CWE-862", "CWE-787",
    "CWE-22",  "CWE-416", "CWE-125", "CWE-78",  "CWE-94",
    "CWE-120", "CWE-434", "CWE-476", "CWE-121", "CWE-502",
    "CWE-122", "CWE-863", "CWE-20",  "CWE-284", "CWE-200",
    "CWE-306", "CWE-918", "CWE-77",  "CWE-639", "CWE-770",
}

# 仓库根目录（相对于脚本所在目录）
REPO_BASE = Path(__file__).parent / "input" / "repository"


def get_source_line(item: dict) -> str | None:
    """
    根据条目中的 project_name_with_version、file_path、line_number
    读取对应源码行，返回去除首尾空白后的字符串；读取失败则返回 None。
    """
    project = item.get("project_name_with_version", "")
    file_path = item.get("file_path", "")
    line_no = item.get("line_number")
    if not project or not file_path or not line_no:
        return None
    src_file = REPO_BASE / project / file_path
    try:
        with open(src_file, "r", encoding="utf-8", errors="replace") as f:
            for i, line in enumerate(f, start=1):
                if i == line_no:
                    return line.strip()
    except OSError:
        return None
    return None


def is_cwe_top25(item: dict) -> bool:
    """判断条目是否属于 CWE Top 25"""
    cwes = item.get("cwe")
    if not cwes:
        return False
    # cwe 字段可能是列表，如 ["CWE-787"]
    if isinstance(cwes, list):
        return any(c in CWE_TOP25 for c in cwes)
    return str(cwes) in CWE_TOP25


def filter_results(input_file, output_file=None, verbose=False):
    """
    过滤结果条目，依次应用以下规则:
      1. 去除 file_path 以 "test/" 开头的测试文件
      2. 仅保留 CWE Top 25 的条目
      3. 去除各项目最新版本的条目
      4. 去除源码行内容以 #include 开头的条目

    Args:
        input_file: 输入的 JSON 文件路径
        output_file: 输出的 JSON 文件路径(默认为 <input>_filtered.json)
        verbose: 是否显示详细信息

    Returns:
        过滤后的结果列表
    """
    # 读取原始数据
    print(f"正在读取文件: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    original_count = len(data)
    print(f"原始条目数: {original_count}")

    # ── 过滤 1: 去除测试文件 ──────────────────────────────────────
    after_test = [
        item for item in data
        if not item.get('file_path', '').startswith('test/')
    ]
    removed_test = original_count - len(after_test)
    print(f"[1] 去除测试文件后: {len(after_test)} 条  (移除 {removed_test})")

    # ── 过滤 2: 仅保留 CWE Top 25 ────────────────────────────────
    after_cwe = [item for item in after_test if is_cwe_top25(item)]
    removed_cwe = len(after_test) - len(after_cwe)
    print(f"[2] 仅保留 CWE Top 25 后: {len(after_cwe)} 条  (移除 {removed_cwe})")

    # ── 过滤 3: 去除各项目最新版本的条目 ────────────────────────────
    proj_latest: dict[str, str] = {}
    for item in after_cwe:
        proj = item.get("project_name", "")
        ver = item.get("project_version", "")
        if not proj or not ver:
            continue
        try:
            if proj not in proj_latest or Version(ver) > Version(proj_latest[proj]):
                proj_latest[proj] = ver
        except Exception:
            pass

    if verbose:
        print("     各项目最新版本:")
        for p, v in sorted(proj_latest.items()):
            print(f"       {p}: {v}")

    after_latest = [
        item for item in after_cwe
        if item.get("project_version") != proj_latest.get(item.get("project_name", ""))
    ]
    removed_latest = len(after_cwe) - len(after_latest)
    print(f"[3] 去除各项目最新版本后: {len(after_latest)} 条  (移除 {removed_latest})")

    # ── 过滤 4: 去除源码行以 #include 开头的条目 ──────────────────
    print(f"[4] 正在读取源码行以过滤 #include 条目，请稍候...")
    after_include = []
    removed_include = 0
    for item in after_latest:
        src_line = get_source_line(item)
        if src_line is not None and src_line.startswith('#include'):
            removed_include += 1
            if verbose:
                print(f"     跳过 #include: {item.get('project_name_with_version')}/"
                      f"{item.get('file_path')}:{item.get('line_number')}")
        else:
            after_include.append(item)
    print(f"[4] 去除 #include 行后: {len(after_include)} 条  (移除 {removed_include})")

    filtered_data = after_include
    filtered_count = len(filtered_data)
    total_removed = original_count - filtered_count
    print(f"\n最终条目数: {filtered_count}  (共移除 {total_removed},"
          f" {total_removed/original_count*100:.2f}%)")
    
    # 确定输出文件路径
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}_filtered{input_path.suffix}"

    # 写入过滤后的数据
    print(f"\n正在写入文件: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, indent=4, ensure_ascii=False)

    print(f"✓ 过滤完成!")

    return filtered_data


# 保留别名以兼容旧调用
filter_test_files = filter_results


def main():
    parser = argparse.ArgumentParser(
        description='过滤 results.json 文件,去除测试文件的条目'
    )
    parser.add_argument(
        '-i', '--input',
        default='results.json',
        help='输入文件路径 (默认: results.json)'
    )
    parser.add_argument(
        '-o', '--output',
        help='输出文件路径 (默认: <输入文件名>_filtered.json)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='显示详细信息'
    )
    
    args = parser.parse_args()
    
    try:
        filter_results(args.input, args.output, args.verbose)
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{args.input}'")
        return 1
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return 1
    except Exception as e:
        print(f"错误: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
