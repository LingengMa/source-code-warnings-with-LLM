#!/usr/bin/env python3
"""
结果过滤器 - 去除测试文件

此脚本用于过滤 results.json 文件中的条目,
去除 file_path 以 "test/" 开头的测试文件。
"""

import json
import argparse
from pathlib import Path


def filter_test_files(input_file, output_file=None, verbose=False):
    """
    过滤掉测试文件的结果条目
    
    Args:
        input_file: 输入的 JSON 文件路径
        output_file: 输出的 JSON 文件路径(默认为 input_file_filtered.json)
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
    
    # 过滤掉 file_path 以 "test/" 开头的条目
    filtered_data = [
        item for item in data 
        if not item.get('file_path', '').startswith('test/')
    ]
    
    filtered_count = len(filtered_data)
    removed_count = original_count - filtered_count
    
    print(f"过滤后条目数: {filtered_count}")
    print(f"已移除条目数: {removed_count} ({removed_count/original_count*100:.2f}%)")
    
    # 如果启用详细模式,显示一些被移除的示例
    if verbose and removed_count > 0:
        print("\n被移除的测试文件示例:")
        test_files = set()
        for item in data:
            if item.get('file_path', '').startswith('test/'):
                test_files.add(item['file_path'])
                if len(test_files) >= 10:
                    break
        for i, file_path in enumerate(sorted(test_files), 1):
            print(f"  {i}. {file_path}")
        if removed_count > len(test_files):
            print(f"  ... 及其他 {removed_count - len(test_files)} 个测试文件")
    
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
        filter_test_files(args.input, args.output, args.verbose)
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
