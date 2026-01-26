#!/usr/bin/env python3
"""诊断 AST 增强问题"""

import logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# 读取实际的源代码文件
source_file = 'slice_input/repository/ffmpeg-6.1.1/libavcodec/motion_est_template.c'
with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
    all_lines = f.readlines()

# 函数范围：771-830
func_start = 771
func_end = 830
source_code = "".join(all_lines[func_start-1:func_end])

# 实际的切片行号（绝对行号）
slice_lines = {771, 775, 778, 779, 780, 785, 787, 788, 790, 791, 792, 796, 
               799, 800, 801, 805, 808, 809, 810, 814, 817, 818, 819, 823, 
               826, 827, 829}

print("="*70)
print("源代码（前500字符）:")
print("="*70)
print(source_code[:500])
print("...")

print("\n" + "="*70)
print("测试 AST 增强:")
print("="*70)
print(f"切片行数: {len(slice_lines)}")
print(f"函数起始行: {func_start}")

# 测试 AST 增强
try:
    from ast_enhancer import enhance_slice_with_ast
    
    enhanced_lines = enhance_slice_with_ast(
        source_code=source_code,
        slice_lines=slice_lines,
        language="c",
        function_start_line=func_start
    )
    
    print(f"✅ AST 增强成功!")
    print(f"增强后行数: {len(enhanced_lines)}")
    
    if enhanced_lines != slice_lines:
        new_lines = sorted(enhanced_lines - slice_lines)
        print(f"新增的行: {new_lines}")
        print("\n新增的代码:")
        for line_no in new_lines:
            if func_start <= line_no <= func_end:
                idx = line_no - func_start
                if 0 <= idx < len(all_lines[func_start-1:func_end]):
                    print(f"  第{line_no}行: {all_lines[line_no-1].rstrip()}")
    else:
        print("⚠️  没有新增行")
        print("\n可能的原因:")
        print("1. 函数节点未找到")
        print("2. AST 解析失败")
        print("3. 增强逻辑未触发")
        
except Exception as e:
    print(f"❌ AST 增强失败: {e}")
    import traceback
    traceback.print_exc()
