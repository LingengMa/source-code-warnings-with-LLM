#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证工具功能
"""

import json
import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from slice_analyzer import CProjectIndexer

def test_indexer():
    """测试索引器"""
    print("测试索引器功能...")
    
    indexer = CProjectIndexer()
    
    # 测试索引一个小项目
    repo_dir = Path(__file__).parent / 'input' / 'repository'
    projects = list(repo_dir.iterdir())[:2]  # 只测试前2个项目
    
    if not projects:
        print("错误: 没有找到项目")
        return False
    
    print(f"\n测试项目: {[p.name for p in projects]}")
    
    for project in projects:
        print(f"\n正在索引: {project.name}")
        indexer.index_project(str(project), project.name)
        
        # 检查索引结果
        if project.name in indexer.function_index:
            func_count = len(indexer.function_index[project.name])
            print(f"  ✓ 成功索引 {func_count} 个不同的函数名")
            
            # 显示一些示例函数
            if func_count > 0:
                sample_funcs = list(indexer.function_index[project.name].keys())[:5]
                print(f"  示例函数: {sample_funcs}")
        else:
            print(f"  ✗ 索引失败")
            return False
    
    print("\n✓ 索引器测试通过!")
    return True

def test_data_loading():
    """测试数据加载"""
    print("\n测试数据加载...")
    
    data_file = Path(__file__).parent / 'input' / 'data.json'
    
    if not data_file.exists():
        print(f"错误: 数据文件不存在 {data_file}")
        return False
    
    print(f"数据文件: {data_file}")
    print(f"文件大小: {data_file.stat().st_size / 1024 / 1024:.2f} MB")
    
    # 尝试读取前几条
    try:
        import subprocess
        result = subprocess.run(
            ['head', '-n', '50', str(data_file)],
            capture_output=True,
            text=True
        )
        
        # 尝试解析JSON片段
        if result.returncode == 0:
            print("\n前几条数据预览:")
            print(result.stdout[:500] + "...")
            print("\n✓ 数据文件可访问")
            return True
    except Exception as e:
        print(f"错误: {e}")
        return False
    
    return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("代码切片和依赖分析工具 - 功能测试")
    print("=" * 60)
    
    # 测试1: 数据加载
    if not test_data_loading():
        print("\n✗ 数据加载测试失败")
        return
    
    # 测试2: 索引器
    if not test_indexer():
        print("\n✗ 索引器测试失败")
        return
    
    print("\n" + "=" * 60)
    print("✓ 所有测试通过!")
    print("=" * 60)
    print("\n工具已准备就绪，可以运行主程序:")
    print("  python slice_analyzer.py")

if __name__ == '__main__':
    main()
