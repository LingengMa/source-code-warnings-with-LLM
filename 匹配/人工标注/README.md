# 人工标注工具

静态分析告警人工标注 Web 应用，用于对五套标签（算法 + 4 种 LLM 模式）存在分歧的告警进行人工审核。

## 快速开始

```bash
conda activate slice

# 1. 生成待标注数据（首次运行，或输入数据更新后）
python prepare_data.py   # → data.json（约 1025 条）

# 2. 启动 Web 服务
cd src
pip install -r requirements.txt   # 首次安装
python app.py                      # → http://localhost:5000
```

## 快捷键

| 键 | 功能 |
|----|------|
| `A` | 上一条告警 |
| `D` | 下一条告警 |
| `N` | 跳至下一个未标注 |
| `T` | 标注为 TP |
| `F` | 标注为 FP |
| `U` | 标注为 Unknown |
| `Delete` | 删除当前标注 |
| `Esc` | 关闭源文件弹窗 |

## 文件说明

| 文件/目录 | 说明 |
|-----------|------|
| `prepare_data.py` | 数据预处理：合并五套标签，筛选不一致条目 |
| `data.json` | 预处理输出，供 Web 应用使用（自动生成） |
| `annotations.json` | 标注结果，自动持久化（自动生成） |
| `src/app.py` | Flask 后端 |
| `src/templates/index.html` | 前端页面 |
| `input/origin_data/` | 原始输入数据（base_data + 4 个 LLM 结果） |
| `input/repository/` | 源代码仓库，用于查看源文件 |
| `docs/` | 项目文档（需求分析等） |
