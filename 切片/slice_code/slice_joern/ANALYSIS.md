# slice_joern_ultra 项目分析与改进方案

## 当前状态分析

### 已实现的功能

1. **PDG 加载** (`pdg_loader.py`)
   - ✅ 从 Joern 生成的 `.dot` 文件加载 PDG
   - ✅ 解析节点属性（LINE_NUMBER, CODE, NODE_TYPE 等）
   - ✅ 获取节点的前驱/后继关系

2. **切片引擎** (`slice_engine.py`)
   - ✅ 基于 PDG 的双向切片（backward + forward）
   - ✅ 沿 DDG/CDG 边遍历依赖关系
   - ✅ 深度控制和标识符过滤
   - ✅ 返回切片节点集合和元数据

3. **Joern 集成** (`single_file_slicer.py`)
   - ✅ 调用 Joern 实时分析单个文件
   - ✅ 生成 PDG/CFG/CPG
   - ✅ PDG 预处理（合并 CFG，清理边）

### 缺失的功能 ⚠️

根据 `recover.md` 文档的分析，项目目前**只输出了切片行号集合**，但**没有实现从节点到源代码的转换**。具体缺失：

1. **代码提取功能**
   - ❌ 从 PDG 节点提取代码片段
   - ❌ 按行号组合生成切片代码
   - ❌ 占位符机制（省略不相关代码）

2. **AST 增强**
   - ❌ 补充语法结构（if/for/while/try-catch 等）
   - ❌ 添加控制流关键语句（break/return/goto）
   - ❌ 修剪不必要的语法节点

3. **代码恢复功能**
   - ❌ 占位符到完整代码的恢复
   - ❌ 与原始代码的其余部分合并

4. **输出格式**
   - ❌ 只有行号列表，没有实际的切片源代码
   - ❌ 无法直接展示给用户

## 改进方案

参考 Mystique 主项目的实现（`src/project.py`），需要添加以下模块：

### 1. 代码提取模块 (`code_extractor.py`)

**功能**:
- 从切片节点集合提取源代码
- 实现 `code_by_lines()` 方法
- 支持占位符机制

**核心逻辑**:
```python
def extract_code(pdg: PDG, slice_lines: Set[int], 
                source_lines: Dict[int, str], 
                placeholder: Optional[str] = None) -> str:
    """
    从切片行号集合生成源代码
    
    Args:
        pdg: PDG 对象
        slice_lines: 切片包含的行号集合
        source_lines: 原始源代码行字典 {行号: 代码}
        placeholder: 占位符字符串（可选）
    
    Returns:
        切片代码字符串
    """
    # 1. 按行号排序
    sorted_lines = sorted(slice_lines)
    
    # 2. 组合代码
    if not placeholder:
        # 无占位符模式：直接拼接
        return "\n".join([source_lines[line] for line in sorted_lines])
    else:
        # 占位符模式：间隔处插入占位符
        code = ""
        last_line = 0
        for line in sorted_lines:
            if line - last_line > 1:
                # 检查是否需要插入占位符
                if not is_trivial_gap(source_lines, last_line + 1, line - 1):
                    code += placeholder + "\n"
            code += source_lines[line] + "\n"
            last_line = line
        return code
```

### 2. AST 增强模块 (`ast_enhancer.py`)

**功能**:
- 使用 tree-sitter 解析源代码的 AST
- 补充完整的语法结构
- 确保切片代码语法正确

**核心方法**:
```python
def ast_dive_c(root_node, slice_lines: Set[int]) -> Set[int]:
    """
    深入 AST，补充必要的语法结构
    
    处理：
    - if 语句：补充条件和分支的起止行
    - for/while 循环：补充循环头和循环体
    - switch-case：补充 case 标签和 break
    """
    pass

def ast_add(root_node, slice_lines: Set[int]) -> Set[int]:
    """
    添加控制流关键语句
    
    - 如果切片包含 if body，则添加对应的 break/return
    - 如果切片包含 goto，则添加对应的 label
    """
    pass

def ast_trim(root_node, slice_lines: Set[int]) -> Set[int]:
    """
    修剪不必要的节点
    
    - 移除空的 if 语句（consequence 为空）
    """
    pass
```

### 3. 代码恢复模块 (`code_recoverer.py`)

**功能**:
- 将带占位符的代码恢复为完整代码
- 用于 LLM 生成的修复代码与原始代码合并

**核心逻辑**:
```python
def recover_placeholder(code_with_placeholder: str, 
                       slice_lines: Set[int],
                       source_lines: Dict[int, str],
                       placeholder: str) -> str:
    """
    将带占位符的代码恢复为完整代码
    
    Args:
        code_with_placeholder: 带占位符的代码
        slice_lines: 切片行号集合
        source_lines: 原始代码行字典
        placeholder: 占位符字符串
    
    Returns:
        完整代码
    """
    # 1. 生成被省略的代码块
    placeholder_hunks = reduced_hunks(slice_lines, source_lines)
    
    # 2. 替换占位符
    result = ""
    for line in code_with_placeholder.split("\n"):
        if line.strip() == placeholder.strip():
            result += placeholder_hunks.pop(0)
        else:
            result += line + "\n"
    return result
```

### 4. 更新 `single_file_slicer.py`

在 `slice_one()` 方法的第 7 步后，添加代码提取和 AST 增强：

```python
# 7. 提取切片行号（已有）
slice_lines = {...}

# 8. AST 增强（新增）
from ast_enhancer import enhance_slice_with_ast
enhanced_lines = enhance_slice_with_ast(
    source_code="\n".join(code_lines),
    slice_lines=slice_lines,
    language="c"
)

# 9. 提取切片代码（新增）
from code_extractor import extract_code
sliced_code = extract_code(
    pdg=pdg,
    slice_lines=enhanced_lines,
    source_lines={i+1: line for i, line in enumerate(code_lines)},
    placeholder=None  # 不使用占位符
)

sliced_code_with_placeholder = extract_code(
    pdg=pdg,
    slice_lines=enhanced_lines,
    source_lines={i+1: line for i, line in enumerate(code_lines)},
    placeholder=config.PLACEHOLDER
)

# 10. 更新结果（新增）
result["sliced_code"] = sliced_code
result["sliced_code_with_placeholder"] = sliced_code_with_placeholder
result["enhanced_slice_lines"] = sorted(list(enhanced_lines))
```

## 实施步骤

1. ✅ **第一步**: 创建 `code_extractor.py` 模块
   - 实现基本的代码提取功能
   - 支持占位符模式

2. ✅ **第二步**: 创建 `ast_enhancer.py` 模块  
   - 集成 tree-sitter
   - 实现 `ast_dive_c()`, `ast_add()`, `ast_trim()`

3. ✅ **第三步**: 创建 `code_recoverer.py` 模块
   - 实现占位符恢复功能

4. ✅ **第四步**: 更新 `single_file_slicer.py`
   - 集成新模块
   - 在切片后添加代码提取步骤

5. ✅ **第五步**: 更新 `config.py`
   - 添加 tree-sitter 配置
   - 添加占位符配置

6. ✅ **第六步**: 测试和验证
   - 对示例文件进行切片
   - 验证输出的源代码语法正确性
   - 验证占位符恢复功能

## 预期效果

实施后，`slice_joern_ultra` 将能够：

1. **输出完整的切片源代码**，而不仅仅是行号列表
2. **保证输出代码语法正确**，可以直接编译或展示
3. **支持占位符模式**，减少不必要的上下文
4. **支持代码恢复**，方便与 LLM 生成的代码合并

最终输出示例：
```json
{
    "project": "vim-9.1.1896",
    "file": "src/uninstall.c",
    "line": 32,
    "function": "main",
    "sliced_code": "完整的可编译的切片代码...",
    "sliced_code_with_placeholder": "带占位符的紧凑版本...",
    "slice_lines": [1, 5, 10, 32, 45],
    "enhanced_slice_lines": [1, 5, 6, 10, 32, 45, 50],
    "metadata": {...}
}
```
