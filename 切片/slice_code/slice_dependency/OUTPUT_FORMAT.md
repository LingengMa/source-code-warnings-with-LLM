# 输出格式说明

## 概述

本工具生成的结果采用JSON格式，所有字段名使用英文，便于国际化和程序化处理。

## 文件列表

### 1. final_results.json
主要输出文件，包含所有成功分析的条目。

### 2. failed_entries.json
包含分析失败的条目及失败原因。

## 详细字段说明

### final_results.json 结构

```json
[
  {
    // 基本信息
    "tool_name": "codeql",                          // 静态分析工具名称
    "project_simple_name": "ffmpeg",                // 项目简称（不含版本）
    "project_name": "ffmpeg-6.1.1",                 // 完整项目名（含版本）
    "project_version": "6.1.1",                     // 版本号
    "defect_file": "libavcodec/motion_est_template.c",  // 缺陷文件相对路径
    "defect_line": 785,                             // 缺陷行号
    
    // 目标函数信息
    "target_function": {
      "function_name": "sad_hpel_motion_search",    // 函数名
      "start_line": 780,                            // 函数起始行号
      "end_line": 850,                              // 函数结束行号
      "source_code": "static int sad_hpel_motion_search(...) { ... }",  // 完整源码
      "called_functions": ["sad", "cmp", "get_mb_score"]  // 该函数调用的其他函数
    },
    
    // 依赖分析（多层）
    "dependency_analysis": [
      {
        "level": 1,                                 // 依赖层级
        "functions": [                              // 该层级的所有函数
          {
            "function_name": "sad",                 // 函数名
            "file_path": "/absolute/path/to/dsputil.c",  // 完整文件路径
            "start_line": 100,                      // 起始行号
            "end_line": 120,                        // 结束行号
            "source_code": "static int sad(...) { ... }",  // 完整源码
            "called_functions": ["pix_abs"]         // 调用的函数
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

### 字段类型说明

| 字段路径 | 类型 | 说明 | 示例 |
|---------|------|------|------|
| `tool_name` | string | 静态分析工具名 | "codeql", "infer" |
| `project_simple_name` | string | 项目简称 | "ffmpeg", "redis" |
| `project_name` | string | 完整项目名 | "ffmpeg-6.1.1" |
| `project_version` | string | 版本号 | "6.1.1" |
| `defect_file` | string | 相对文件路径 | "libavcodec/file.c" |
| `defect_line` | integer | 行号（1-based） | 785 |
| `target_function.function_name` | string | 函数名 | "main" |
| `target_function.start_line` | integer | 起始行 | 100 |
| `target_function.end_line` | integer | 结束行 | 200 |
| `target_function.source_code` | string | 完整代码 | "int main() {...}" |
| `target_function.called_functions` | array[string] | 调用列表 | ["func1", "func2"] |
| `dependency_analysis` | array[object] | 依赖层级 | [...] |
| `dependency_analysis[].level` | integer | 层级编号 | 1, 2, 3 |
| `dependency_analysis[].functions` | array[object] | 函数列表 | [...] |
| `dependency_analysis[].functions[].function_name` | string | 函数名 | "helper" |
| `dependency_analysis[].functions[].file_path` | string | 完整路径 | "/path/to/file.c" |
| `dependency_analysis[].functions[].start_line` | integer | 起始行 | 50 |
| `dependency_analysis[].functions[].end_line` | integer | 结束行 | 75 |
| `dependency_analysis[].functions[].source_code` | string | 完整代码 | "void helper() {...}" |
| `dependency_analysis[].functions[].called_functions` | array[string] | 调用列表 | ["func3"] |

### failed_entries.json 结构

```json
[
  {
    // 原始输入字段（保留中文）
    "静态分析工具名": "codeql",
    "简单项目名(不带版本)": "ffmpeg",
    "项目名(带版本)": "ffmpeg-6.1.1",
    "项目版本": "6.1.1",
    "缺陷所属文件": "unknown_file.c",
    "缺陷行": 100,
    
    // 失败原因（英文）
    "reason": "function_not_found"
  }
]
```

### 失败原因代码

| 原因代码 | 说明 |
|---------|------|
| `function_not_found` | 在指定位置找不到函数定义 |
| `file_not_found` | 文件不存在 |
| `parse_error` | 文件解析失败 |
| `line_out_of_range` | 行号超出文件范围 |
| 其他字符串 | 异常错误消息 |

## 使用示例

### Python 读取结果

```python
import json

# 读取结果
with open('output/final_results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# 遍历每个条目
for entry in results:
    print(f"项目: {entry['project_name']}")
    print(f"目标函数: {entry['target_function']['function_name']}")
    
    # 遍历依赖层级
    for dep_layer in entry['dependency_analysis']:
        level = dep_layer['level']
        func_count = len(dep_layer['functions'])
        print(f"  第{level}层: {func_count} 个函数")
        
        for func in dep_layer['functions']:
            print(f"    - {func['function_name']} ({func['file_path']})")
```

### 统计分析

```python
import json
from collections import Counter

with open('output/final_results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# 统计每个项目的缺陷数
project_defects = Counter(entry['project_name'] for entry in results)
print("项目缺陷统计:")
for project, count in project_defects.most_common(10):
    print(f"  {project}: {count}")

# 统计依赖深度分布
max_depths = []
for entry in results:
    max_depth = max((layer['level'] for layer in entry['dependency_analysis']), default=0)
    max_depths.append(max_depth)

print(f"\n依赖深度统计:")
print(f"  平均深度: {sum(max_depths) / len(max_depths):.2f}")
print(f"  最大深度: {max(max_depths)}")
```

### 导出为CSV

```python
import json
import csv

with open('output/final_results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

# 导出基本信息
with open('output/summary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Tool', 'Project', 'File', 'Line', 'Function', 'Dependency Layers'])
    
    for entry in results:
        writer.writerow([
            entry['tool_name'],
            entry['project_name'],
            entry['defect_file'],
            entry['defect_line'],
            entry['target_function']['function_name'],
            len(entry['dependency_analysis'])
        ])

print("已导出到 output/summary.csv")
```

### 查询特定函数

```python
import json

def find_function_usages(function_name: str, results_file: str = 'output/final_results.json'):
    """查找函数的所有使用位置"""
    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    usages = []
    for entry in results:
        # 检查目标函数
        if entry['target_function']['function_name'] == function_name:
            usages.append({
                'type': 'target',
                'project': entry['project_name'],
                'file': entry['defect_file'],
                'line': entry['defect_line']
            })
        
        # 检查依赖函数
        for dep_layer in entry['dependency_analysis']:
            for func in dep_layer['functions']:
                if func['function_name'] == function_name:
                    usages.append({
                        'type': f'dependency_level_{dep_layer["level"]}',
                        'project': entry['project_name'],
                        'file': func['file_path'],
                        'line': func['start_line']
                    })
    
    return usages

# 使用示例
usages = find_function_usages('malloc')
print(f"找到 {len(usages)} 处使用")
for usage in usages[:10]:
    print(f"  {usage['project']} - {usage['file']}:{usage['line']} ({usage['type']})")
```

## 数据质量

### 完整性
- ✅ 所有成功分析的条目都包含完整字段
- ✅ `source_code` 包含函数的完整源代码
- ✅ `called_functions` 列出所有静态可识别的函数调用

### 准确性
- ✅ 行号基于1-based索引（与编辑器一致）
- ✅ 路径使用绝对路径，避免歧义
- ✅ 函数调用通过AST精确提取

### 局限性
- ⚠️ 无法识别函数指针和虚函数调用
- ⚠️ 宏展开后的函数调用可能无法识别
- ⚠️ 内联函数可能被当作普通函数处理

## 版本变更

### v1.0 (2025-12-18)
- 初始版本
- 所有字段名改为英文
- 依赖分析结构优化（level + functions数组）
- 添加完整的字段类型说明

## 相关文档

- **README.md**: 项目概述
- **USAGE.md**: 使用指南
- **FILE_STRUCTURE.md**: 项目结构
