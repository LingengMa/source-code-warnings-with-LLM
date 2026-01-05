# 项目文件说明

## 核心文件

### slice_analyzer.py
**主程序** - 完整的代码切片和依赖分析工具

**核心类:**
- `FunctionInfo`: 函数信息数据类
- `SliceResult`: 切片结果数据类
- `CProjectIndexer`: C项目索引器（使用tree-sitter进行AST解析）
- `SliceAnalyzer`: 主控制器（协调索引构建和批量处理）

**工作流程:**
1. **阶段1: 构建索引** - 解析所有项目，构建函数索引和调用图
2. **阶段2: 批量处理** - 流式读取data.json，查询索引，提取切片
3. **阶段3: 合并结果** - 合并所有批次文件为最终结果

**性能特点:**
- ✅ 先索引后查询，避免重复解析
- ✅ 批量保存，支持超大数据集
- ✅ 内存索引，查询速度快
- ✅ 容错设计，单个失败不影响整体

### cache_manager.py
**缓存管理器** - 索引缓存支持

**功能:**
- 保存构建好的索引到磁盘
- 自动检测项目更新
- 加速后续运行

**使用:**
```python
analyzer = SliceAnalyzer('input', 'output', use_cache=True)
```

## 辅助脚本

### run.py
**快速运行脚本** - 带进度监控的交互式界面

**特点:**
- 显示文件统计信息
- 询问确认后执行
- 详细的进度和时间统计
- 友好的错误提示

### test_tool.py
**测试脚本** - 验证工具功能

**测试内容:**
- 数据文件可访问性
- 索引器功能
- 基本解析能力

### demo.py
**演示脚本** - 展示核心功能

**演示内容:**
- 单个项目索引构建
- 函数依赖分析
- 代码提取

## 配置文件

### requirements.txt
**依赖列表**

```
tree-sitter>=0.20.0
tree-sitter-c>=0.20.0
```

## 文档

### README.md
**项目概述** - 功能介绍、快速开始

### USAGE.md
**详细使用指南** - 完整的使用说明、故障排除、高级用法

### FILE_STRUCTURE.md
**本文件** - 项目结构说明

## 目录结构

```
slice_dependency_new/
│
├── 核心程序
│   ├── slice_analyzer.py      # 主程序
│   └── cache_manager.py       # 缓存管理
│
├── 辅助脚本
│   ├── run.py                 # 快速运行
│   ├── test_tool.py          # 测试工具
│   └── demo.py               # 功能演示
│
├── 配置和文档
│   ├── requirements.txt      # 依赖
│   ├── README.md            # 概述
│   ├── USAGE.md             # 使用指南
│   └── FILE_STRUCTURE.md    # 本文件
│
├── 输入数据
│   └── input/
│       ├── data.json         # 待分析条目（109MB，382万条）
│       └── repository/       # 项目源代码（58个项目）
│
├── 输出结果
│   └── output/
│       ├── final_results.json      # 最终结果
│       └── failed_entries.json     # 失败条目
│
└── 缓存（自动生成）
    └── .cache/
        ├── function_index.pkl      # 序列化的索引
        └── index_meta.json        # 索引元数据
```

## 使用建议

### 首次使用
1. 运行测试: `python test_tool.py`
2. 查看演示: `python demo.py`
3. 阅读文档: `USAGE.md`
4. 正式运行: `python run.py`

### 开发调试
- 使用 `demo.py` 测试单个项目
- 修改 `slice_analyzer.py` 中的批次大小进行调试
- 查看 `failed_entries.json` 了解失败原因

### 生产使用
- 使用 `run.py` 进行完整分析
- 启用缓存加速（默认）
- 定期备份 `.cache/` 目录

## 扩展建议

### 支持更多语言
在 `CProjectIndexer` 中添加其他语言支持:

```python
import tree_sitter_python
import tree_sitter_java

# 添加语言检测和解析器选择逻辑
```

### 并行处理
使用 `multiprocessing` 并行索引多个项目:

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as executor:
    futures = [executor.submit(index_project, proj) for proj in projects]
```

### Web界面
添加Web前端进行可视化查询:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/query/<project>/<file>/<line>')
def query_function(project, file, line):
    # 查询逻辑
    return jsonify(result)
```

### 增量更新
支持只更新变化的项目:

```python
# 检测Git变更
changed_files = subprocess.check_output(['git', 'diff', '--name-only'])
# 只重新索引变化的文件
```

## 性能指标

基于测试数据估算:

| 项目 | 文件数 | 函数数 | 索引时间 |
|------|--------|--------|----------|
| redis-7.0.11 | 567 | 6,494 | ~2秒 |
| openssl-3.2.1 | 2,010 | 14,648 | ~5秒 |
| ffmpeg-6.1.1 | ~3,000 | ~20,000 | ~10秒 |

**完整索引构建**: 约20-60分钟（58个项目，首次）

**使用缓存**: 0秒（加载预构建索引）

**批量查询**: 约0.1-1秒/条（382万条预计10-20小时）

## 注意事项

1. **内存使用**: 全量索引可能占用1-2GB内存
2. **磁盘空间**: 缓存文件可能占用数百MB
3. **解析失败**: 某些复杂C++语法可能解析失败（会自动跳过）
4. **路径匹配**: 使用模糊匹配处理不同的文件路径格式

## 常见问题

**Q: 如何查看处理进度?**
A: 观察终端输出，或者查看 `output/` 目录中的批次文件数量

**Q: 可以中途停止吗?**
A: 可以，已处理的批次会保存，可以手动合并或删除后重新运行

**Q: 如何提高速度?**
A: 
- 启用缓存（默认）
- 使用SSD
- 增加批次大小
- 考虑并行处理（需修改代码）

**Q: 结果准确吗?**
A: 基于AST静态分析，准确度取决于：
- tree-sitter解析质量（一般很高）
- 代码复杂度（宏、模板可能影响）
- 函数指针和动态调用（无法静态分析）

## 许可和致谢

使用的开源库:
- **tree-sitter**: MIT License
- **tree-sitter-c**: MIT License

感谢这些优秀的开源项目！
