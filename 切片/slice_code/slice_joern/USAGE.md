# 单文件切片器使用指南

## 功能特性

- ✅ **分块保存**: 每处理 N 个任务自动保存一次,避免内存溢出
- ✅ **断点续传**: 程序中断后可从上次位置继续执行
- ✅ **进度跟踪**: 实时保存处理进度和统计信息
- ✅ **错误恢复**: 单个任务失败不影响整体流程

## 配置说明

在 `config.py` 中可以配置以下参数:

```python
CHUNK_SIZE = 100              # 每个chunk保存的任务数(可根据内存调整)
ENABLE_CHECKPOINT = True      # 是否启用断点续传
CHECKPOINT_FILE = "..."       # 断点文件路径
PROGRESS_FILE = "..."         # 进度文件路径
```

## 使用方法

### 1. 正常执行切片任务

```bash
python single_file_slicer.py
```

程序会:
- 自动加载之前的断点(如果存在)
- 跳过已处理的任务
- 每处理 100 个任务保存一个 chunk 文件
- 每处理一个任务更新断点和进度
- **处理完成后自动合并所有 chunk 文件**

### 2. 查看当前进度

```bash
python single_file_slicer.py --progress
```

输出示例:
```
Current Progress:
  Processed: 1234/50000
  Progress: 2.5%
  Success: 1150
  Failed: 84
  Last Update: 2026-01-24T15:30:45.123456
```

### 3. 清除断点重新开始

```bash
python single_file_slicer.py --clear
```

**⚠️ 注意**: 这不会删除已保存的 chunk 文件,只会清除断点信息,下次运行会从头开始处理所有任务。

### 4. 自定义 chunk 大小

```bash
python single_file_slicer.py --chunk-size 200
```

将 chunk 大小临时设置为 200(不修改配置文件)。

### 5. 组合使用

```bash
# 清除断点并使用更大的chunk重新开始
python single_file_slicer.py --clear --chunk-size 500
```

## 输出文件说明

### Chunk 文件 (处理过程中)

```
slice_output/
├── slices_chunk_0001.json          # 第1个chunk (1-100)
├── slices_chunk_0001_summary.json  # 第1个chunk的摘要
├── slices_chunk_0002.json          # 第2个chunk (101-200)
├── slices_chunk_0002_summary.json
├── ...
├── checkpoint.json                 # 断点文件
└── progress.json                   # 进度文件
```

### 最终合并文件

```
slice_output/
├── slices.json          # 所有结果合并后的完整文件
└── slices_summary.json  # 合并后的摘要文件
```

## 断点续传机制

### 工作原理

1. **checkpoint.json** 记录:
   - `processed_indices`: 已处理任务的索引列表
   - `chunk_count`: 已保存的 chunk 数量

2. **progress.json** 记录:
   - 当前处理的任务索引
   - 总任务数
   - 成功/失败统计
   - 进度百分比
   - 最后更新时间

3. 程序启动时:
   - 自动加载 checkpoint
   - 跳过所有已处理的任务
   - 从下一个未处理的任务继续

### 中断恢复场景

#### 场景 1: 正常中断 (Ctrl+C)

```bash
# 第一次运行 (处理了 1500 个任务后中断)
python single_file_slicer.py
^C
Interrupted by user
Progress has been saved. Run again to resume from checkpoint.

# 直接再次运行,自动从第 1501 个任务继续
python single_file_slicer.py
Resuming from checkpoint: 1500 tasks already processed
```

#### 场景 2: 程序崩溃

程序崩溃前已保存的进度不会丢失,重新运行即可继续。

#### 场景 3: 机器重启

所有进度保存在文件中,机器重启后可继续执行。

## 性能优化建议

### 针对 5 万+任务的建议

1. **chunk 大小设置**:
   - 内存充足: `CHUNK_SIZE = 500`
   - 内存有限: `CHUNK_SIZE = 50` 或 `100`
   - 推荐值: `100-200`

2. **磁盘空间**:
   - 每个 chunk 约 10-50 MB (取决于代码复杂度)
   - 5 万任务预计需要 2-10 GB 存储空间

3. **执行时间估算**:
   - 单任务平均 5-10 秒
   - 5 万任务预计 70-140 小时
   - **建议**: 使用 screen/tmux 在后台运行

4. **后台运行**:
   ```bash
   # 使用 nohup
   nohup python single_file_slicer.py > slice.log 2>&1 &
   
   # 或使用 screen
   screen -S slicing
   python single_file_slicer.py
   # Ctrl+A+D 退出 screen
   # screen -r slicing 重新连接
   ```

## 常见问题

### Q: chunk 文件太大,能否减小?

A: 减小 `CHUNK_SIZE` 配置值,例如设置为 50。

### Q: 如何删除所有输出重新开始?

A: 
```bash
# 删除所有输出
rm -rf slice_output/*
# 然后重新运行
python single_file_slicer.py
```

### Q: 部分 chunk 文件损坏怎么办?

A: 
1. 删除损坏的 chunk 文件
2. 编辑 `checkpoint.json`,删除对应的已处理索引
3. 重新运行程序

### Q: 如何查看某个具体 chunk 的内容?

A: 
```bash
# 查看第 10 个 chunk 的摘要
cat slice_output/slices_chunk_0010_summary.json | jq
```

### Q: 进度显示不准确?

A: 检查 `progress.json` 文件,确保内容格式正确。如果损坏,删除该文件重新运行。

## 监控脚本示例

创建一个简单的监控脚本 `monitor.sh`:

```bash
#!/bin/bash
# 每 60 秒显示一次进度

while true; do
    clear
    echo "==================== Slicing Progress ===================="
    python single_file_slicer.py --progress
    echo "========================================================="
    sleep 60
done
```

使用方法:
```bash
chmod +x monitor.sh
./monitor.sh
```

## 数据恢复

所有数据都保存在 JSON 文件中,即使程序完全失败,也可以手动合并 chunk 文件:

```python
import json
import glob

chunks = sorted(glob.glob('slice_output/slices_chunk_*.json'))
all_data = []

for chunk_file in chunks:
    if '_summary' not in chunk_file:
        with open(chunk_file) as f:
            all_data.extend(json.load(f))

with open('slice_output/slices.json', 'w') as f:
    json.dump(all_data, f, indent=2)

print(f"Merged {len(all_data)} results")
```
