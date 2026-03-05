# LLM 静态分析告警分类工具

本工具使用大语言模型（LLM）对静态分析工具产生的告警进行自动分类，判断每条告警是**真实漏洞（TP）**还是**误报（FP）**。

---

## 目录结构

```
llm-match/
├── llm.py                  # 主运行脚本
├── add_file_path.py        # 为结果文件补充 file_path 字段的工具脚本
├── analyze_results.py      # 结果统计分析脚本
├── prompts/                # 四种模式的提示词模板
├── input/
│   ├── data.json                      # 原始告警数据（含真实标签）
│   └── slices_for_llm_with_label.json # 供 LLM 处理的切片数据
└── output/
    ├── results_with_unknown_with_label.json
    ├── results_with_unknown_without_label.json
    ├── results_without_unknown_with_label.json
    └── results_without_unknown_without_label.json
```

---

## 输出 JSON 字段说明

每个输出文件均为 JSON 数组，每个元素对应一条告警的完整处理结果，包含以下字段：

### LLM 输出字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `llm_label` | `string` | LLM 给出的分类结果。取值为 `"TP"`（真实告警）、`"FP"`（误报），三分类模式下还包含 `"Unknown"`（无法确定） |
| `llm_label_reason` | `string` | LLM 对分类结论的文字解释，说明判断依据 |

### 告警基本信息字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `id` | `integer` | 告警唯一标识，全局自增 ID |
| `tool_name` | `string` | 产生该告警的静态分析工具名称，如 `"codeql"` |
| `rule_id` | `string` | 触发告警的规则编号，如 `"cpp/offset-use-before-range-check"` |
| `message` | `string` | 静态分析工具生成的告警描述文本 |
| `line_number` | `integer` | 告警所在的源文件行号 |
| `function_name` | `string` | 告警所在的函数名，全局代码显示为 `"<global>"` |

### 项目与文件定位字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `project_name_with_version` | `string` | 项目名称及版本号，如 `"ffmpeg-6.1.1"` |
| `project_version` | `string` | 项目版本号，如 `"6.1.1"` |
| `file_path` | `string` | 告警所在源文件的相对路径（相对于项目根目录） |
| `full_file_path` | `string` | 告警源文件的完整本地路径，格式为 `input/repository/{project_name_with_version}/{file_path}` |

### 代码切片字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `sliced_code` | `string` | 经程序切片（Program Slicing）分析后提取的代码片段。包含与告警直接相关的数据流和控制流路径，以及被调用函数的定义。告警所在行以注释 `// The line where the warning is located` 标注。该字段是 LLM 判断告警的核心依据 |

### 参考标签字段（仅 `with_label` 模式存在）

| 字段名 | 类型 | 说明 |
|--------|------|------|
| `label` | `string` | 由**自动版本追踪算法**生成的参考标签，取值为 `"TP"` 或 `"FP"`。判定规则：若告警在后续版本中**消失**则标记为 `TP`（推测已被修复），若**持续存在**则标记为 `FP`（推测开发者认为无需修复）。此标签仅供参考，存在误判可能 |

---

## 四种运行模式说明

本工具支持两个维度的组合，形成四种运行模式：

### 维度一：是否允许 Unknown（`with_unknown` / `without_unknown`）

| 模式 | `llm_label` 取值 | 说明 |
|------|-----------------|------|
| `with_unknown` | `TP` / `FP` / `Unknown` | **三分类模式**。允许 LLM 在证据不足时给出 `Unknown`，表示当前切片信息不足以做出判断 |
| `without_unknown` | `TP` / `FP` | **二分类模式**。强制 LLM 给出明确结论，当信息存在不确定性时，要求 LLM 基于可见证据做出倾向性判断，不允许回避 |

### 维度二：是否提供算法参考标签（`with_label` / `without_label`）

| 模式 | 是否含 `label` 字段 | 说明 |
|------|-------------------|------|
| `with_label` | ✅ 是 | LLM 在分析时**可参考**自动版本追踪算法生成的 `label` 标签，但仍须以代码分析为最终判断依据 |
| `without_label` | ❌ 否 | LLM 在分析时**不提供**算法标签，完全依据 `sliced_code` 进行独立判断，避免算法标签的干扰 |

### 四种模式对应的输出文件

| 模式名称 | 输出文件 | 分类数 | 含参考标签 |
|----------|----------|--------|-----------|
| `with_unknown_with_label` | `results_with_unknown_with_label.json` | 3（TP/FP/Unknown） | ✅ |
| `with_unknown_without_label` | `results_with_unknown_without_label.json` | 3（TP/FP/Unknown） | ❌ |
| `without_unknown_with_label` | `results_without_unknown_with_label.json` | 2（TP/FP） | ✅ |
| `without_unknown_without_label` | `results_without_unknown_without_label.json` | 2（TP/FP） | ❌ |

---

## 快速使用

```bash
# 三分类 + 不含参考标签（最纯粹的 LLM 独立判断）
python llm.py --mode with_unknown_without_label

# 二分类 + 不含参考标签
python llm.py --mode without_unknown_without_label

# 三分类 + 含参考标签
python llm.py --mode with_unknown_with_label

# 二分类 + 含参考标签
python llm.py --mode without_unknown_with_label
```

> 脚本支持**断点续传**，中途中断后重新运行会自动跳过已处理的条目，从断点处继续。
