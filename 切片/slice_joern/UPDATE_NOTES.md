# slice_joern_ultra 更新说明

## 新增功能

根据 `recover.md` 文档中描述的 Mystique 主项目流程，我已经为 `slice_joern_ultra` 项目添加了以下模块：

### 1. 代码提取模块 (`code_extractor.py`) ✅

**功能**:
- 从切片节点集合提取源代码
- 支持占位符模式（在代码间隙插入占位符）
- 生成被省略代码块列表（用于恢复）

**主要函数**:
- `extract_code(slice_lines, source_lines, placeholder)` - 提取切片代码
- `reduced_hunks(slice_lines, source_lines, all_lines)` - 生成被省略的代码块
- `extract_code_with_mapping(...)` - 提取代码并返回占位符映射

### 2. AST 增强模块 (`ast_enhancer.py`) ✅

**功能**:
- 使用 tree-sitter 解析源代码 AST
- 补充完整的语法结构（if/for/while/switch 等）
- 确保切片代码语法正确

**主要类和函数**:
- `ASTEnhancer` 类 - AST 增强器
- `enhance_slice_with_ast(source_code, slice_lines, language)` - 便捷函数

**依赖**:
需要安装 tree-sitter：
```bash
pip install tree-sitter tree-sitter-c
```

### 3. 代码恢复模块 (`code_recoverer.py`) ✅

**功能**:
- 将带占位符的代码恢复为完整代码
- 支持批量恢复
- 适用于 LLM 生成的修复代码与原始代码合并

**主要函数**:
- `recover_placeholder(code_with_placeholder, slice_lines, source_lines, all_lines)` - 恢复单个代码
- `recover_batch(results, source_files)` - 批量恢复

### 4. 更新的主程序 (`single_file_slicer.py`) ✅

**新增步骤**:
- 第 8 步：AST 增强（可选）
- 第 9 步：代码提取（无占位符 + 带占位符）
- 第 10 步：构建包含源代码的结果

**新增输出字段**:
```json
{
    "sliced_code": "完整的切片源代码（无占位符）",
    "sliced_code_with_placeholder": "紧凑的切片代码（带占位符）",
    "enhanced_slice_lines": [1, 5, 6, 10, 32, 45],
    "metadata": {
        "original_slice_lines": 15,
        "enhanced_slice_lines": 18,
        "ast_enhanced": true
    }
}
```

## 工作流程对比

### 之前（仅切片行号）:
```
源代码 → Joern PDG → 切片引擎 → 行号列表
```

### 现在（完整源代码）:
```
源代码 → Joern PDG → 切片引擎 → 行号列表
                                    ↓
                              AST 增强（可选）
                                    ↓
                              代码提取
                                    ↓
                     切片源代码（完整 + 占位符版本）
```

## 使用示例

### 1. 基本切片（输出源代码）

```python
from single_file_slicer import SingleFileSlicer

slicer = SingleFileSlicer()
result = slicer.slice_one({
    'project_name_with_version': 'my_project-1.0',
    'file_path': 'src/main.c',
    'line_number': 42
})

print("切片代码:")
print(result['sliced_code'])

print("\n带占位符的切片代码:")
print(result['sliced_code_with_placeholder'])
```

### 2. 代码恢复（LLM 修复场景）

```python
from code_recoverer import recover_placeholder

# 假设 LLM 生成了修复后的代码（带占位符）
llm_fixed_code = """
int main() {
    int x = 10;
    /* <PLACEHOLDER> */
    x = x + 5;  // 修复：改为 +5
    /* <PLACEHOLDER> */
    return x;
}
"""

# 恢复为完整代码
full_code = recover_placeholder(
    code_with_placeholder=llm_fixed_code,
    slice_lines=result['slice_lines'],
    source_lines={i+1: line for i, line in enumerate(original_code.split('\n'))},
    all_lines=set(range(1, 100)),
    placeholder="/* <PLACEHOLDER> */"
)

print("完整的修复后代码:")
print(full_code)
```

### 3. 批量处理

```bash
python single_file_slicer.py
```

输出文件：
- `slice_output/slices.json` - 完整结果（包含源代码）
- `slice_output/slices_summary.json` - 摘要

## 配置选项

在 `config.py` 中：

```python
# AST 修复配置
ENABLE_AST_FIX = True  # 启用/禁用 AST 增强
LANGUAGE = "c"         # 语言类型

# 占位符
PLACEHOLDER = "    /* <PLACEHOLDER> */"
```

## 安装依赖

```bash
# 基本依赖
pip install networkx pygraphviz

# AST 增强依赖（可选，但强烈推荐）
pip install tree-sitter tree-sitter-c
```

## 输出对比

### 之前（仅行号）:
```json
{
    "slice_lines": [1, 5, 10, 32, 45],
    "metadata": {
        "total_slice_lines": 5
    }
}
```

### 现在（完整源代码）:
```json
{
    "slice_lines": [1, 5, 10, 32, 45],
    "enhanced_slice_lines": [1, 5, 6, 10, 32, 45, 50],
    "sliced_code": "int main() {\n    int x = 10;\n    ...",
    "sliced_code_with_placeholder": "int main() {\n    /* <PLACEHOLDER> */\n    int x = 10;\n    ...",
    "metadata": {
        "original_slice_lines": 5,
        "enhanced_slice_lines": 7,
        "ast_enhanced": true
    }
}
```

## 测试

运行测试脚本（需要先准备测试数据）：

```bash
# 准备测试数据
# 1. 在 slice_input/repository/ 下放置源代码
# 2. 在 slice_input/data.json 中定义切片任务

# 运行切片
python single_file_slicer.py

# 查看结果
cat slice_output/slices.json
```

## 下一步

建议的改进方向：

1. **完善 AST 增强**
   - 更精细的控制流分析
   - 支持更多 C/C++ 语法结构
   - 添加 Java 支持

2. **可视化**
   - 生成 HTML 报告，高亮显示切片代码
   - 可视化 PDG 子图

3. **性能优化**
   - 缓存 Joern 分析结果
   - 并行处理多个文件

4. **代码质量检查**
   - 验证切片代码可编译性
   - 语法错误检测

## 参考

- `recover.md` - 完整工作流程文档
- `ANALYSIS.md` - 项目分析文档
- Mystique 主项目 `src/project.py` - 核心实现参考
