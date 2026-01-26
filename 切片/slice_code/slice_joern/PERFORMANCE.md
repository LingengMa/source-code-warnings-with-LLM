# 多进程性能说明

## 性能对比

### 处理5万条任务的预计时间

| 模式 | 进程数 | 每任务耗时 | 总耗时 | 加速比 | 内存占用 |
|------|--------|------------|--------|--------|----------|
| 单进程 | 1 | 10秒 | 139小时 | 1x | 500MB |
| 多进程 | 2 | 10秒 | 70小时 | 2x | 1GB |
| **多进程(默认)** | **3** | **10秒** | **47小时** | **3x** | **1.5GB** |
| 多进程 | 4 | 10秒 | 35小时 | 4x | 2GB |
| 多进程 | 5 | 10秒 | 28小时 | 5x | 2.5GB |

**注意**: 实际加速比取决于:
- CPU核心数和性能
- 磁盘I/O速度 (Joern大量读写临时文件)
- 内存大小
- 系统负载

## 推荐配置

### 根据CPU核心数

| CPU核心数 | 推荐进程数 | 说明 |
|-----------|------------|------|
| 2核 | 1-2 | 建议单进程或2进程 |
| 4核 | 2-3 | 默认3进程即可 |
| 6核 | 3-4 | 可以使用4进程 |
| 8核+ | 3-5 | 推荐3-5进程,更多不一定更快 |

### 根据内存大小

| 内存 | 推荐进程数 | 说明 |
|------|------------|------|
| 4GB | 1-2 | 建议单进程 |
| 8GB | 2-3 | 默认配置 |
| 16GB+ | 3-5 | 可以使用更多进程 |

## 使用建议

### 1. 首次运行 - 使用默认配置
```bash
python single_file_slicer.py
```
默认使用3进程,适合大多数场景。

### 2. 高性能服务器 - 增加进程数
```bash
# 8核CPU, 16GB内存
python single_file_slicer.py --processes 5
```

### 3. 低配机器 - 减少进程数
```bash
# 4核CPU, 8GB内存
python single_file_slicer.py --processes 2

# 或使用单进程
python single_file_slicer.py --no-multiprocess
```

### 4. 调试模式 - 单进程
```bash
python single_file_slicer.py --no-multiprocess
```
单进程便于查看日志和调试问题。

## 性能优化tips

### 1. 磁盘I/O优化
- 使用SSD而非HDD
- 确保有足够的磁盘空间 (至少20GB)
- 避免在磁盘I/O繁忙时运行

### 2. CPU优化
- 关闭其他占用CPU的程序
- 确保散热良好,避免降频
- 不要设置过多进程数 (通常3-5个最优)

### 3. 内存优化
- 监控内存使用,避免swap
- 可以适当减小CHUNK_SIZE以降低内存峰值

### 4. 后台运行
```bash
# 使用screen避免SSH断开
screen -S slicing
python single_file_slicer.py --processes 3
# Ctrl+A+D 退出
```

## 监控性能

### 使用htop监控
```bash
htop
```
观察:
- CPU使用率 (应该接近进程数×100%)
- 内存使用 (不应接近总内存)
- Load Average (不应超过CPU核心数太多)

### 查看进度
```bash
# 每60秒刷新一次
watch -n 60 python show_progress.py
```

### 估算完成时间
根据进度文件中的速度估算:
```python
import json
with open('slice_output/progress.json') as f:
    p = json.load(f)
remaining = p['total_tasks'] - p['processed']
# 根据当前速度估算
```

## 故障排查

### CPU占用过低
- 可能I/O瓶颈,检查磁盘速度
- 可能进程数太少,尝试增加

### 内存占用过高
- 减少进程数
- 减小CHUNK_SIZE

### 进程卡住
- 检查是否有任务特别耗时
- 查看日志找出问题任务
- 考虑设置任务超时机制

### 速度没有提升
- 检查是否I/O瓶颈 (使用iostat)
- 尝试不同的进程数
- 确认CPU没有被其他程序占用
