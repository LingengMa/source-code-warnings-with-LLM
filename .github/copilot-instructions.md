# Copilot Instructions

This is a research monorepo for a graduation thesis on **automated classification of static analysis warnings** (TP/FP) using LLM and version-tracking algorithms.

## Architecture Overview

The pipeline flows through four stages:

```
数据/预处理  →  切片  →  匹配/匹配  →  匹配/llm-match  →  匹配/结果分析
(preprocess)   (slice)  (version-track)   (LLM classify)   (annotate/analyze)
```

**数据/预处理**: Aggregates raw reports from static analysis tools (CodeQL `.sarif`, CSA `index.html`, Semgrep `.json`) into a unified `results.json`. Scripts: `aggregate_results.py` → `analyze_results.py` → `cwe_analysis.py`.

**切片/slice_code**: Extracts program slices (data/control flow) around each warning using tree-sitter (`slice/`) or Joern PDG (`slice_joern/`). Produces `sliced_code` field containing relevant code with the warning line marked as `// The line where the warning is located`.

**匹配/匹配**: Cross-version warning lifecycle tracker. `tracker.py` drives `match.py` (the `Matcher` class) to label each warning as TP/FP/Unknown based on whether it disappears in later versions. Source repos live at `input/repository/{project_name_with_version}/{file_path}`.

**匹配/llm-match**: Sends sliced warnings to the DeepSeek API (`deepseek-chat` model) for classification. Uses `DEEPSEEK_API_KEY` env var. Supports resume on interruption.

**匹配/结果分析**: Flask web app (`app.py`) for manual annotation at `http://localhost:5000`. Reads `inconsistent_labels.json`, writes to `annotations.json`.

## Key Data Schema

All data flows as JSON arrays. Core warning fields:

| Field | Description |
|-------|-------------|
| `id` | Global auto-increment integer |
| `tool_name` | `"codeql"`, `"csa"`, `"semgrep"`, etc. |
| `project_name_with_version` | e.g. `"ffmpeg-6.1.1"` |
| `file_path` | Relative path from project root |
| `full_file_path` | `input/repository/{project_name_with_version}/{file_path}` |
| `sliced_code` | Code slice with warning line annotated |
| `label` | Algorithm-generated: `"TP"` / `"FP"` / `"Unknown"` |
| `llm_label` | LLM output: `"TP"` / `"FP"` / `"Unknown"` |
| `manual_annotation` | Human label from annotation tool |

## Running Key Scripts

```bash
# 1. Preprocess: aggregate static analysis reports
cd 数据/预处理
python aggregate_results.py   # → results.json
python analyze_results.py     # → warnings_analysis.md
python cwe_analysis.py        # → cwe_analysis_report.md

# 2. Version-tracking matcher
cd 匹配/匹配
python tracker.py             # reads input/data.json, outputs labeled JSON

# 3. LLM classification (requires DEEPSEEK_API_KEY)
cd 匹配/llm-match
python llm.py --mode with_unknown_without_label    # 3-class, no reference label
python llm.py --mode without_unknown_without_label # 2-class, no reference label
python llm.py --mode with_unknown_with_label       # 3-class, with reference label
python llm.py --mode without_unknown_with_label    # 2-class, with reference label

# 4. Manual annotation web app (匹配/人工标注)
cd 匹配/人工标注
python prepare_data.py        # merge + filter → data.json (1025 records)
cd src
pip install -r requirements.txt
python app.py                 # → http://localhost:5000

# 5. Slicing (tree-sitter based)
cd 切片/slice_code/slice
pip install -r requirements.txt
```

## LLM Classification Modes

Two independent dimensions combine into 4 modes:
- **with/without_unknown**: whether LLM can output `"Unknown"` (3-class) or must choose TP/FP (2-class)
- **with/without_label**: whether the algorithm-generated `label` is provided to the LLM as a hint

## Matcher Algorithm (`匹配/匹配/match.py`)

Four-tier progressive matching (highest to lowest priority):
1. **Exact**: same file + same line number
2. **Location**: diff-based relative position within `MATCHING_THRESHOLD=3` lines
3. **Snippet**: `SequenceMatcher` similarity ≥ `SNIPPET_SIMILARITY=0.8` on ±`CONTEXT_LINES=2` context
4. **Hash**: MD5 of first/last `HASH_SIZE=30` tokens (tolerates variable renaming)

TP = warning disappears in all subsequent versions (assumed fixed).  
FP = warning persists in subsequent versions (assumed noise).  
Unknown = warning is from the last tracked version.

## Current Work Area: `匹配/人工标注`

Active stage 3 (manual annotation web app). Full functional requirements in `docs/需求分析.md`.

```
匹配/人工标注/
├── README.md              # Task spec — only file edited at root; all other docs go in docs/
├── docs/
│   ├── Prompt.md          # Project background and task description
│   └── 需求分析.md        # Full functional requirements (FR-1 through FR-13)
├── src/                   # Web app code lives here
└── input/
    ├── origin_data/       # base_data.json + 4 LLM result JSONs + per-file reports
    └── repository/        # Source repos: {project_name_with_version}/ (curl, ffmpeg, git, libuv…)
```

**`input/origin_data/` files** (2510 records each):
- `base_data.json` — complete warning info; `label` field is the algorithm result
- `results_with_unknown_with_label.json` — LLM 3-class, with algorithm label hint
- `results_with_unknown_without_label.json` — LLM 3-class, no hint
- `results_without_unknown_with_label.json` — LLM 2-class, with hint
- `results_without_unknown_without_label.json` — LLM 2-class, no hint

**Data preprocessing** (`prepare_data.py` at root of this dir):
- Merges `base_data.json` with the 4 LLM JSONs by `id`
- Filters to warnings where the 5 labels (1 algorithm + 4 LLM) are **not all identical** (~1025 of 2510)
- Outputs `data.json` — the working dataset for the annotation app

**Merged `data.json` record shape:**
```json
{
  "id": 4,
  "tool_name": "codeql",
  "project_name_with_version": "ffmpeg-6.1.1",
  "file_path": "libavcodec/x86/snowdsp.c",
  "line_number": 80,
  "cwe": ["CWE-120"],
  "rule_id": "...",
  "message": "...",
  "label": "FP",
  "llm_results": {
    "wuwl": {"llm_label": "TP", "llm_label_reason": "...", "mode_desc": "三分类+含算法标签"},
    "wuol": {"llm_label": "FP", "llm_label_reason": "...", "mode_desc": "三分类+不含算法标签"},
    "ouwl": {"llm_label": "TP", "llm_label_reason": "...", "mode_desc": "二分类+含算法标签"},
    "ouol": {"llm_label": "FP", "llm_label_reason": "...", "mode_desc": "二分类+不含算法标签"}
  },
  "sliced_code": "..."
}
```

**Source file lookup:** `input/repository/{project_name_with_version}/{file_path}`

**Web app** (Flask, to be built in `src/`):
- Serves the 1025 inconsistent warnings for human review
- `annotations.json` stores labels: `{"4": {"label": "TP", "timestamp": "..."}}`
- Keyboard shortcuts: `A`/`D` = prev/next, `T`/`F`/`U` = label, `N` = next unannotated, `Delete` = remove label
- `file_path` is clickable → shows full source file with `line_number` highlighted
- Export adds `manual_annotation` + `annotation_timestamp` fields to each record

## Environment

- **Active conda env**: `conda activate slice` (use this for all scripts in this repo)
- LLM API: DeepSeek (`DEEPSEEK_API_KEY` env var), OpenAI-compatible client (`base_url=https://api.deepseek.com`, model `deepseek-chat`)
- Static analysis tools: CodeQL, CSA (scan-build), Semgrep, CppCheck, SpotBugs
- Slicing tools: tree-sitter (C/C++), Joern (PDG-based)
- CWE mapping data in `映射/` as Excel files
- Root-level `llm_match_output_1/` contains early LLM output (`llm_results.json`, `llm_results_with_labels.json`)
