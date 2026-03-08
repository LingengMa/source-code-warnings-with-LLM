# C/C++ 代码切片与函数依赖分析工具

基于 **tree-sitter** 的高性能 C/C++ 代码切片工具，采用「先全量索引建图，再批量查询」的两阶段模式，可对大规模代码仓库中的缺陷位置进行函数级切片，并自动提取多层函数调用依赖关系。

---

## 目录

- [功能特性](#功能特性)
- [工作原理](#工作原理)
- [项目结构](#项目结构)
- [环境要求](#环境要求)
- [快速开始](#快速开始)
- [输入格式](#输入格式)
- [输出格式](#输出格式)
- [高级用法](#高级用法)
- [性能调优](#性能调优)
- [故障排除](#故障排除)

---

## 功能特性

- 🔍 **精准的 AST 解析**：使用 tree-sitter 解析 C/C++ 语法树，精确提取函数定义与调用关系
- ⚡ **高性能两阶段模式**：一次性构建全量索引，后续批量查询无需重复解析
- 💾 **智能增量缓存**：基于文件修改时间的签名比对，项目未变化时直接加载缓存
- 📊 **多层依赖分析**：BFS 广度优先遍历，默认提取 3 层函数调用依赖
- 🗂️ **批量处理 + 断点保护**：每处理 1000 条自动保存，中断后不丢失已有结果
- 🌐 **多语言兼容输出**：全英文字段名的 JSON 输出，便于下游程序化处理

---

## 工作原理

```
输入数据 (data.json)          代码仓库 (repository/)
       │                              │
       │              ┌───────────────▼───────────────┐
       │              │   阶段 1: 构建全量索引          │
       │              │   tree-sitter 解析所有 .c/.h   │
       │              │   提取函数定义 + 调用关系       │
       │              │   构建 function_index 内存图   │
       │              │   结果序列化缓存到 .cache/     │
       │              └───────────────┬───────────────┘
       │                              │
       └──────────────┐               │ (内存索引)
                      ▼               ▼
              ┌───────────────────────────────────┐
              │   阶段 2: 批量查询处理              │
              │   按 file_path + line_number 定位  │
              │   目标函数，BFS 扩展 3 层依赖        │
              │   每 1000 条写出一个批次文件         │
              └───────────────┬───────────────────┘
                              │
              ┌───────────────▼───────────────┐
              │   阶段 3: 合并结果             │
              │   汇总所有批次 → final_results  │
              └───────────────────────────────┘
```

---

## 项目结构

```
slice_dependency/
├── slice_analyzer.py      # 核心模块：CProjectIndexer + SliceAnalyzer
├── cache_manager.py       # 增量缓存管理（IndexCache）
├── run.py                 # 交互式运行入口，带进度监控
├── demo.py                # 演示脚本，快速体验核心功能
├── test_tool.py           # 功能测试脚本
├── test_output_format.py  # 输出格式验证脚本
├── requirements.txt       # Python 依赖
├── USAGE.md               # 详细使用指南
├── OUTPUT_FORMAT.md       # 输出格式规范
├── input/
│   ├── data.json          # 待分析条目（缺陷数据）
│   └── repository/        # 各项目源代码目录
│       ├── ffmpeg-6.1.1/
│       ├── redis-8.0.2/
│       └── ...
├── output/                # 输出目录（自动创建）
│   ├── final_results.json     # 最终合并结果
│   └── failed_entries.json    # 处理失败的条目
└── .cache/                # 索引缓存（自动管理）
    ├── function_index.pkl
    └── index_meta.json
```

---

## 环境要求

- Python >= 3.8
- tree-sitter >= 0.20.0
- tree-sitter-c >= 0.20.0

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 准备输入数据

将代码仓库放入 `input/repository/`，将缺陷数据放入 `input/data.json`（格式见[输入格式](#输入格式)）。

### 3. 运行分析

**推荐方式（交互式，带进度输出）：**

```bash
python run.py
```

**直接运行主程序：**

```bash
python slice_analyzer.py
```

**演示模式（快速体验，无需完整数据）：**

```bash
python demo.py
```

**Python API 方式：**

```python
from slice_analyzer import SliceAnalyzer

analyzer = SliceAnalyzer('input', 'output')
analyzer.build_index()           # 阶段1：构建索引
analyzer.process_entries()       # 阶段2：批量处理
analyzer.merge_results()         # 阶段3：合并结果
```

---

## 输入格式

### `input/data.json`

JSON 数组，每个元素描述一处待分析的缺陷位置：

```json
[
  {
    "tool_name": "codeql",
    "project_name": "ffmpeg",
    "project_name_with_version": "ffmpeg-6.1.1",
    "project_version": "6.1.1",
    "file_path": "libavcodec/motion_est_template.c",
    "line_number": 785
  },
  ...
]
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `tool_name` | string | 静态分析工具名称（如 codeql、infer） |
| `project_name` | string | 项目简称（不含版本） |
| `project_name_with_version` | string | 完整项目名（含版本，须与 repository/ 下目录名一致） |
| `project_version` | string | 版本号 |
| `file_path` | string | 缺陷文件相对路径 |
| `line_number` | integer | 缺陷行号（1-based） |

### `input/repository/`

每个子目录为一个独立的 C/C++ 项目，目录名需与 `project_name_with_version` 字段一致：

```
repository/
├── ffmpeg-6.1.1/
│   ├── libavcodec/
│   └── ...
└── redis-8.0.2/
    ├── src/
    └── ...
```

---

## 输出格式

### `output/final_results.json`

JSON 数组，包含所有成功分析的结果：

```json
[
  {
    "tool_name": "codeql",
    "project_simple_name": "ffmpeg",
    "project_name": "ffmpeg-6.1.1",
    "project_version": "6.1.1",
    "defect_file": "libavcodec/motion_est_template.c",
    "defect_line": 785,
    "target_function": {
      "function_name": "sad_hpel_motion_search",
      "start_line": 780,
      "end_line": 850,
      "source_code": "static int sad_hpel_motion_search(...) { ... }",
      "called_functions": ["sad", "cmp", "get_mb_score"]
    },
    "dependency_analysis": [
      {
        "level": 1,
        "functions": [
          {
            "function_name": "sad",
            "file_path": "/abs/path/to/dsputil.c",
            "start_line": 100,
            "end_line": 120,
            "source_code": "static int sad(...) { ... }",
            "called_functions": ["pix_abs"]
          }
        ]
      },
      { "level": 2, "functions": [ ... ] },
      { "level": 3, "functions": [ ... ] }
    ]
  }
]
```

`dependency_analysis` 按 BFS 层级排列，`level: 1` 为目标函数直接调用的函数，`level: 2` 为第二层，以此类推（默认最多 3 层）。

### `output/failed_entries.json`

记录无法处理的条目及失败原因：

```json
[
  {
    "tool_name": "codeql",
    "project_name_with_version": "ffmpeg-6.1.1",
    "file_path": "unknown_file.c",
    "line_number": 100,
    "reason": "function_not_found"
  }
]
```

| 失败原因 | 说明 |
|---------|------|
| `function_not_found` | 指定行号未在任何函数定义范围内 |
| `file_not_found` | 文件在仓库中不存在 |
| `parse_error` | 文件解析失败 |
| 其他字符串 | 运行时异常消息 |

---

## 高级用法

### 调整依赖深度

```python
# 修改 slice_analyzer.py 中 _process_single_entry 方法
dep_layers = self.indexer.get_dependencies(
    project_name, target_func.name, depth=5  # 默认 3，按需调整
)
```

### 只索引特定项目

```python
from slice_analyzer import CProjectIndexer, SliceAnalyzer

analyzer = SliceAnalyzer('input', 'output')
analyzer.indexer = CProjectIndexer()

for proj_name in ['ffmpeg-6.1.1', 'redis-8.0.2']:
    proj_path = analyzer.repository_dir / proj_name
    analyzer.indexer.index_project(str(proj_path), proj_name)

analyzer.process_entries()
analyzer.merge_results()
```

### 禁用缓存

```python
analyzer = SliceAnalyzer('input', 'output', use_cache=False)
```

### 清除缓存

```bash
rm -rf .cache/
```

### 导出函数调用图（DOT 格式）

```python
project_name = 'ffmpeg-6.1.1'
function_index = analyzer.indexer.function_index[project_name]

with open('callgraph.dot', 'w') as f:
    f.write('digraph CallGraph {\n')
    for func_name, func_infos in function_index.items():
        for func_info in func_infos:
            for callee in func_info.calls:
                f.write(f'  "{func_name}" -> "{callee}";\n')
    f.write('}\n')
```

然后使用 Graphviz 渲染：

```bash
dot -Tpng callgraph.dot -o callgraph.png
```

---

## 性能调优

| 场景 | 建议 |
|------|------|
| 内存不足 | 减小 `batch_size`（默认 1000），如改为 200 |
| 索引构建慢 | 确认缓存已开启；使用 SSD 存储 |
| 多次运行同一仓库 | 保留 `.cache/` 目录，自动跳过重新索引 |
| 数据量极大（>100 万条）| 手动拆分 `data.json`，多实例并行处理后合并 |

调整批次大小：

```python
analyzer.process_entries(batch_size=500)
```

---

## 故障排除

**Q：提示 `需要安装tree-sitter`**

```bash
pip install tree-sitter tree-sitter-c
```

**Q：大量条目出现 `function_not_found`**

- 检查 `project_name_with_version` 是否与 `repository/` 下目录名完全一致
- 检查 `file_path` 是否为相对路径（相对于项目根目录）
- 缺陷行可能位于宏定义或全局变量处，而非函数体内

**Q：中断后如何继续**

程序每 1000 条自动保存批次文件到 `output/`。中断后可直接运行阶段 3 合并已有批次：

```python
analyzer = SliceAnalyzer('input', 'output')
analyzer.build_index()   # 使用缓存，秒级完成
# 跳过 process_entries，直接合并
analyzer.merge_results()
```

或者删除 `output/results_batch_*.json` 后从头重新处理。

**Q：索引文件过大**

pickle 格式的索引文件大小取决于项目规模，正常情况下每万个函数约占 10-50 MB。可通过 `use_cache=False` 不持久化缓存来节省磁盘空间。

---

## 技术栈

| 技术 | 用途 |
|------|------|
| [tree-sitter](https://tree-sitter.github.io/) | 增量 C/C++ 语法树解析 |
| [tree-sitter-c](https://github.com/tree-sitter/tree-sitter-c) | C 语言语法支持 |
| Python `pickle` | 索引的序列化与反序列化 |
| BFS（collections.deque） | 多层函数调用依赖遍历 |
| Python `dataclass` | 函数信息的结构化表示 |
