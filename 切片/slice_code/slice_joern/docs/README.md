# Program Slicer for C/C++ Projects

这是一个基于 **Joern** 实时生成 PDG 的 C/C++ 程序切片工具，面向大规模静态分析告警的上下文提取场景（如为 LLM 提供漏洞分析所需的代码切片）。

## 功能特性

- ✅ **实时分析**：对每个源文件实时调用 Joern 生成 CPG/PDG，无需预生成
- ✅ **双向切片**：前向切片（DDG/CDG 向下追踪）+ 后向切片（DDG/CDG 向上追溯）
- ✅ **规则感知切片**：针对不同 rule_id（如 `cpp/use-after-free`、`cpp/nullptr-dereference` 等）使用专用切片策略和深度配置
- ✅ **AST 语法增强**：使用 Tree-sitter 补全 if/for/while 等控制结构的语法完整性
- ✅ **Def-Use 增强**：自动追踪警告行赋值变量的后续使用，补全上下文
- ✅ **空切片回退**：PDG 切片失败时依次尝试 AST 变量追踪切片 → 上下文窗口截取
- ✅ **函数调用提取**：自动提取切片中调用的用户自定义函数完整定义
- ✅ **多进程并行**：默认 5 个进程并行处理，大幅提升吞吐量
- ✅ **分块保存**：自动分 chunk 保存结果，避免内存溢出
- ✅ **断点续传**：支持中断后继续处理，基于任务 ID 去重，不会重复计算
- ✅ **进度跟踪**：实时保存进度文件，随时查看处理状态
- ✅ **LLM 专用输出**：自动生成精简版切片结果（含/不含 label），可直接用于模型训练

## 目录结构

```
slice_joern/
├── docs/
│   └── README.md                  # 本文件
├── single_file_slicer.py          # 主程序入口（含多进程调度、断点续传）
├── slice_engine.py                # 切片引擎：双向切片 + 规则感知策略
├── pdg_loader.py                  # PDG 加载与解析（DOT 格式）
├── ast_enhancer.py                # AST 增强：Tree-sitter 补全语法结构
├── code_extractor.py              # 代码提取：占位符、函数调用提取、AST 变量切片
├── function_extractor.py          # 函数定义提取（正则 + Tree-sitter 双模式）
├── treesitter_extractor.py        # 基于 Tree-sitter 的函数提取器
├── code_recoverer.py              # 占位符代码恢复（供 LLM 修复后还原用）
├── extract_by_id.py               # 按 ID 从 data copy.json 提取任务到 data.json
├── view_results.py                # 快速查看切片结果
├── show_progress.py               # 查看处理进度
├── config.py                      # 配置文件
├── requirements.txt               # Python 依赖
├── slice_input/                   # 输入数据目录
│   ├── data.json                 # 当前切片任务列表
│   ├── data copy.json            # 完整任务备份（用于按 ID 提取子集）
│   └── repository/               # 源代码仓库（按 project_name_with_version 组织）
└── slice_output/                  # 输出结果目录
    ├── slices_chunk_XXXX.json    # 分块切片结果
    ├── checkpoint.json           # 断点文件
    ├── progress.json             # 进度文件
    ├── slices.json               # 合并后的完整结果
    ├── slices_summary.json       # 摘要文件
    ├── slices_for_llm.json       # LLM 用精简版（不含 label）
    └── slices_for_llm_with_label.json  # LLM 用精简版（含 label）
```

## 环境要求

- Python 3.10+
- [Joern](https://joern.io/) 已安装，默认路径 `/opt/joern-cli`（含 `joern-parse` 和 `joern-export`）
- Graphviz（`pygraphviz` 依赖）
- conda 虚拟环境（推荐 `slice`）

## 安装

### 1. 激活虚拟环境

```bash
conda activate slice
```

### 2. 安装 Python 依赖

```bash
cd slice_joern
pip install -r requirements.txt
```

依赖列表：
| 包 | 用途 |
|---|---|
| `networkx` | PDG 图操作 |
| `pygraphviz` | 读取 Joern 导出的 DOT 文件 |
| `tree-sitter` | AST 解析与语法增强 |
| `tree-sitter-c` | C 语言语法支持 |

### 3. 准备输入数据

**任务文件** `slice_input/data.json` 格式（JSON 数组）：

```json
[
  {
    "id": 1,
    "tool_name": "codeql",
    "project_name_with_version": "vim-9.1.1896",
    "project_version": "9.1.1896",
    "file_path": "src/memfile.c",
    "line_number": 256,
    "rule_id": "cpp/use-after-free",
    "message": "...",
    "label": 1
  }
]
```

**源码仓库** 按 `project_name_with_version` 组织，放置于 `slice_input/repository/` 下：

```
slice_input/repository/
└── vim-9.1.1896/
    └── src/
        └── memfile.c
```

## 使用方法

### 基本运行

```bash
# 多进程并行执行切片（默认 5 进程）
python single_file_slicer.py

# 查看当前进度
python single_file_slicer.py --progress

# 清除断点，从头重新处理
python single_file_slicer.py --clear

# 自定义 chunk 大小（默认 100）
python single_file_slicer.py --chunk-size 200

# 自定义进程数
python single_file_slicer.py --processes 8

# 禁用多进程（单进程，便于调试）
python single_file_slicer.py --no-multiprocess
```

### 按 ID 提取子集任务

```bash
# 从 data copy.json 提取指定 ID 的任务写入 data.json
python extract_by_id.py 1 2 3
python extract_by_id.py 1-100
python extract_by_id.py 1 5 10-20 23
```

### 查看切片结果

```bash
python view_results.py
```

### 后台运行（推荐用于大规模任务）

```bash
# nohup 后台运行
nohup python single_file_slicer.py > slice.log 2>&1 &

# 查看日志
tail -f slice.log

# screen 方式（支持重新连接）
screen -S slicing
python single_file_slicer.py
# Ctrl+A+D 退出，screen -r slicing 重新连接
```

## 配置说明

在 `config.py` 中可以调整所有参数：

### 切片深度

| 参数 | 默认值 | 说明 |
|---|---|---|
| `BACKWARD_DEPTH` | `10` | 后向切片深度（沿 DDG/CDG 向上追溯） |
| `FORWARD_DEPTH` | `10` | 前向切片深度（沿 DDG/CDG 向下追踪） |
| `RULE_SLICE_DEPTH_OVERRIDES` | 见下表 | 按 rule_id 覆盖切片深度 |

各规则默认深度覆盖：

| rule_id | backward | forward |
|---|---|---|
| `cpp/inconsistent-null-check` | 3 | 5 |
| `cpp/nullptr-dereference` | 3 | 5 |
| `cpp/use-after-free` | 5 | 8 |
| `cpp/overflow-buffer` | 5 | 5 |
| `cpp/integer-overflow-tainted` | 5 | 5 |

### AST 与增强

| 参数 | 默认值 | 说明 |
|---|---|---|
| `ENABLE_AST_FIX` | `True` | 是否启用 AST 语法修复 |
| `ENABLE_DEF_USE_AUGMENTATION` | `True` | 是否启用 Def-Use 增强 |
| `LANGUAGE` | `"c"` | 源码语言 |

### 空切片回退

| 参数 | 默认值 | 说明 |
|---|---|---|
| `EMPTY_SLICE_FALLBACK` | `True` | 空切片时启用回退策略 |
| `CONTEXT_SIZE` | `50` | 上下文截取窗口大小（前后各 N 行） |

### 函数调用提取

| 参数 | 默认值 | 说明 |
|---|---|---|
| `EXTRACT_FUNCTION_CALLS` | `True` | 是否提取被调函数定义 |
| `INCLUDE_STDLIB_FUNCTIONS` | `False` | 是否包含标准库函数 |
| `MAX_FUNCTION_DEFINITIONS` | `10` | 最多提取函数定义数量 |

### 并行与断点

| 参数 | 默认值 | 说明 |
|---|---|---|
| `NUM_PROCESSES` | `5` | 并行进程数 |
| `ENABLE_MULTIPROCESSING` | `True` | 是否启用多进程 |
| `CHUNK_SIZE` | `100` | 每个 chunk 保存的任务数 |
| `ENABLE_CHECKPOINT` | `True` | 是否启用断点续传 |

## 断点续传与分块保存

### 工作原理

- 任务完成后（无论成功或失败）立即写入 `checkpoint.json`，使用**任务 ID** 去重（而非索引）
- 每处理 `CHUNK_SIZE` 个任务保存一个 chunk 文件
- 中断后重新运行自动跳过已完成的任务
- 处理过程中的崩溃只会导致**当前任务**重新处理

### 多进程并行

- 使用 `multiprocessing.Pool` + `imap_unordered`，任务完成即收集结果
- 各进程独立处理，互不干扰；主进程负责写入 checkpoint 和 chunk
- 支持 Ctrl+C 中断后继续（已完成任务不会重复）

### 性能参考

| 配置 | 单任务耗时 | 5万任务总耗时 | 加速比 |
|------|-----------|--------------|--------|
| 单进程 | ~10s | ~140h | 1x |
| 3 进程 | ~10s | ~47h | 3x |
| 5 进程 | ~10s | ~28h | 5x |

> 实际速度取决于 CPU 核心数、磁盘 I/O 和 Joern 分析耗时。

## 输出文件说明

```
slice_output/
├── slices_chunk_0001.json              # 第 1 个 chunk（100 条结果）
├── slices_chunk_0001_summary.json      # chunk 摘要
├── ...
├── checkpoint.json                     # 断点文件（processed_ids 列表）
├── progress.json                       # 进度文件（当前状态快照）
├── slices.json                         # 合并后的完整结果（按 ID 排序）
├── slices_summary.json                 # 摘要（不含 sliced_code）
├── slices_for_llm.json                 # LLM 用精简版（不含 label）
└── slices_for_llm_with_label.json      # LLM 用精简版（含 label）
```

**各文件字段说明：**

| 文件 | 包含字段 |
|---|---|
| `slices.json` | 完整字段：输入字段 + `function_name`、`sliced_code`、`complete_code`、`slice_lines`、`enhanced_slice_lines`、`called_functions`、`function_definitions`、`metadata` |
| `slices_summary.json` | id、project、file、line、status、function_name、slice_lines_count、metadata |
| `slices_for_llm.json` | id、tool_name、project_name_with_version、project_version、line_number、function_name、rule_id、message、sliced_code |
| `slices_for_llm_with_label.json` | 同上 + label |

**注意事项：**
- `checkpoint.json` 使用 `processed_ids` 记录已完成的任务 ID
- `progress.json` 使用 `current_id` 记录当前正在处理的任务 ID
- 合并时自动按 ID 升序排序，chunk 文件合并完成后自动删除

## 算法原理

### 切片流程

```
源文件
  │
  ├─ Joern 分析 ──► CPG / PDG / CFG（DOT 格式）
  │
  ├─ PDG 预处理 ──► 合并 CFG 边，清理空 DDG 边
  │
  ├─ 定位目标节点 ──► 精确行匹配 → 邻近节点匹配 → 宽松匹配
  │
  ├─ 双向切片 ────► 后向（DDG/CDG 向上）+ 前向（DDG/CDG 向下）
  │    └─ 规则感知 ──► 按 rule_id 选择专用策略
  │
  ├─ AST 增强 ────► 补全 if/for/while/switch 结构的完整括号
  │    └─ Def-Use 增强 ──► 追踪赋值变量的后续使用
  │
  ├─ 空切片回退 ──► AST 变量追踪切片 → 上下文窗口截取
  │
  └─ 代码提取 ────► 含占位符的切片代码 + 被调函数定义
```

### 规则感知切片策略

| 规则类型 | 策略说明 |
|---|---|
| `cpp/use-after-free` | 提取完整左值路径（如 `s->s3.alpn_selected`），文本扫描所有 free/alloc/赋值操作 |
| `cpp/unbounded-write` / `cpp/overflow-buffer` | 扫描含 size/len/count 等关键词的变量，补全边界相关节点 |
| `cpp/inconsistent-null-check` / `cpp/nullptr-dereference` | 提取赋值左值，前向切片不过滤标识符，文本扫描所有使用节点 |
| 其他规则 | 通用双向切片 + Def-Use 增强 |

### PDG 节点查找策略

1. **精确范围匹配**：PDG 的 METHOD 节点行范围 `[start_line, end_line]` 包含目标行
2. **节点精确命中**：PDG 中存在行号等于目标行的节点
3. **宽松匹配**：选择目标行 ±200 行内节点最多的 PDG（处理宏展开等场景）

## 示例输出

`slices.json` 单条结果示例：

```json
{
    "id": 42,
    "tool_name": "codeql",
    "project_name_with_version": "vim-9.1.1896",
    "file_path": "src/memfile.c",
    "line_number": 256,
    "rule_id": "cpp/use-after-free",
    "message": "Potential use after free",
    "label": 1,
    "status": "success",
    "function_name": "mf_close",
    "function_start_line": 230,
    "function_end_line": 290,
    "sliced_code": "/* 主切片代码（含占位符） */",
    "complete_code": "/* 主切片代码 + 被调函数定义 */",
    "slice_lines": [231, 240, 250, 256, 260],
    "enhanced_slice_lines": [231, 238, 240, 248, 250, 254, 256, 258, 260],
    "called_functions": ["mf_hash_free", "mf_buf_free"],
    "function_definitions": {
        "mf_hash_free": "void mf_hash_free(...) { ... }"
    },
    "metadata": {
        "backward_nodes": 12,
        "forward_nodes": 5,
        "original_slice_lines": 5,
        "enhanced_slice_lines": 9,
        "ast_enhanced": true,
        "slice_type": "pdg_slice",
        "called_functions_count": 2,
        "extracted_functions_count": 2
    }
}
```

## 常见问题

**Q：Joern 超时怎么办？**  
A：默认超时 60 秒。对于特别大的文件，可在 `single_file_slicer.py` 的 `JoernAnalyzer.analyze_file` 中调整 `timeout` 参数。

**Q：切片结果为空（slice_type = context_extraction）？**  
A：说明 PDG 切片和 AST 变量切片均失败，已自动回退到上下文窗口截取（前后各 `CONTEXT_SIZE` 行）。可检查 Joern 是否成功生成了 PDG。

**Q：如何只处理部分任务进行测试？**  
A：使用 `extract_by_id.py` 提取少量任务到 `data.json`，然后运行单进程模式：
```bash
python extract_by_id.py 1-10
python single_file_slicer.py --no-multiprocess
```

**Q：如何保留 chunk 文件不自动删除？**  
A：在代码中将 `merge_chunks()` 改为 `merge_chunks(delete_chunks=False)`。
