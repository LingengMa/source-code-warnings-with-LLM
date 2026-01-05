# 使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 准备数据

确保以下目录结构：

```
slice_dependency_new/
├── input/
│   ├── data.json              # 待分析条目
│   └── repository/            # 项目源代码
│       ├── ffmpeg-6.1.1/
│       ├── redis-8.0.2/
│       └── ...
├── output/                     # 输出目录（自动创建）
└── slice_analyzer.py          # 主程序
```

### 3. 运行分析

**方式1: 使用快速运行脚本（推荐）**
```bash
python run.py
```

**方式2: 直接运行主程序**
```bash
python slice_analyzer.py
```

**方式3: 使用Python解释器**
```bash
python
>>> from slice_analyzer import SliceAnalyzer
>>> analyzer = SliceAnalyzer('input', 'output')
>>> analyzer.build_index()
>>> analyzer.process_entries()
>>> analyzer.merge_results()
```

## 工作流程

### 阶段 1: 构建索引（一次性）

程序会：
1. 扫描所有项目目录
2. 解析所有C/C++源文件（.c, .h, .cpp, .cc, .cxx）
3. 提取所有函数定义和调用关系
4. 构建内存索引

**性能**: 
- 索引会自动缓存到 `.cache/` 目录
- 首次运行需要较长时间（取决于项目规模）
- 后续运行会直接加载缓存（除非项目有更新）

**示例输出**:
```
正在索引项目: ffmpeg-6.1.1
  找到 1234 个C/C++文件
  已处理 100/1234 个文件
  ...
  完成! 索引了 15678 个函数，耗时 12.34秒
```

### 阶段 2: 批量处理

程序会：
1. 流式读取 `data.json`
2. 对每条记录：
   - 根据文件路径和行号定位目标函数
   - 提取函数完整代码
   - 分析3层函数依赖关系
3. 批量保存结果（每1000条）

**性能优化**:
- 基于内存索引快速查询
- 批量处理，定期保存
- 支持断点续传

**示例输出**:
```
进度: 1000/382649 (0%)
已保存批次结果: output/results_batch_1234567890.json (1000 条)
进度: 2000/382649 (0%)
...
```

### 阶段 3: 合并结果

程序会：
1. 收集所有批次文件
2. 合并为单一JSON文件
3. 清理临时批次文件

**输出**:
- `output/final_results.json` - 最终结果
- `output/failed_entries.json` - 处理失败的条目（如果有）

## 输出格式

### final_results.json

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
            "file_path": "/path/to/dsputil.c",
            "start_line": 100,
            "end_line": 120,
            "source_code": "static int sad(...) { ... }",
            "called_functions": ["pix_abs"]
          },
          {
            "function_name": "cmp",
            "file_path": "/path/to/cmp.c",
            "start_line": 200,
            "end_line": 250,
            "source_code": "static int cmp(...) { ... }",
            "called_functions": ["compare_values"]
          }
        ]
      },
      {
        "level": 2,
        "functions": [
          {
            "function_name": "pix_abs",
            "file_path": "/path/to/pixelutils.c",
            "start_line": 50,
            "end_line": 80,
            "source_code": "int pix_abs(...) { ... }",
            "called_functions": []
          }
        ]
      },
      {
        "level": 3,
        "functions": []
      }
    ]
  }
]
```

### 字段说明

**顶层字段:**
- `tool_name`: 静态分析工具名称
- `project_simple_name`: 简单项目名（不带版本）
- `project_name`: 完整项目名（带版本）
- `project_version`: 项目版本号
- `defect_file`: 缺陷所在文件路径
- `defect_line`: 缺陷所在行号

**target_function (目标函数):**
- `function_name`: 函数名
- `start_line`: 函数起始行号
- `end_line`: 函数结束行号
- `source_code`: 完整函数源代码
- `called_functions`: 该函数调用的其他函数列表

**dependency_analysis (依赖分析):**
- `level`: 依赖层级（1, 2, 3）
- `functions`: 该层级的函数列表
  - `function_name`: 函数名
  - `file_path`: 函数所在文件的完整路径
  - `start_line`: 起始行号
  - `end_line`: 结束行号
  - `source_code`: 完整函数源代码
  - `called_functions`: 调用的函数列表

### failed_entries.json

记录无法处理的条目：

```json
[
  {
    "静态分析工具名": "codeql",
    "项目名(带版本)": "ffmpeg-6.1.1",
    "缺陷所属文件": "unknown_file.c",
    "缺陷行": 100,
    "reason": "function_not_found"
  }
]
```

可能的失败原因：
- `function_not_found`: 无法找到包含该行号的函数
- 文件不存在或无法解析
- 行号超出文件范围

## 性能调优

### 1. 调整批次大小

在 `slice_analyzer.py` 中修改：

```python
analyzer.process_entries(batch_size=1000)  # 默认1000，可调整
```

- 较大的批次: 减少I/O，但占用更多内存
- 较小的批次: 更频繁保存，更安全

### 2. 禁用缓存

如果不需要缓存：

```python
analyzer = SliceAnalyzer('input', 'output', use_cache=False)
```

### 3. 清理缓存

手动删除缓存：

```bash
rm -rf .cache/
```

## 故障排除

### 1. 内存不足

**症状**: 程序崩溃或系统卡顿

**解决方案**:
- 减小批次大小
- 分批处理项目
- 增加系统swap空间

### 2. 索引构建慢

**原因**: 项目规模大

**优化**:
- 使用缓存（默认启用）
- 排除测试文件和第三方库
- 使用SSD存储

### 3. 找不到函数

**可能原因**:
- 缺陷行不在任何函数内（全局变量、宏定义等）
- 文件路径不匹配
- 解析失败

**检查方法**:
查看 `failed_entries.json` 了解详情

## 高级用法

### 自定义依赖深度

默认分析3层依赖，可修改：

```python
dep_layers = self.indexer.get_dependencies(
    project_name, 
    target_func.name, 
    depth=5  # 改为5层
)
```

### 只索引特定项目

```python
analyzer = SliceAnalyzer('input', 'output')
analyzer.indexer = CProjectIndexer()

# 只索引感兴趣的项目
projects_to_index = ['ffmpeg-6.1.1', 'redis-8.0.2']
for proj in projects_to_index:
    proj_path = analyzer.repository_dir / proj
    analyzer.indexer.index_project(str(proj_path), proj)

analyzer.process_entries()
analyzer.merge_results()
```

### 导出函数调用图

```python
# 获取某个项目的完整调用图
project_name = 'ffmpeg-6.1.1'
function_index = analyzer.indexer.function_index[project_name]

# 导出为DOT格式（可用Graphviz可视化）
with open('callgraph.dot', 'w') as f:
    f.write('digraph CallGraph {\n')
    for func_name, func_infos in function_index.items():
        for func_info in func_infos:
            for callee in func_info.calls:
                f.write(f'  "{func_name}" -> "{callee}";\n')
    f.write('}\n')
```

## 常见问题

**Q: 处理需要多长时间？**

A: 取决于项目规模和数据量：
- 索引构建: 10-60分钟（首次），0秒（使用缓存）
- 批量处理: 约0.1-1秒/条（基于索引查询）
- 对于38万条数据，预计10-20小时

**Q: 支持哪些编程语言？**

A: 目前仅支持C/C++。如需支持其他语言，需要：
1. 安装对应的tree-sitter语言包
2. 修改 `CProjectIndexer` 类

**Q: 如何中断后继续？**

A: 程序会定期保存批次结果。如果中断：
1. 查看 `output/` 目录中已保存的批次文件
2. 手动运行阶段3合并结果
3. 或者删除已处理的条目，重新运行

**Q: 可以并行处理吗？**

A: 当前版本使用单进程。如需并行：
- 可以手动分割 `data.json`
- 分别运行多个实例
- 最后合并结果

## 技术细节

### 使用的技术

- **tree-sitter**: 增量解析器生成器
- **tree-sitter-c**: C语言语法
- **AST**: 抽象语法树分析
- **BFS**: 广度优先搜索依赖

### 数据结构

```python
# 函数索引: {项目名: {函数名: [函数信息列表]}}
function_index = {
    'ffmpeg-6.1.1': {
        'main': [FunctionInfo(...), FunctionInfo(...)],
        'decode': [FunctionInfo(...)]
    }
}

# 文件索引: {项目名: {文件路径: [函数名列表]}}
file_functions = {
    'ffmpeg-6.1.1': {
        'ffmpeg.c': ['main', 'init', 'cleanup'],
        'decode.c': ['decode', 'decode_frame']
    }
}
```

### 查找算法

1. **定位函数**: 在文件索引中查找包含目标行号的函数
2. **依赖分析**: BFS遍历函数调用图
3. **去重**: 使用集合避免重复访问
