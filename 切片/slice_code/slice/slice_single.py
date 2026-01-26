#!/usr/bin/env python3
"""
单文件切片示例 - 对指定的单个文件和行号执行切片
"""

import sys
import json
from slice_analyzer import CSemanticSlicer


def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("Usage: python slice_single.py <file_path> <line_number> [options]")
        print("Options:")
        print("  --no-interprocedural  禁用过程间分析")
        print("  --max-call-depth N    函数调用追踪的最大深度 (默认: 1)")
        print("\nExample: python slice_single.py input/repository/vim-9.1.1896/src/netbeans.c 2292")
        sys.exit(1)
    
    file_path = sys.argv[1]
    target_line = int(sys.argv[2])
    
    # 解析选项
    enable_interprocedural = True
    max_call_depth = 1
    
    for i, arg in enumerate(sys.argv[3:]):
        if arg == '--no-interprocedural':
            enable_interprocedural = False
        elif arg == '--max-call-depth' and i + 4 < len(sys.argv):
            max_call_depth = int(sys.argv[i + 4])
    
    # 自动检测文件类型
    is_cpp = file_path.endswith(('.cpp', '.cc', '.cxx', '.hpp', '.hxx'))
    
    print(f"分析文件: {file_path}")
    print(f"目标行: {target_line}")
    print(f"文件类型: {'C++' if is_cpp else 'C'}")
    print(f"过程间分析: {'启用' if enable_interprocedural else '禁用'}")
    if enable_interprocedural:
        print(f"最大调用深度: {max_call_depth}")
    print("="*60)
    
    # 执行切片
    slicer = CSemanticSlicer(is_cpp=is_cpp)
    result = slicer.slice(file_path, target_line,
                         enable_interprocedural=enable_interprocedural,
                         max_call_depth=max_call_depth)
    
    if not result:
        print("错误: 无法解析文件")
        sys.exit(1)
    
    # 显示结果
    print(f"\n语义锚点 ({len(result.anchors)} 个):")
    for anchor in sorted(result.anchors):
        print(f"  - {anchor}")
    
    print(f"\n切片大小: {len(result.slice_lines)} 行")
    print(f"切片行号: {sorted(result.slice_lines)}")
    
    print(f"\n函数分布:")
    func_counts = {}
    for line, func in result.function_map.items():
        func_counts[func] = func_counts.get(func, 0) + 1
    
    for func, count in sorted(func_counts.items()):
        print(f"  {func}: {count} 行")
    
    # 显示指针和函数调用信息
    if enable_interprocedural and hasattr(slicer, 'pointer_aliases'):
        if slicer.pointer_aliases:
            print(f"\n指针别名关系:")
            for ptr, aliases in list(slicer.pointer_aliases.items())[:5]:
                if aliases:
                    print(f"  {ptr} -> {aliases}")
        
        if slicer.call_graph:
            print(f"\n函数调用关系:")
            relevant_funcs = set(result.function_map.values())
            for caller, callees in slicer.call_graph.items():
                if caller in relevant_funcs:
                    print(f"  {caller} -> {callees}")
    
    # 显示代码
    print(f"\n切片代码预览:")
    print("="*60)
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        sorted_lines = sorted(result.slice_lines)
        
        for i, line_num in enumerate(sorted_lines):
            # 如果行号跳跃较大，添加分隔
            if i > 0 and line_num - sorted_lines[i-1] > 1:
                print("    ...")
            
            line_content = lines[line_num - 1].rstrip('\n')
            marker = ">>>" if line_num == target_line else "***"
            func_name = result.function_map.get(line_num, '')
            func_info = f" [{func_name}]" if func_name else ""
            
            print(f"{marker} {line_num:4d} | {line_content}{func_info}")
    
    except Exception as e:
        print(f"错误: 无法读取文件 - {e}")
    
    # 保存结果
    output_file = f"output/slice_{target_line}.json"
    import os
    os.makedirs('output', exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result.to_dict(), f, indent=2, ensure_ascii=False)
    
    print(f"\n结果已保存到: {output_file}")


if __name__ == '__main__':
    main()
