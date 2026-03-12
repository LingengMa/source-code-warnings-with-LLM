# slice_joern_ultra 更新说明

## 2026-03-01 更新：PDG 切片失败场景优化（语义切片回退）

### 问题背景

对于某些特殊文件（如含大量宏展开/内联汇编的 `snowdsp.c`），Joern 会将函数解析为 `<global>` 作用域，导致：
1. `METHOD` 节点的 `LINE_NUMBER_END` 无法覆盖目标行
2. `_find_pdg_for_line` 找不到对应的 PDG
3. `SliceEngine` 得到空节点集
4. 最终回退到「前后50行上下文截取」—— 包含大量无关代码，缺少关键变量定义和函数上下文

### 改动内容

#### `pdg_loader.py` — PDG 类新增方法

- `has_node_at_line(target_line)`: 检查 PDG 中是否存在精确位于目标行的节点
- `count_nodes_near_line(target_line, radius=200)`: 统计目标行附近节点数，用于宽松匹配打分

#### `single_file_slicer.py` — 三段策略 PDG 查找

`_find_pdg_for_line` 和 `process_single_task` 中的 PDG 查找均升级为三段策略：
1. **精确范围匹配**：`METHOD.start_line ≤ target_line ≤ METHOD.end_line`（原有逻辑）
2. **节点精确命中**：PDG 中存在行号 == target_line 的节点
3. **宽松邻近匹配**：选取目标行 ±200 行内节点最多的 PDG（适用于 `<global>` 场景）

#### `slice_engine.py` — 切片准则节点容错

`SliceEngine.slice` 在目标行找不到节点时，自动在 ±3 行范围内搜索邻近节点作为切片准则，
适应 Joern 对宏展开行的行号偏移场景。

#### `code_extractor.py` — 新增 `ast_variable_slice` 函数

当 PDG 切片仍然为空时（如 PDG 结构与目标行完全无关），使用 tree-sitter 做
**基于变量使用的语义切片**：

1. 解析函数代码的 AST，提取警告行上所有标识符（变量名）作为种子
2. 迭代扩展：函数范围内所有「定义或使用了这些变量」的语句行均纳入切片
3. 多轮传播（默认3轮），直到集合稳定
4. 用 `ASTEnhancer` 补全语法括号，保证语法完整性

#### `single_file_slicer.py` — 空切片回退策略升级

原来：直接截取前后 N 行上下文

现在：优先级从高到低：
1. **PDG 切片**（正常路径）
2. **AST 变量追踪切片**（PDG 为空时）：`slice_type = "ast_variable_slice"`
3. **上下文截取**（AST 切片也失败时兜底）：`slice_type = "context_extraction"`

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
