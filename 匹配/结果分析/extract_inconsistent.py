#!/usr/bin/env python3
"""
提取 llm_results.json 中 label 与 llm_label 不一致的数据
将结果保存为新的 JSON 文件
"""

import json
from pathlib import Path
from datetime import datetime


def extract_inconsistent_labels(input_file, output_file):
    """提取标签不一致的记录"""
    
    # 读取 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 提取不一致的记录
    inconsistent_data = []
    
    for item in data:
        label = item.get('label', '').upper()
        llm_label = item.get('llm_label', '').upper()
        
        # 只保留不一致的记录
        if label != llm_label:
            # 添加一个字段标记不一致类型
            item_copy = item.copy()
            if label == 'TP' and llm_label == 'FP':
                item_copy['inconsistency_type'] = 'label_TP_llm_FP'
            elif label == 'FP' and llm_label == 'TP':
                item_copy['inconsistency_type'] = 'label_FP_llm_TP'
            else:
                item_copy['inconsistency_type'] = 'unknown'
            
            inconsistent_data.append(item_copy)
    
    # 保存到新的 JSON 文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inconsistent_data, f, ensure_ascii=False, indent=2)
    
    # 输出统计信息
    print("=" * 60)
    print("不一致数据提取完成")
    print("=" * 60)
    print(f"原始数据总数: {len(data)}")
    print(f"不一致记录数: {len(inconsistent_data)}")
    print(f"不一致比例:   {len(inconsistent_data)/len(data)*100:.2f}%")
    print("-" * 60)
    
    # 统计不一致类型
    label_tp_llm_fp = sum(1 for item in inconsistent_data if item['inconsistency_type'] == 'label_TP_llm_FP')
    label_fp_llm_tp = sum(1 for item in inconsistent_data if item['inconsistency_type'] == 'label_FP_llm_TP')
    
    print(f"label=TP, llm_label=FP: {label_tp_llm_fp:6d} ({label_tp_llm_fp/len(inconsistent_data)*100:6.2f}%)")
    print(f"label=FP, llm_label=TP: {label_fp_llm_tp:6d} ({label_fp_llm_tp/len(inconsistent_data)*100:6.2f}%)")
    print("-" * 60)
    print(f"输出文件: {output_file}")
    print("=" * 60)
    
    return inconsistent_data


if __name__ == '__main__':
    input_file = Path(__file__).parent / 'input' / 'llm_results.json'
    
    # 生成带时间戳的输出文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = Path(__file__).parent / f'inconsistent_labels_{timestamp}.json'
    
    # 或者使用固定文件名
    output_file = Path(__file__).parent / 'inconsistent_labels.json'
    
    if not input_file.exists():
        print(f"错误: 找不到文件 {input_file}")
        exit(1)
    
    extract_inconsistent_labels(input_file, output_file)
