"""
测试脚本：验证代码提取和恢复功能
"""
import json
from code_extractor import extract_code, reduced_hunks
from code_recoverer import recover_placeholder


def test_code_extraction():
    """测试代码提取功能"""
    print("=" * 60)
    print("测试 1: 代码提取")
    print("=" * 60)
    
    # 模拟源代码
    source_lines = {
        1: "int main() {",
        2: "    int x = 0;",
        3: "    int y = 0;",
        4: "    // 一些中间代码",
        5: "    for (int i = 0; i < 10; i++) {",
        6: "        x += i;",
        7: "        y += i * 2;",
        8: "    }",
        9: "    printf(\"%d\\n\", x);",
        10: "    return 0;",
        11: "}"
    }
    
    # 切片行（只包含关键行）
    slice_lines = {1, 2, 6, 9, 10, 11}
    
    # 无占位符提取
    code = extract_code(slice_lines, source_lines, placeholder=None)
    print("\n无占位符版本:")
    print(code)
    
    # 带占位符提取
    code_with_ph = extract_code(slice_lines, source_lines, 
                               placeholder="    /* <PLACEHOLDER> */")
    print("\n带占位符版本:")
    print(code_with_ph)
    
    return code_with_ph, slice_lines, source_lines


def test_code_recovery():
    """测试代码恢复功能"""
    print("\n" + "=" * 60)
    print("测试 2: 代码恢复")
    print("=" * 60)
    
    code_with_ph, slice_lines, source_lines = test_code_extraction()
    
    # 模拟 LLM 修改了代码
    modified_code = code_with_ph.replace("int x = 0;", "int x = 10;  // LLM 修复")
    
    print("\nLLM 修改后的代码:")
    print(modified_code)
    
    # 恢复为完整代码
    all_lines = set(range(1, 12))
    recovered = recover_placeholder(
        code_with_placeholder=modified_code,
        slice_lines=slice_lines,
        source_lines=source_lines,
        all_lines=all_lines,
        placeholder="    /* <PLACEHOLDER> */"
    )
    
    if recovered:
        print("\n恢复后的完整代码:")
        print(recovered)
    else:
        print("\n恢复失败!")


def test_reduced_hunks():
    """测试 reduced_hunks 功能"""
    print("\n" + "=" * 60)
    print("测试 3: Reduced Hunks")
    print("=" * 60)
    
    source_lines = {
        1: "int main() {",
        2: "    int x = 0;",
        3: "    int y = 0;",
        4: "    // 一些中间代码",
        5: "    for (int i = 0; i < 10; i++) {",
        6: "        x += i;",
        7: "        y += i * 2;",
        8: "    }",
        9: "    printf(\"%d\\n\", x);",
        10: "    return 0;",
        11: "}"
    }
    
    slice_lines = {1, 2, 6, 9, 10, 11}
    all_lines = set(range(1, 12))
    
    hunks = reduced_hunks(slice_lines, source_lines, all_lines)
    
    print(f"\n找到 {len(hunks)} 个被省略的代码块:")
    for i, hunk in enumerate(hunks, 1):
        print(f"\n代码块 {i}:")
        print(hunk)


def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("slice_joern_ultra 功能测试")
    print("=" * 60 + "\n")
    
    try:
        # 测试 1: 代码提取
        test_code_extraction()
        
        # 测试 2: 代码恢复
        test_code_recovery()
        
        # 测试 3: Reduced Hunks
        test_reduced_hunks()
        
        print("\n" + "=" * 60)
        print("✓ 所有测试完成!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
