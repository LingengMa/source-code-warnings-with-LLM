# 高性能代码切片和依赖分析工具

一个基于AST的C/C++代码切片和函数依赖分析工具，采用"先全量索引/建图，再批量查询"的高性能架构，可处理超大规模代码库和海量分析任务。

## ✨ 核心特性

### 🚀 高性能架构
- **一次索引，多次使用**: 构建全量函数索引和调用图，支持快速批量查询
- **智能缓存**: 自动保存和加载索引，避免重复构建
- **流式处理**: 支持处理超大JSON文件（100MB+），批量保存结果
- **增量安全**: 定期保存批次结果，支持断点续传

### 🎯 功能全面
- ✅ 自动定位指定行号所在的函数
- ✅ 提取完整函数源代码
- ✅ 分析多层函数依赖关系（默认3层，可配置）
- ✅ 识别所有函数调用
- ✅ 详细的JSON格式输出

### 🔧 易于使用
- 📖 详细的文档和示例
- 🧪 完整的测试和演示脚本
- 🎨 友好的命令行界面
- ⚠️ 智能错误处理和日志

## 📊 数据规模

本工具设计用于处理：
- ✅ **58个开源项目** (ffmpeg, redis, curl, git, nginx, openssl等)
- ✅ **382万条分析记录** (109MB JSON文件)
- ✅ **数万个源文件** (C/C++代码)
- ✅ **数十万个函数** 

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 测试工具

```bash
# 运行功能测试
python test_tool.py

# 查看演示
python demo.py
```

### 3. 运行分析

**推荐方式（交互式）:**
```bash
python run.py
```

**直接运行:**
```bash
python slice_analyzer.py
```

**Python API:**
```python
from slice_analyzer import SliceAnalyzer

analyzer = SliceAnalyzer('input', 'output')
analyzer.build_index()      # 阶段1: 构建索引
analyzer.process_entries()  # 阶段2: 批量处理
analyzer.merge_results()    # 阶段3: 合并结果
```

## 📁 输入格式

### input/data.json
每条记录包含待分析的代码位置信息：

```json
[
    {
        "静态分析工具名": "codeql",
        "简单项目名(不带版本)": "ffmpeg",
        "项目名(带版本)": "ffmpeg-6.1.1",
        "项目版本": "6.1.1",
        "缺陷所属文件": "libavcodec/motion_est_template.c",
        "缺陷行": 785
    }
]
```

### input/repository/
包含所有项目的源代码：
```
repository/
├── ffmpeg-6.1.1/
├── redis-8.0.2/
├── curl-8_11_1/
└── ...
```

## 📤 输出格式

### output/final_results.json
完整的分析结果，包含目标函数和3层依赖：

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
                        "source_code": "...",
                        "called_functions": ["pix_abs"]
                    }
                ]
            },
            {
                "level": 2,
                "functions": [...]
            },
            {
                "level": 3,
                "functions": [...]
            }
        ]
    }
]
```

### output/failed_entries.json
处理失败的条目（如果有）：

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

## ⚡ 性能特点

### 索引构建（阶段1）
- **首次运行**: 20-60分钟（取决于项目规模）
- **使用缓存**: ~0秒（自动加载预构建索引）
- **内存占用**: 1-2GB

### 批量查询（阶段2）
- **查询速度**: 0.1-1秒/条
- **382万条数据**: 预计10-20小时
- **批量保存**: 每1000条自动保存

### 示例性能
| 项目 | 文件数 | 函数数 | 索引时间 |
|------|--------|--------|----------|
| redis-7.0.11 | 567 | 6,494 | ~2秒 |
| openssl-3.2.1 | 2,010 | 14,648 | ~5秒 |
| ffmpeg-6.1.1 | ~3,000 | ~20,000 | ~10秒 |

## 🛠️ 技术栈

- **tree-sitter**: 高性能增量解析器
- **tree-sitter-c**: C/C++语法支持
- **AST分析**: 精确的语法树遍历
- **BFS算法**: 高效的依赖图搜索

## 📚 文档

- **README.md** (本文件): 项目概述和快速开始
- **USAGE.md**: 详细使用指南、故障排除、高级用法
- **FILE_STRUCTURE.md**: 项目结构说明、扩展建议

## 🎯 使用场景

### 代码审计
快速定位漏洞代码及其依赖链，评估影响范围

### 缺陷分析
分析静态分析工具报告的问题，理解问题上下文

### 代码理解
理解大型代码库中的函数调用关系

### 影响分析
评估修改某个函数可能影响的其他函数

## 🔍 示例输出

运行演示查看实际效果：

```bash
$ python demo.py

======================================================================
代码切片和依赖分析工具 - 演示
======================================================================

📦 演示项目: redis-7.0.11

步骤 1: 构建索引
----------------------------------------------------------------------
正在索引项目: redis-7.0.11
  找到 567 个C/C++文件
  已处理 100/567 个文件
  ...
  完成! 索引了 6494 个函数，耗时 1.92秒

统计:
  - 不同函数名数量: 5977
  - 函数定义总数: 6494
  - 文件数量: 388

步骤 2: 依赖分析演示
----------------------------------------------------------------------

目标函数: crc64Hash
  文件: tracking_collisions.c
  位置: 第34-36行
  调用的函数: crc64

依赖分析（3层）:

  第0层: 1 个函数
    - crc64Hash (目标函数)

  第1层: 1 个函数
    1. crc64 (crc64.c)

  第2层: 1 个函数
    1. crcspeed64native (crcspeed.c)

步骤 3: 代码提取演示
----------------------------------------------------------------------

目标函数代码片段:
----------------------------------------------------------------------
  34 | uint64_t crc64Hash(char *key, size_t len) {
  35 |     return crc64(0,(unsigned char*)key,len);
  36 | }

======================================================================
✅ 演示完成!
======================================================================
```

## ⚙️ 高级配置

### 调整依赖深度

```python
# 在 slice_analyzer.py 中修改
dep_layers = self.indexer.get_dependencies(
    project_name, 
    target_func.name, 
    depth=5  # 改为5层
)
```

### 调整批次大小

```python
# 更大的批次减少I/O，但占用更多内存
analyzer.process_entries(batch_size=2000)
```

### 禁用缓存

```python
analyzer = SliceAnalyzer('input', 'output', use_cache=False)
```

## 🐛 故障排除

### 内存不足
- 减小批次大小
- 分批处理项目
- 增加系统swap

### 索引构建慢
- 使用缓存（默认启用）
- 使用SSD存储
- 排除不必要的文件

### 找不到函数
检查 `output/failed_entries.json` 了解失败原因

详细的故障排除指南请参考 `USAGE.md`

## 📝 注意事项

1. ⚠️ 首次运行需要构建索引，可能耗时较长
2. 💾 索引会自动缓存，后续运行会快速加载
3. 🔄 结果采用批次保存，支持断点续传
4. 📊 处理失败的条目会单独记录

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可

使用的开源库:
- tree-sitter (MIT License)
- tree-sitter-c (MIT License)

---

**祝您使用愉快！如有问题，请查看 `USAGE.md` 或提交Issue。**
