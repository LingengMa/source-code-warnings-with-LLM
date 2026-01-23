#!/usr/bin/env python3
"""测试修复后的 AST 增强器"""

from ast_enhancer import ASTEnhancer, TREE_SITTER_AVAILABLE

print(f"tree-sitter 可用: {TREE_SITTER_AVAILABLE}")

if not TREE_SITTER_AVAILABLE:
    print("❌ tree-sitter 不可用")
    exit(1)

# 测试代码
test_code = """static int var_diamond_search(MpegEncContext * s, int *best, int dmin,
                               int src_index, int ref_index, int size,
                               int h, int ref_h, int flags)
{
    MotionEstContext * const c= &s->me;
    me_cmp_func cmpf, chroma_cmpf;
    LOAD_COMMON
    LOAD_COMMON2
    int map_generation= c->map_generation;
    int x, y, d;
    int dia_size;
    
    for(dia_size=1; dia_size<=c->dia_size; dia_size++){
        int dir;
        const int x= best[0];
        const int y= best[1];
        int start, end;
        
        start= FFMAX(0, y + dia_size - ymax);
        end  = FFMIN(dia_size, xmax - x + 1);
        for(dir= start; dir<end; dir++){
            int y2= y + dia_size - dir;
            CHECK_MV(x + dir           , y + dia_size - dir);
        }
        
        if(x!=best[0] || y!=best[1])
            dia_size=0;
    }
    return dmin;
}"""

# 切片行号（模拟实际切片结果）
slice_lines = {
    1,   # 函数签名第1行
    5,   # MotionEstContext
    8,   # LOAD_COMMON2
    9,   # map_generation
    12,  # for 循环开始
    14,  # const int x
    15,  # const int y
    17,  # start=
    18,  # end=
    19,  # for(dir=
    21,  # CHECK_MV
    24,  # if(x!=best[0]
    25,  # dia_size=0
    27,  # return dmin
}

print(f"\n原始切片行数: {len(slice_lines)}")
print(f"原始切片行: {sorted(slice_lines)}")

# 测试 AST 增强
try:
    enhancer = ASTEnhancer("c")
    print("\n✅ ASTEnhancer 初始化成功")
    
    enhanced_lines = enhancer.enhance_slice(
        source_code=test_code,
        slice_lines=slice_lines,
        function_start_line=1
    )
    
    print(f"\n增强后行数: {len(enhanced_lines)}")
    print(f"增强后行: {sorted(enhanced_lines)}")
    print(f"新增行数: {len(enhanced_lines) - len(slice_lines)}")
    
    # 显示新增的行
    new_lines = enhanced_lines - slice_lines
    if new_lines:
        print(f"\n新增的行: {sorted(new_lines)}")
        lines = test_code.split('\n')
        for line_no in sorted(new_lines):
            if 1 <= line_no <= len(lines):
                print(f"  第{line_no}行: {lines[line_no-1]}")
    else:
        print("\n⚠️ 没有新增行，AST 增强可能未生效")
        
except Exception as e:
    print(f"\n❌ AST 增强失败: {e}")
    import traceback
    traceback.print_exc()
