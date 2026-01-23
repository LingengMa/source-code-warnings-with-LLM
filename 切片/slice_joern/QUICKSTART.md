# 分Chunk保存和断点续传功能 - 快速上手

## 🚀 快速开始

### 正常运行 (完成后自动合并chunk)
```bash
python single_file_slicer.py
```

### 查看进度
```bash
python show_progress.py
# 或
python single_file_slicer.py --progress
```

### 中断后继续
```bash
# 直接再次运行即可，会自动从断点继续
python single_file_slicer.py
```

### 重新开始
```bash
python single_file_slicer.py --clear
```

## 📊 主要功能

| 功能 | 说明 | 命令 |
|------|------|------|
| 分块保存 | 每处理100个任务保存一次 | 自动执行 |
| 断点续传 | 中断后自动继续 | 自动检测 |
| 进度跟踪 | 实时保存进度信息 | `--progress` |
| 自动合并 | 全部完成后自动合并chunk | 自动执行 |
| 清除断点 | 重新开始处理 | `--clear` |
| 自定义chunk | 修改chunk大小 | `--chunk-size N` |

## 📁 输出文件结构

```
slice_output/
├── slices_chunk_0001.json          # ← Chunk数据文件
├── slices_chunk_0001_summary.json  # ← Chunk摘要
├── slices_chunk_0002.json
├── slices_chunk_0002_summary.json
├── ...
├── checkpoint.json                 # ← 断点文件 (记录已处理任务)
├── progress.json                   # ← 进度文件 (统计信息)
├── slices.json                     # ← 最终合并结果
└── slices_summary.json             # ← 最终摘要
```

## ⚙️ 配置选项 (config.py)

```python
CHUNK_SIZE = 100              # 每个chunk的大小
ENABLE_CHECKPOINT = True      # 启用断点续传
ENABLE_AST_FIX = True        # 启用AST增强
```

## 🔧 常用操作

### 1. 后台运行 (推荐)
```bash
nohup python single_file_slicer.py > slice.log 2>&1 &
```

### 2. 监控日志
```bash
tail -f slice.log
```

### 3. 查看进度
```bash
python show_progress.py
```

### 4. 测试配置
```bash
python test_checkpoint.py
```

## 💡 最佳实践

### 针对5万+任务

1. **设置合适的chunk大小**
   - 内存充足: 200-500
   - 内存有限: 50-100
   
2. **使用后台运行**
   ```bash
   screen -S slicing
   python single_file_slicer.py
   # Ctrl+A+D 退出
   ```

3. **定期检查进度**
   ```bash
   screen -r slicing  # 重新连接查看
   # 或在另一个终端
   python show_progress.py
   ```

4. **预留足够磁盘空间**
   - 5万任务约需 2-10 GB

## 🐛 故障排除

### 问题: chunk文件太大
```bash
# 在 config.py 中减小 CHUNK_SIZE
CHUNK_SIZE = 50
```

### 问题: 想重新开始
```bash
# 清除断点
python single_file_slicer.py --clear
```

### 问题: 部分chunk损坏
```bash
# 删除损坏的chunk文件
rm slice_output/slices_chunk_00XX.json
# 编辑 checkpoint.json 删除对应索引
# 重新运行
python single_file_slicer.py
```

### 问题: 进度显示异常
```bash
# 删除进度文件重新生成
rm slice_output/progress.json
```

## 📈 性能参考

- 单任务处理时间: 5-10秒
- 5万任务预计时间: 70-140小时
- 内存占用: < 500MB (使用分chunk)
- 磁盘占用: 2-10GB (5万任务)

## 🎯 典型工作流

```bash
# 1. 第一次运行
python single_file_slicer.py

# 2. 中断 (Ctrl+C 或关机)
^C

# 3. 查看已完成进度
python show_progress.py

# 4. 继续运行 (自动从断点继续)
python single_file_slicer.py

# 5. 完成后查看结果
ls -lh slice_output/slices.json
cat slice_output/slices_summary.json | jq
```

## 📚 更多信息

- 详细文档: [USAGE.md](USAGE.md)
- 主文档: [README.md](README.md)
