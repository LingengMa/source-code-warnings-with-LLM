#!/usr/bin/env python3
"""测试 tree-sitter API"""

import tree_sitter
import tree_sitter_c as tsc

print("=== tree_sitter 模块 ===")
print([x for x in dir(tree_sitter) if not x.startswith('_')])

print("\n=== tree_sitter_c 模块 ===")
print([x for x in dir(tsc) if not x.startswith('_')])

# 尝试直接使用 Parser
print("\n=== 测试方法1: Parser() ===")
try:
    parser = tree_sitter.Parser()
    print("✅ Parser 创建成功")
    print("Parser 方法:", [x for x in dir(parser) if not x.startswith('_')])
except Exception as e:
    print(f"❌ Parser 创建失败: {e}")

# 尝试设置语言
print("\n=== 测试方法2: set_language ===")
try:
    parser = tree_sitter.Parser()
    # 直接传入 capsule
    parser.set_language(tsc.language())
    print("✅ set_language 成功")
    
    code = b"int main() { return 0; }"
    tree = parser.parse(code)
    print(f"✅ 解析成功: {tree.root_node.type}")
    for child in tree.root_node.children:
        print(f"  - {child.type}: {child.start_point} - {child.end_point}")
except Exception as e:
    print(f"❌ 失败: {e}")
    import traceback
    traceback.print_exc()
