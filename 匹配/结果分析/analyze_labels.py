#!/usr/bin/env python3
"""
分析 llm_results.json 中 label 与 llm_label 的一致性情况
统计四种情况的数量：
1. 均为 TP
2. label 为 TP，llm_label 为 FP
3. label 为 FP，llm_label 为 TP
4. 均为 FP
"""

import json
from pathlib import Path


def analyze_labels(input_file):
    """分析标签一致性"""
    
    # 读取 JSON 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 初始化计数器
    both_tp = 0  # 均为 TP
    label_tp_llm_fp = 0  # label 为 TP，llm_label 为 FP
    label_fp_llm_tp = 0  # label 为 FP，llm_label 为 TP
    both_fp = 0  # 均为 FP
    
    # 遍历数据统计
    for item in data:
        label = item.get('label', '').upper()
        llm_label = item.get('llm_label', '').upper()
        
        if label == 'TP' and llm_label == 'TP':
            both_tp += 1
        elif label == 'TP' and llm_label == 'FP':
            label_tp_llm_fp += 1
        elif label == 'FP' and llm_label == 'TP':
            label_fp_llm_tp += 1
        elif label == 'FP' and llm_label == 'FP':
            both_fp += 1
    
    # 计算总数
    total = len(data)
    
    # 输出统计结果
    print("=" * 60)
    print("标签一致性分析结果")
    print("=" * 60)
    print(f"数据总数: {total}")
    print("-" * 60)
    print(f"1. 均为 TP (label=TP, llm_label=TP):          {both_tp:6d} ({both_tp/total*100:6.2f}%)")
    print(f"2. 一个TP一个FP (label=TP, llm_label=FP):     {label_tp_llm_fp:6d} ({label_tp_llm_fp/total*100:6.2f}%)")
    print(f"3. 一个FP一个TP (label=FP, llm_label=TP):     {label_fp_llm_tp:6d} ({label_fp_llm_tp/total*100:6.2f}%)")
    print(f"4. 均为 FP (label=FP, llm_label=FP):          {both_fp:6d} ({both_fp/total*100:6.2f}%)")
    print("-" * 60)
    
    # 计算一致性
    consistent = both_tp + both_fp
    inconsistent = label_tp_llm_fp + label_fp_llm_tp
    
    print(f"\n一致情况 (label == llm_label):               {consistent:6d} ({consistent/total*100:6.2f}%)")
    print(f"不一致情况 (label != llm_label):             {inconsistent:6d} ({inconsistent/total*100:6.2f}%)")
    print("=" * 60)
    
    return {
        'total': total,
        'both_tp': both_tp,
        'label_tp_llm_fp': label_tp_llm_fp,
        'label_fp_llm_tp': label_fp_llm_tp,
        'both_fp': both_fp,
        'consistent': consistent,
        'inconsistent': inconsistent
    }


if __name__ == '__main__':
    input_file = Path(__file__).parent / 'input' / 'llm_results.json'
    
    if not input_file.exists():
        print(f"错误: 找不到文件 {input_file}")
        exit(1)
    
    analyze_labels(input_file)
