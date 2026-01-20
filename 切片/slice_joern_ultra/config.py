"""
配置文件
"""
import os

# 路径配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "slice_input")
OUTPUT_DIR = os.path.join(BASE_DIR, "slice_output")
REPOSITORY_DIR = os.path.join(INPUT_DIR, "repository")
CPG_DIR = os.path.join(INPUT_DIR, "cpg")
PDG_DIR = os.path.join(INPUT_DIR, "pdg")

# 数据文件
DATA_JSON = os.path.join(INPUT_DIR, "data.json")
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "slices.json")

# 切片参数
BACKWARD_DEPTH = 4  # 后向切片深度
FORWARD_DEPTH = 4   # 前向切片深度
MIN_SLICE_LINES = 5  # 最小切片行数（少于此数则包含整个函数）

# AST 修复配置
ENABLE_AST_FIX = True  # 是否启用 AST 语法修复
LANGUAGE = "c"  # 默认语言

# 输出配置
OUTPUT_FORMAT = "json"  # json 或 markdown
VERBOSE = True  # 是否输出详细日志

# PDG 边类型
DDG_LABEL = "DDG"  # 数据依赖边
CDG_LABEL = "CDG"  # 控制依赖边
CFG_LABEL = "CFG"  # 控制流边

# 占位符
PLACEHOLDER = "    /* PLACEHOLDER: Code omitted for brevity */"

# Joern
JOERN_PATH = "/opt/joern-cli"

# Tree-sitter
TREE_SITTER_SO_FILE = "build/c.so"

# Slicing
FORWARD_SLICE = True
