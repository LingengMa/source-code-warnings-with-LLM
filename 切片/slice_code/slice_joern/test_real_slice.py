#!/usr/bin/env python3
"""测试 AST 增强在实际切片中的效果"""

import logging
import json
import sys

# 设置详细日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s: %(message)s'
)

from single_file_slicer import slice_single_task

# 加载任务
with open('slice_input/data.json', 'r') as f:
    tasks = json.load(f)

task = tasks[0]
print(f'\n{"="*60}')
print(f'处理任务: {task["file"]}:{task["line"]}')
print(f'{"="*60}\n')

result = slice_single_task(task)

print(f'\n{"="*60}')
print(f'结果:')
print(f'{"="*60}')
print(f'状态: {result["status"]}')
print(f'AST enhanced: {result["metadata"]["ast_enhanced"]}')
print(f'原始切片行数: {len(result["slice_lines"])}')
print(f'增强后行数: {len(result["enhanced_slice_lines"])}')

if set(result["slice_lines"]) != set(result["enhanced_slice_lines"]):
    new_lines = sorted(set(result["enhanced_slice_lines"]) - set(result["slice_lines"]))
    print(f'新增的行: {new_lines}')
else:
    print('⚠️  没有新增行')

print(f'\n{"="*60}\n')
