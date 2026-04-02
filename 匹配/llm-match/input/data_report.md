# LLM 分类结果分析报告

- **分析文件**：`data.json`
- **完整路径**：`/home/lg/Documents/projects/毕设/大仓/匹配/llm-match/input/data.json`
- **生成时间**：2026-04-03 00:36:48

---

## 1. 数据总览

| 指标 | 数值 |
|---|---|
| 数据总条数 | 2510 |
| 有效条目数（含 label / llm_label） | 0 |
| 跳过条目数（字段缺失或无效） | 2510 |
| Unknown 条目数 | 0 |
| Unknown 比率 | N/A |
| 已判定条目数（非 Unknown） | 0 |
| 判定一致数 | 0 |
| 判定不一致数 | 0 |

## 2. 算法标注（label）分布

| label | 数量 | 占比 |
|---|---|---|
| TP | 0 | N/A |
| FP | 0 | N/A |

## 3. label × llm_label 交叉矩阵

| label \ llm_label | TP | FP | Unknown | **合计** |
|---|---|---|---|---|
| **TP** | 0 | 0 | 0 | **0** |
| **FP** | 0 | 0 | 0 | **0** |
| **合计** | 0 | 0 | 0 | **0** |

## 4. 汇总指标

> 以下指标仅基于**已判定（非 Unknown）**条目计算。

| 指标 | 数值 |
|---|---|
| 准确率（Accuracy） | N/A |
| 精确率（Precision，以 TP 为正类） | N/A |
| 召回率（Recall，以 TP 为正类） | N/A |
| F1 分数（以 TP 为正类） | N/A |

## 5. 各分类条目详情

### 5.1 一致：算法=TP，LLM=TP（共 0 条）

> 算法与 LLM 均判定为真阳性（True Positive）。

*（无）*

### 5.2 一致：算法=FP，LLM=FP（共 0 条）

> 算法与 LLM 均判定为假阳性（False Positive）。

*（无）*

### 5.3 不一致：算法=TP，LLM=FP（共 0 条）

> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。

*（无）*

### 5.4 不一致：算法=FP，LLM=TP（共 0 条）

> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。

*（无）*

### 5.5 Unknown：算法=TP，LLM=Unknown（共 0 条）

> 算法判定为 TP，LLM 无法判定。

*（无）*

### 5.6 Unknown：算法=FP，LLM=Unknown（共 0 条）

> 算法判定为 FP，LLM 无法判定。

*（无）*

## 6. 按 (tool_name, project_name_without_version, rule_id) 联合分组统计

> 共 **0** 种不同组合（种类），按条目数降序排列。

| # | tool_name | project_name_without_version | rule_id | 总计 | TP | FP | Unknown |
|---|---|---|---|---|---|---|---|

---

*报告由 `analyze_results.py` 自动生成，生成时间：2026-04-03 00:36:48*
