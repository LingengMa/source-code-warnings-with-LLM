# Program Slicer for C/C++ Projects

这是一个基于 Joern PDG 的程序切片工具，用于对复杂 C/C++ 项目进行精确的前向和后向切片。

## 功能特性

- ✅ 支持复杂 C/C++ 项目的程序切片
- ✅ 基于预生成的 PDG（程序依赖图）进行高效切片
- ✅ 双向切片：前向切片 + 后向切片
- ✅ AST 语法修复，确保输出代码语法正确
- ✅ 自动识别并记录所在函数信息
- ✅ 支持批量处理多个切片任务
- ✅ **分块保存**: 自动分chunk保存结果,避免内存溢出
- ✅ **断点续传**: 支持中断后继续处理,不会重复计算
- ✅ **进度跟踪**: 实时保存进度,随时查看处理状态

## 目录结构

```
slice_joern/
├── README.md              # 本文件
├── slicer.py             # 主程序入口
├── pdg_loader.py         # PDG 加载和解析模块
├── slice_engine.py       # 切片引擎核心逻辑
├── config.py             # 配置文件
├── requirements.txt      # 依赖包
├── slice_input/          # 输入数据
│   ├── data.json        # 切片任务列表
│   ├── repository/      # 源代码仓库
│   ├── cpg/             # Joern CPG 文件
│   └── pdg/             # Joern PDG 文件
└── slice_output/         # 输出结果
    └── slices.json      # 切片结果
```

## 使用方法

### 1. 激活虚拟环境

```bash
conda activate slice
```

### 2. 安装依赖

```bash
cd slice_joern
pip install -r requirements.txt
```

### 3. 运行切片

```bash
# 基本用法 - 正常执行切片 (完成后自动合并chunk文件)
python single_file_slicer.py

# 查看当前进度
python single_file_slicer.py --progress

# 清除断点重新开始
python single_file_slicer.py --clear

# 自定义chunk大小(默认100)
python single_file_slicer.py --chunk-size 200
```

### 4. 监控进度

```bash
# 使用便捷脚本查看进度
python show_progress.py

# 或使用原始命令
python single_file_slicer.py --progress
```

### 5. 后台运行 (推荐用于大量任务)

```bash
# 使用 nohup 后台运行
nohup python single_file_slicer.py > slice.log 2>&1 &

# 查看日志
tail -f slice.log

# 或使用 screen (推荐)
screen -S slicing
python single_file_slicer.py
# 按 Ctrl+A+D 退出, screen -r slicing 重新连接
```

### 6. 查看结果

结果保存在 `slice_output/slices.json`，包含：
- 切片后的完整代码
- 所在函数信息
- 切片行号映射
- 元数据信息

## 配置参数

在 `config.py` 中可以调整：
- `BACKWARD_DEPTH`: 后向切片深度（默认：4）
- `FORWARD_DEPTH`: 前向切片深度（默认：4）
- `ENABLE_AST_FIX`: 是否启用 AST 修复（默认：True）
- `OUTPUT_FORMAT`: 输出格式（json/markdown）
- `CHUNK_SIZE`: 每个chunk保存的任务数（默认：100）
- `ENABLE_CHECKPOINT`: 是否启用断点续传（默认：True）

## 断点续传与分块保存

### 工作原理

- 程序每处理完一个任务就保存断点
- 每处理 N 个任务（CHUNK_SIZE）保存一个chunk文件
- 中断后重新运行会自动跳过已处理的任务
- 所有进度信息保存在 `slice_output/` 目录

### 输出文件

```
slice_output/
├── slices_chunk_0001.json          # 第1个chunk
├── slices_chunk_0001_summary.json  # chunk摘要
├── slices_chunk_0002.json          # 第2个chunk
├── ...
├── checkpoint.json                 # 断点文件
├── progress.json                   # 进度文件
├── slices.json                     # 最终合并文件
└── slices_summary.json             # 最终摘要
```

### 使用场景

- **大规模任务** (5万+): 避免内存溢出,分批保存结果
- **长时间运行**: 支持中断恢复,不丢失已处理数据
- **调试优化**: 可以查看部分结果,无需等待全部完成

详细使用说明请参考 [USAGE.md](USAGE.md)

## 算法原理

1. **加载 PDG**：从预生成的 PDG 文件加载程序依赖图
2. **定位目标行**：在 PDG 中找到目标代码行对应的节点
3. **后向切片**：沿 DDG/CDG 边向上追溯依赖
4. **前向切片**：沿 DDG/CDG 边向下追踪影响
5. **AST 修复**：使用 Tree-sitter 补全语法结构
6. **代码生成**：提取切片行并生成完整代码

## 示例输出

```json
{
    "project": "vim-9.1.1896",
    "file": "src/uninstall.c",
    "line": 32,
    "function": "main",
    "sliced_code": "完整的切片代码...",
    "slice_lines": [1, 5, 10, 15, 32, 45],
    "metadata": {
        "backward_nodes": 15,
        "forward_nodes": 8,
        "total_lines": 23
    }
}
```
