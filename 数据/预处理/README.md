# 静态分析结果聚合与分析工具

本项目包含两个核心 Python 脚本，用于自动化处理和分析来自多个静态代码分析工具的扫描结果。

## 功能概述

1.  **`aggregate_results.py`**: 聚合来自不同工具（如 CodeQL, CSA, Semgrep）的原始报告，将它们解析、规范化，并整合成一个统一的 `results.json` 文件。
2.  **`analyze_results.py`**: 读取 `results.json` 文件，对聚合后的数据进行统计分析，并生成一份易于阅读的 Markdown 格式报告 `warnings_analysis.md`。
3.  **`cwe_analysis.py`**: 读取 `results.json` 文件，按工具统计 CWE（通用缺陷枚举）类型的数量，并生成详细的 `cwe_analysis_report.md` 报告。

---

## 文件结构

为了使脚本能够正确运行，请遵循以下目录结构：

```
.
├── codeql/                  # CodeQL 报告目录
│   ├── curl/
│   │   └── curl-8.11.1_codeql.sarif
│   └── ...
├── csa/                     # CSA (scan-build) 报告目录
│   ├── curl/
│   │   └── curl-8.11.1/
│   │       └── index.html
│   └── ...
├── semgrep/                 # Semgrep 报告目录
│   ├── curl/
│   │   └── curl-8.11.1_semgrep.json
│   └── ...
├── aggregate_results.py     # 结果聚合脚本
├── analyze_results.py       # 结果分析脚本
├── cwe_analysis.py          # CWE 分析脚本
├── results.json             # (自动生成) 聚合后的JSON结果
├── warnings_analysis.md     # (自动生成) Markdown分析报告
└── cwe_analysis_report.md   # (自动生成) CWE分析报告
```

- 每个工具一个主目录（`codeql`, `csa`, `semgrep`）。
- 在每个工具目录下，为每个被分析的项目创建一个子目录（如 `curl`, `ffmpeg`）。
- 将对应工具生成的原始报告文件放入相应的项目子目录中。

---

## 使用指南

### 1. 准备环境

确保您的 Python 环境中已安装所需的库。

```bash
pip install beautifulsoup4 pandas
```

### 2. 运行聚合脚本

首先，执行 `aggregate_results.py` 来处理原始报告并生成 `results.json`。

```bash
python aggregate_results.py
```

脚本会遍历所有工具目录，解析报告文件，并输出处理进度。完成后，您将在根目录下看到 `results.json` 文件。

### 3. 运行分析脚本

接着，执行 `analyze_results.py` 来分析聚合后的数据。

```bash
python analyze_results.py
```

该脚本会读取 `results.json`，进行数据统计，并生成 `warnings_analysis.md` 文件。

### 4. 运行CWE分析脚本

然后，可以运行 `cwe_analysis.py` 来生成按工具分类的 CWE 报告。脚本会自动读取 `docs/cwe-top10-2025` 文件，并在报告中高亮（加粗）属于 Top 10 的 CWE。

```bash
python cwe_analysis.py
```

此脚本会生成 `cwe_analysis_report.md` 文件。

### 5. 查看报告

最后，您可以直接打开 `warnings_analysis.md` 和 `cwe_analysis_report.md` 文件查看格式化的分析报告，其中包含了按工具、按项目和按项目版本分类的警告数量统计。
