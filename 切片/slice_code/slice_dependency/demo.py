#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示脚本 - 展示工具核心功能
分析单个项目的一个示例
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from slice_analyzer import CProjectIndexer

def demo():
    print("=" * 70)
    print("代码切片和依赖分析工具 - 演示")
    print("=" * 70)
    
    # 选择一个较小的项目进行演示
    repo_dir = Path(__file__).parent / 'input' / 'repository'
    
    # 查找一个中等规模的项目
    projects = sorted([d for d in repo_dir.iterdir() if d.is_dir()])
    
    demo_project = None
    for proj in projects:
        if 'redis' in proj.name.lower():
            demo_project = proj
            break
    
    if not demo_project:
        demo_project = projects[0] if projects else None
    
    if not demo_project:
        print("错误: 没有找到项目")
        return
    
    print(f"\n📦 演示项目: {demo_project.name}")
    print()
    
    # 创建索引器
    indexer = CProjectIndexer()
    
    # 索引项目
    print("步骤 1: 构建索引")
    print("-" * 70)
    indexer.index_project(str(demo_project), demo_project.name)
    
    # 显示统计信息
    func_count = len(indexer.function_index[demo_project.name])
    total_funcs = sum(len(funcs) for funcs in indexer.function_index[demo_project.name].values())
    
    print(f"\n统计:")
    print(f"  - 不同函数名数量: {func_count}")
    print(f"  - 函数定义总数: {total_funcs}")
    print(f"  - 文件数量: {len(indexer.file_functions[demo_project.name])}")
    
    # 显示一些示例函数
    print(f"\n示例函数（前10个）:")
    for i, func_name in enumerate(list(indexer.function_index[demo_project.name].keys())[:10], 1):
        func_infos = indexer.function_index[demo_project.name][func_name]
        print(f"  {i}. {func_name} ({len(func_infos)} 个定义)")
    
    # 选择一个有调用关系的函数进行依赖分析
    print(f"\n" + "=" * 70)
    print("步骤 2: 依赖分析演示")
    print("-" * 70)
    
    # 找一个有调用的函数
    target_func = None
    target_name = None
    
    for func_name, func_infos in indexer.function_index[demo_project.name].items():
        for func_info in func_infos:
            if len(func_info.calls) > 0:
                target_func = func_info
                target_name = func_name
                break
        if target_func:
            break
    
    if target_func:
        print(f"\n目标函数: {target_name}")
        print(f"  文件: {Path(target_func.file_path).name}")
        print(f"  位置: 第{target_func.start_line}-{target_func.end_line}行")
        print(f"  调用的函数: {', '.join(target_func.calls[:5])}")
        if len(target_func.calls) > 5:
            print(f"              ... 还有 {len(target_func.calls) - 5} 个")
        
        # 分析依赖
        print(f"\n依赖分析（3层）:")
        dep_layers = indexer.get_dependencies(demo_project.name, target_name, depth=3)
        
        for level, layer in enumerate(dep_layers):
            print(f"\n  第{level}层: {len(layer)} 个函数")
            if level == 0:
                print(f"    - {layer[0].name} (目标函数)")
            else:
                for i, func in enumerate(layer[:3], 1):
                    print(f"    {i}. {func.name} ({Path(func.file_path).name})")
                if len(layer) > 3:
                    print(f"    ... 还有 {len(layer) - 3} 个函数")
        
        # 显示简短的代码示例
        print(f"\n" + "=" * 70)
        print("步骤 3: 代码提取演示")
        print("-" * 70)
        print(f"\n目标函数代码片段:")
        print("-" * 70)
        
        code_lines = target_func.full_text.split('\n')
        preview_lines = min(15, len(code_lines))
        for i, line in enumerate(code_lines[:preview_lines], target_func.start_line):
            print(f"{i:4d} | {line}")
        
        if len(code_lines) > preview_lines:
            print(f"     | ... (共 {len(code_lines)} 行)")
    
    else:
        print("未找到有调用关系的函数")
    
    print("\n" + "=" * 70)
    print("✅ 演示完成!")
    print("=" * 70)
    print("\n提示:")
    print("  - 运行 'python slice_analyzer.py' 处理完整数据集")
    print("  - 运行 'python run.py' 使用交互式界面")
    print("  - 查看 'USAGE.md' 了解详细使用说明")

if __name__ == '__main__':
    demo()
