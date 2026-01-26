#!/usr/bin/env python3
"""查看当前切片结果"""
import json

with open('slice_output/slices.json', 'r') as f:
    data = json.load(f)

result = data[0]
print("="*70)
print("元数据:")
print("="*70)
print(f"函数: {result['function_name']}")
print(f"行范围: {result['function_start_line']}-{result['function_end_line']}")
print(f"目标行: {result['line']}")
print(f"切片行数: {len(result['slice_lines'])}")
print(f"增强后: {len(result['enhanced_slice_lines'])}")
print(f"AST enhanced: {result['metadata']['ast_enhanced']}")

print("\n" + "="*70)
print("切片行号:")
print("="*70)
print(result['slice_lines'])

print("\n" + "="*70)
print("切片代码（无占位符）:")
print("="*70)
print(result['sliced_code'])

print("\n" + "="*70)
print("切片代码（带占位符，前800字符）:")
print("="*70)
print(result['sliced_code_with_placeholder'][:800])
print("...")
