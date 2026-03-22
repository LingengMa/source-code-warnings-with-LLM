# output/annotated_data.json 字段说明

本文件由 `merge_annotations.py` 生成，将 `data.json`（1025 条不一致告警）与 `annotations.json`（人工标注结果）按 `id` 合并。

---

## 顶层字段

| 字段 | 类型 | 来源 | 说明 |
|------|------|------|------|
| `id` | `int` | base_data | 全局自增唯一标识符 |
| `tool_name` | `string` | base_data | 静态分析工具名称，如 `"codeql"`、`"csa"`、`"semgrep"` |
| `project_name` | `string` | base_data | 项目名称，如 `"ffmpeg"` |
| `project_name_with_version` | `string` | base_data | 项目名称+版本号，如 `"ffmpeg-6.1.1"` |
| `project_version` | `string` | base_data | 项目版本号，如 `"6.1.1"` |
| `file_path` | `string` | base_data | 告警所在文件的相对路径（相对于项目根目录） |
| `line_number` | `int` | base_data | 告警所在行号 |
| `cwe` | `string[]` | base_data | 关联的 CWE 编号列表，如 `["CWE-120", "CWE-125"]` |
| `rule_id` | `string` | base_data | 工具内部规则 ID |
| `message` | `string` | base_data | 工具输出的告警描述信息 |
| `severity` | `string \| null` | base_data | 告警严重级别（部分工具未提供，值为 `null`） |
| `function_name` | `string` | base_data | 告警所在函数名 |
| `label` | `string` | base_data（算法） | 版本追踪算法生成的标签：`"TP"` / `"FP"` / `"Unknown"` |
| `llm_results` | `object` | llm-match | 四种 LLM 分类模式的输出，详见下节 |
| `sliced_code` | `string` | 切片 | 围绕告警行提取的程序切片代码，告警行标注有 `// The line where the warning is located` |
| `manual_annotation` | `string \| null` | 人工标注 | 人工标注结果：`"TP"` / `"FP"` / `"Unknown"`；未标注时为 `null` |
| `annotation_reason` | `string \| null` | 人工标注 | 人工标注时填写的判断理由；未标注时为 `null` |
| `annotation_timestamp` | `string \| null` | 人工标注 | 标注时间，ISO 8601 格式，如 `"2026-03-21T00:02:26.544881"`；未标注时为 `null` |

---

## `llm_results` 字段

`llm_results` 是一个对象，包含四个键，对应 LLM 分类的四种模式组合：

| 键 | 含义 |
|----|------|
| `wuwl` | 三分类（with Unknown）+ 含算法标签（with Label） |
| `wuol` | 三分类（with Unknown）+ 不含算法标签（without Label） |
| `ouwl` | 二分类（without Unknown）+ 含算法标签（with Label） |
| `ouol` | 二分类（without Unknown）+ 不含算法标签（without Label） |

每个键对应的值结构如下：

| 子字段 | 类型 | 说明 |
|--------|------|------|
| `llm_label` | `string` | LLM 输出的分类结果：`"TP"` / `"FP"` / `"Unknown"`（二分类模式无 `"Unknown"`） |
| `llm_label_reason` | `string` | LLM 给出的判断理由 |
| `mode_desc` | `string` | 模式的中文描述，如 `"三分类+含算法标签"` |

---

## 标签含义

| 标签 | 含义 |
|------|------|
| `TP`（True Positive） | 真实缺陷，告警有效 |
| `FP`（False Positive） | 误报，告警无效 |
| `Unknown` | 无法确定（仅算法标签和三分类 LLM 模式会出现） |

---

## 数据筛选说明

`data.json`（本文件的基础数据集）是从完整的 2510 条告警中筛选出的 **1025 条不一致告警**——即算法标签与四种 LLM 标签五者并非完全相同的告警。这些记录是人工标注的目标，最终通过 `manual_annotation` 字段提供裁决标签。

`input/origin_data` 有未进行人工标注的原始 2510 条警告.
