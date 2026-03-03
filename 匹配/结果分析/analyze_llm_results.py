#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析 llm_results.json 文件中 llm_label 和 label 的一致性。
"""

import json
from collections import defaultdict
import os

# --- 配置 ---
# 输入文件路径
INPUT_FILE = os.path.join('input', 'llm_results.json')

def analyze_labels(file_path):
    """
    分析JSON文件中的标签一致性。

    Args:
        file_path (str): 输入的JSON文件路径。

    Returns:
        dict: 包含分析结果的字典，如果文件不存在则返回None。
    """
    if not os.path.exists(file_path):
        print(f"❌ 错误: 文件 '{file_path}' 不存在。")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"❌ 错误: 文件 '{file_path}' 不是有效的JSON格式。")
        return None
    except Exception as e:
        print(f"❌ 错误: 读取文件时发生错误: {e}")
        return None

    if not isinstance(data, list):
        print("❌ 错误: JSON文件的顶层结构应该是一个列表。")
        return None

    counts = defaultdict(int)
    total_records = 0

    for record in data:
        if 'llm_label' not in record or 'label' not in record:
            counts['missing_labels'] += 1
            continue

        total_records += 1
        llm_label = record['llm_label']
        manual_label = record['label']

        # 构建组合键，例如 "LLM_TP_vs_Manual_FP"
        key = f"LLM_{llm_label}_vs_Manual_{manual_label}"
        counts[key] += 1

    # --- 结果计算 ---
    llm_tp_manual_tp = counts.get('LLM_TP_vs_Manual_TP', 0)
    llm_fp_manual_fp = counts.get('LLM_FP_vs_Manual_FP', 0)
    llm_tp_manual_fp = counts.get('LLM_TP_vs_Manual_FP', 0)
    llm_fp_manual_tp = counts.get('LLM_FP_vs_Manual_TP', 0)
    llm_unknown_manual_tp = counts.get('LLM_Unknown_vs_Manual_TP', 0)
    llm_unknown_manual_fp = counts.get('LLM_Unknown_vs_Manual_FP', 0)

    consistent_count = llm_tp_manual_tp + llm_fp_manual_fp
    inconsistent_count = llm_tp_manual_fp + llm_fp_manual_tp
    unknown_count = llm_unknown_manual_tp + llm_unknown_manual_fp
    
    # 用于计算比率的总数，不包括标签缺失的记录
    valid_records = consistent_count + inconsistent_count + unknown_count

    # --- 结果组装 ---
    results = {
        "total_records": total_records,
        "valid_records": valid_records,
        "counts": {
            "llm_tp_manual_tp": llm_tp_manual_tp,
            "llm_fp_manual_fp": llm_fp_manual_fp,
            "llm_tp_manual_fp": llm_tp_manual_fp,
            "llm_fp_manual_tp": llm_fp_manual_tp,
            "llm_unknown_manual_tp": llm_unknown_manual_tp,
            "llm_unknown_manual_fp": llm_unknown_manual_fp,
            "missing_labels": counts['missing_labels']
        },
        "summary": {
            "consistent_count": consistent_count,
            "inconsistent_count": inconsistent_count,
            "unknown_count": unknown_count,
            "consistent_rate": (consistent_count / valid_records) if valid_records > 0 else 0,
            "inconsistent_rate": (inconsistent_count / valid_records) if valid_records > 0 else 0,
            "unknown_rate": (unknown_count / valid_records) if valid_records > 0 else 0,
        },
        "rates": {
            "llm_tp_manual_tp_rate": (llm_tp_manual_tp / valid_records) if valid_records > 0 else 0,
            "llm_fp_manual_fp_rate": (llm_fp_manual_fp / valid_records) if valid_records > 0 else 0,
            "llm_tp_manual_fp_rate": (llm_tp_manual_fp / valid_records) if valid_records > 0 else 0,
            "llm_fp_manual_tp_rate": (llm_fp_manual_tp / valid_records) if valid_records > 0 else 0,
            "llm_unknown_manual_tp_rate": (llm_unknown_manual_tp / valid_records) if valid_records > 0 else 0,
            "llm_unknown_manual_fp_rate": (llm_unknown_manual_fp / valid_records) if valid_records > 0 else 0,
        }
    }
    return results

def print_report(results):
    """
    打印格式化的分析报告。

    Args:
        results (dict): analyze_labels函数返回的结果字典。
    """
    if not results:
        return

    total = results['total_records']
    valid_total = results['valid_records']
    counts = results['counts']
    summary = results['summary']
    rates = results['rates']

    print("\n" + "="*60)
    print("📊 LLM 与算法标签一致性分析报告")
    print("="*60)
    print(f"总记录数 (含标签缺失): {total}")
    print(f"有效记录数 (用于计算比率): {valid_total}\n")

    print("--- 详细分类 ---")
    print(f"  ✅ LLM: TP, 算法: TP      : {counts['llm_tp_manual_tp']:>5} 条 ({rates['llm_tp_manual_tp_rate']:>7.2%})")
    print(f"  ✅ LLM: FP, 算法: FP      : {counts['llm_fp_manual_fp']:>5} 条 ({rates['llm_fp_manual_fp_rate']:>7.2%})")
    print(f"  ❌ LLM: TP, 算法: FP      : {counts['llm_tp_manual_fp']:>5} 条 ({rates['llm_tp_manual_fp_rate']:>7.2%})")
    print(f"  ❌ LLM: FP, 算法: TP      : {counts['llm_fp_manual_tp']:>5} 条 ({rates['llm_fp_manual_tp_rate']:>7.2%})")
    print(f"  ❓ LLM: Unknown, 算法: TP : {counts['llm_unknown_manual_tp']:>5} 条 ({rates['llm_unknown_manual_tp_rate']:>7.2%})")
    print(f"  ❓ LLM: Unknown, 算法: FP : {counts['llm_unknown_manual_fp']:>5} 条 ({rates['llm_unknown_manual_fp_rate']:>7.2%})")
    
    if counts['missing_labels'] > 0:
        print(f"  ⚠️ 缺少标签的记录     : {counts['missing_labels']:>5} 条")
    
    print("\n" + "-"*60)
    print("--- 总体概览 (基于有效记录) ---")
    print(f"  👍 一致总数: {summary['consistent_count']:>5} 条")
    print(f"  👎 不一致总数: {summary['inconsistent_count']:>5} 条")
    print(f"  🤔 LLM 未知总数: {summary['unknown_count']:>5} 条")
    print(f"  📈 一致率: {summary['consistent_rate']:>7.2%}")
    print(f"  📉 不一致率: {summary['inconsistent_rate']:>7.2%}")
    print(f"  🧐 LLM 未知率: {summary['unknown_rate']:>7.2%}")
    print("="*60)


if __name__ == '__main__':
    analysis_results = analyze_labels(INPUT_FILE)
    if analysis_results:
        print_report(analysis_results)
