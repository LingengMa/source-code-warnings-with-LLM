#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试新的输出格式 - 验证英文字段名
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from slice_analyzer import SliceAnalyzer

def test_output_format():
    """测试输出格式"""
    print("=" * 70)
    print("测试新输出格式（英文字段名）")
    print("=" * 70)
    
    # 选择一个小项目进行测试
    from slice_analyzer import CProjectIndexer
    
    indexer = CProjectIndexer()
    
    repo_dir = Path(__file__).parent / 'input' / 'repository'
    test_project = None
    
    # 找一个redis项目
    for proj in repo_dir.iterdir():
        if 'redis' in proj.name.lower():
            test_project = proj
            break
    
    if not test_project:
        print("错误: 找不到测试项目")
        return False
    
    print(f"\n测试项目: {test_project.name}")
    
    # 索引项目
    indexer.index_project(str(test_project), test_project.name)
    
    # 找一个有依赖的函数
    target_func = None
    for func_name, func_infos in indexer.function_index[test_project.name].items():
        for func_info in func_infos:
            if len(func_info.calls) > 0:
                target_func = func_info
                break
        if target_func:
            break
    
    if not target_func:
        print("错误: 找不到有调用关系的函数")
        return False
    
    # 获取依赖
    dep_layers = indexer.get_dependencies(test_project.name, target_func.name, depth=3)
    
    # 构建结果（使用新格式）
    result = {
        "tool_name": "codeql",
        "project_simple_name": test_project.name.split('-')[0],
        "project_name": test_project.name,
        "project_version": test_project.name.split('-')[-1] if '-' in test_project.name else "unknown",
        "defect_file": Path(target_func.file_path).relative_to(test_project).as_posix(),
        "defect_line": target_func.start_line,
        "target_function": {
            "function_name": target_func.name,
            "start_line": target_func.start_line,
            "end_line": target_func.end_line,
            "source_code": target_func.full_text,
            "called_functions": target_func.calls
        },
        "dependency_analysis": []
    }
    
    # 添加依赖层级
    for level, layer_funcs in enumerate(dep_layers[1:], 1):
        layer_info = {
            "level": level,
            "functions": [
                {
                    "function_name": func.name,
                    "file_path": func.file_path,
                    "start_line": func.start_line,
                    "end_line": func.end_line,
                    "source_code": func.full_text,
                    "called_functions": func.calls
                }
                for func in layer_funcs
            ]
        }
        result["dependency_analysis"].append(layer_info)
    
    # 保存示例结果
    output_file = Path(__file__).parent / 'output' / 'example_output.json'
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump([result], f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 示例结果已保存: {output_file}")
    
    # 验证字段
    print("\n验证输出格式:")
    required_fields = {
        'tool_name', 'project_simple_name', 'project_name', 'project_version',
        'defect_file', 'defect_line', 'target_function', 'dependency_analysis'
    }
    
    actual_fields = set(result.keys())
    
    if required_fields == actual_fields:
        print("  ✓ 顶层字段正确")
    else:
        print(f"  ✗ 字段不匹配")
        print(f"    期望: {required_fields}")
        print(f"    实际: {actual_fields}")
        return False
    
    # 验证target_function
    target_required = {'function_name', 'start_line', 'end_line', 'source_code', 'called_functions'}
    target_actual = set(result['target_function'].keys())
    
    if target_required == target_actual:
        print("  ✓ target_function字段正确")
    else:
        print(f"  ✗ target_function字段不匹配")
        return False
    
    # 验证dependency_analysis
    if result['dependency_analysis']:
        dep_layer = result['dependency_analysis'][0]
        dep_required = {'level', 'functions'}
        dep_actual = set(dep_layer.keys())
        
        if dep_required == dep_actual:
            print("  ✓ dependency_analysis结构正确")
        else:
            print(f"  ✗ dependency_analysis结构不匹配")
            return False
        
        if dep_layer['functions']:
            func = dep_layer['functions'][0]
            func_required = {'function_name', 'file_path', 'start_line', 'end_line', 'source_code', 'called_functions'}
            func_actual = set(func.keys())
            
            if func_required == func_actual:
                print("  ✓ function对象字段正确")
            else:
                print(f"  ✗ function对象字段不匹配")
                return False
    
    # 显示示例数据
    print("\n示例输出（JSON片段）:")
    print("-" * 70)
    print(json.dumps({
        "tool_name": result['tool_name'],
        "project_name": result['project_name'],
        "defect_file": result['defect_file'],
        "defect_line": result['defect_line'],
        "target_function": {
            "function_name": result['target_function']['function_name'],
            "start_line": result['target_function']['start_line'],
            "end_line": result['target_function']['end_line'],
            "called_functions": result['target_function']['called_functions']
        },
        "dependency_analysis": [
            {
                "level": layer['level'],
                "functions_count": len(layer['functions'])
            }
            for layer in result['dependency_analysis']
        ]
    }, ensure_ascii=False, indent=2))
    
    return True

def main():
    print("\n")
    
    if test_output_format():
        print("\n" + "=" * 70)
        print("✅ 输出格式测试通过!")
        print("=" * 70)
        print("\n新的输出格式特点:")
        print("  • 所有字段名使用英文")
        print("  • 结构清晰，易于解析")
        print("  • 依赖层级使用 level + functions 数组")
        print("  • 完整的类型定义（见 OUTPUT_FORMAT.md）")
        print("\n查看完整文档:")
        print("  - OUTPUT_FORMAT.md: 详细字段说明")
        print("  - output/example_output.json: 示例输出")
    else:
        print("\n✗ 测试失败")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
