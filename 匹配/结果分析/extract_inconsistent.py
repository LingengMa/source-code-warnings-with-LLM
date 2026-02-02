#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取 llm_results.json 中 label 和 llm_label 不一致的条目
"""

import json
import os


def extract_inconsistent_labels(input_file, output_file=None):
    """
    提取 label 和 llm_label 不一致的条目
    
    Args:
        input_file: 输入的 JSON 文件路径
        output_file: 输出的 JSON 文件路径（可选，默认为 inconsistent_labels.json）
    """
    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取不一致的条目
    inconsistent_items = []
    for item in data:
        if item.get('label') != item.get('llm_label'):
            inconsistent_items.append(item)
    
    # 设置默认输出文件路径
    if output_file is None:
        output_dir = os.path.dirname(input_file)
        output_file = os.path.join(output_dir, 'inconsistent_labels.json')
    
    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inconsistent_items, f, ensure_ascii=False, indent=2)
    
    # 打印统计信息
    total_count = len(data)
    inconsistent_count = len(inconsistent_items)
    consistent_count = total_count - inconsistent_count
    
    print(f"总条目数: {total_count}")
    print(f"一致条目数: {consistent_count}")
    print(f"不一致条目数: {inconsistent_count}")
    print(f"不一致率: {inconsistent_count / total_count * 100:.2f}%")
    print(f"\n结果已保存到: {output_file}")
    
    # 返回不一致的条目
    return inconsistent_items


if __name__ == '__main__':
    # 输入文件路径
    input_file = 'input/llm_results.json'
    
    # 提取不一致的条目
    inconsistent_items = extract_inconsistent_labels(input_file)
    
    # 可选：显示前几个不一致的条目示例
    print("\n前 3 个不一致条目示例:")
    for i, item in enumerate(inconsistent_items[:3], 1):
        print(f"\n--- 示例 {i} ---")
        print(f"ID: {item.get('id')}")
        print(f"Label: {item.get('label')}")
        print(f"LLM Label: {item.get('llm_label')}")
        print(f"Project: {item.get('project_name_with_version')}")
        print(f"Rule: {item.get('rule_id')}")
