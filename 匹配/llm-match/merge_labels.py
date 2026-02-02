#!/usr/bin/env python3
"""
将 data.json 中的 label 字段缝合到 llm_results.json 中
根据记录的顺序位置进行匹配（因为 id 是按顺序生成的）
"""

import json
import os


def merge_labels():
    """将原始数据中的label字段合并到LLM结果中"""
    
    # 文件路径
    data_file = 'input/data.json'
    results_file = 'output/llm_results.json'
    output_file = 'output/llm_results_with_labels.json'
    
    print(f"正在读取文件: {data_file}")
    
    # 读取原始数据
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"错误: 文件 {data_file} 不存在")
        return
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return
    
    print(f"成功读取 {len(data)} 条原始记录")
    
    print(f"正在读取文件: {results_file}")
    
    # 读取LLM结果
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
    except FileNotFoundError:
        print(f"错误: 文件 {results_file} 不存在")
        return
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return
    
    print(f"成功读取 {len(results)} 条LLM结果记录")
    
    # 创建id到label的映射（基于数组索引）
    # data.json 的第 i 个元素对应 id = i + 1
    id_to_label = {}
    for idx, item in enumerate(data, start=1):
        label = item.get('label', None)
        id_to_label[idx] = label
    
    print(f"创建了 {len(id_to_label)} 个ID到Label的映射")
    
    # 合并label到结果中
    merged_count = 0
    missing_count = 0
    
    for result in results:
        result_id = result.get('id')
        if result_id in id_to_label:
            result['label'] = id_to_label[result_id]
            merged_count += 1
        else:
            result['label'] = None
            missing_count += 1
            print(f"警告: ID {result_id} 在原始数据中找不到对应的记录")
    
    # 保存合并后的结果
    print(f"\n正在写入文件: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n合并完成!")
    print(f"  - 成功合并: {merged_count} 条")
    print(f"  - 未找到匹配: {missing_count} 条")
    print(f"  - 输出文件: {output_file}")
    
    # 显示第一条记录作为示例
    if results:
        print("\n第一条记录示例:")
        first_record = results[0]
        print(f"  ID: {first_record.get('id')}")
        print(f"  Label (真实标签): {first_record.get('label')}")
        print(f"  LLM Label (LLM预测): {first_record.get('llm_label')}")
        print(f"  Rule ID: {first_record.get('rule_id')}")
        
        # 如果两者都存在，显示是否一致
        if first_record.get('label') and first_record.get('llm_label'):
            match = first_record.get('label') == first_record.get('llm_label')
            print(f"  匹配状态: {'✓ 一致' if match else '✗ 不一致'}")


if __name__ == '__main__':
    merge_labels()
