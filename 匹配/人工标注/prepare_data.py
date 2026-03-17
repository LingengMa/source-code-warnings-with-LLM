#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据预处理脚本

合并 base_data.json 与四个 LLM 结果 JSON，筛选五套标签（1算法+4LLM）
不完全一致的条目，输出 data.json 供标注工具使用。

用法：
    python prepare_data.py
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGIN_DIR = os.path.join(BASE_DIR, 'input', 'origin_data')

INPUT_FILES = {
    'base': os.path.join(ORIGIN_DIR, 'base_data.json'),
    'wuwl': os.path.join(ORIGIN_DIR, 'results_with_unknown_with_label.json'),
    'wuol': os.path.join(ORIGIN_DIR, 'results_with_unknown_without_label.json'),
    'ouwl': os.path.join(ORIGIN_DIR, 'results_without_unknown_with_label.json'),
    'ouol': os.path.join(ORIGIN_DIR, 'results_without_unknown_without_label.json'),
}

OUTPUT_FILE = os.path.join(BASE_DIR, 'data.json')

LLM_MODE_LABELS = {
    'wuwl': '三分类+含算法标签',
    'wuol': '三分类+不含算法标签',
    'ouwl': '二分类+含算法标签',
    'ouol': '二分类+不含算法标签',
}


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    print('加载数据...')
    base_list = load_json(INPUT_FILES['base'])
    llm_data = {
        key: {x['id']: x for x in load_json(path)}
        for key, path in INPUT_FILES.items()
        if key != 'base'
    }

    print(f'基础数据条数: {len(base_list)}')
    for key, d in llm_data.items():
        print(f'  {key}: {len(d)} 条')

    merged = []
    skipped = 0

    for item in base_list:
        iid = item['id']
        alg_label = item.get('label')

        llm_results = {}
        for key, d in llm_data.items():
            if iid in d:
                entry = d[iid]
                llm_results[key] = {
                    'llm_label': entry.get('llm_label'),
                    'llm_label_reason': entry.get('llm_label_reason', ''),
                    'mode_desc': LLM_MODE_LABELS[key],
                }

        all_labels = [alg_label] + [v['llm_label'] for v in llm_results.values() if v['llm_label']]
        unique_labels = set(all_labels) - {None}

        if len(unique_labels) <= 1:
            skipped += 1
            continue

        record = {
            'id': iid,
            'tool_name': item.get('tool_name'),
            'project_name': item.get('project_name'),
            'project_name_with_version': item.get('project_name_with_version'),
            'project_version': item.get('project_version'),
            'file_path': item.get('file_path'),
            'line_number': item.get('line_number'),
            'cwe': item.get('cwe', []),
            'rule_id': item.get('rule_id'),
            'message': item.get('message'),
            'severity': item.get('severity'),
            'function_name': item.get('function_name'),
            'label': alg_label,
            'llm_results': llm_results,
            'sliced_code': (llm_data['wuwl'].get(iid) or {}).get('sliced_code', ''),
        }
        merged.append(record)

    print(f'\n筛选结果:')
    print(f'  总条数: {len(base_list)}')
    print(f'  一致（跳过）: {skipped}')
    print(f'  不一致（待标注）: {len(merged)}')

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f'\n已输出到: {OUTPUT_FILE}')


if __name__ == '__main__':
    main()
