#!/usr/bin/env python3
"""
将 data.json 文件中的数据添加编号ID,并提取指定字段,输出到 data_for_llm.json
"""

import json
import os


def process_data():
    """处理 data.json 并输出到 data_for_llm.json"""
    
    # 文件路径
    input_file = 'input/data.json'
    output_file = 'input/data_for_llm.json'
    
    # 需要提取的字段(注意：sliced_code 将从 complete_code 字段获取)
    fields_to_extract = [
        'tool_name',
        'project_name_with_version',
        'project_version',
        'line_number',
        'function_name',
        'rule_id',
        'message'
    ]
    
    print(f"正在读取文件: {input_file}")
    
    # 读取原始数据
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"错误: 文件 {input_file} 不存在")
        return
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败 - {e}")
        return
    
    print(f"成功读取 {len(data)} 条记录")
    
    # 处理数据
    processed_data = []
    
    for idx, item in enumerate(data, start=1):
        # 创建新的记录
        new_item = {'id': idx}
        
        # 提取指定字段
        for field in fields_to_extract:
            # 如果字段存在则添加,否则设置为 null
            new_item[field] = item.get(field, None)
        
        # 将 complete_code 字段作为 sliced_code 输出
        new_item['sliced_code'] = item.get('complete_code', None)
        
        processed_data.append(new_item)
    
    # 写入输出文件
    print(f"正在写入文件: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"成功处理 {len(processed_data)} 条记录")
    print(f"输出文件: {output_file}")
    
    # 显示第一条记录作为示例
    if processed_data:
        print("\n第一条记录示例:")
        print(json.dumps(processed_data[0], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    process_data()
