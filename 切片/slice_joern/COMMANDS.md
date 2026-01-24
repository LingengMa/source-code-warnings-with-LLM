# 命令参考

## 可用命令

### 正常运行 (多进程)
```bash
python single_file_slicer.py
```
- **使用3个进程并行处理**
- 执行切片任务
- 自动断点续传
- 每100个任务保存一个chunk
- **完成后自动合并所有chunk文件**

### 自定义进程数
```bash
# 使用5个进程
python single_file_slicer.py --processes 5

# 使用单进程(禁用多进程)
python single_file_slicer.py --no-multiprocess
```

### 查看进度
```bash
python single_file_slicer.py --progress
```
或使用便捷脚本:
```bash
python show_progress.py
```

### 清除断点
```bash
python single_file_slicer.py --clear
```
- 清除断点和进度信息
- 下次运行从头开始

### 自定义chunk大小
```bash
python single_file_slicer.py --chunk-size 200
```
- 临时设置chunk大小为200
- 不修改配置文件

### 组合使用
```bash
# 清除断点并使用大chunk+更多进程重新运行
python single_file_slicer.py --clear --chunk-size 500 --processes 5

# 清除断点后正常运行
python single_file_slicer.py --clear

# 使用单进程运行(调试时)
python single_file_slicer.py --no-multiprocess
```

## 辅助工具

### 查看详细进度
```bash
python show_progress.py
```

### 测试配置
```bash
python test_checkpoint.py
```

## 后台运行

### 使用nohup
```bash
nohup python single_file_slicer.py > slice.log 2>&1 &
```

### 使用screen (推荐)
```bash
screen -S slicing
python single_file_slicer.py
# 按 Ctrl+A+D 退出
# screen -r slicing 重新连接
```

## 工作流程

```bash
# 1. 首次运行
python single_file_slicer.py

# 2. 查看进度
python show_progress.py

# 3. 如果中断，再次运行自动继续
python single_file_slicer.py

# 4. 完成后查看结果
ls -lh slice_output/slices.json
```

## 注意事项

1. **自动合并**: 无需手动合并chunk文件，程序完成后会自动合并
2. **断点续传**: 中断后直接运行即可继续，无需特殊参数
3. **chunk文件**: 中间chunk文件可以保留作为备份，也可以删除
4. **进度文件**: `checkpoint.json` 和 `progress.json` 不要手动修改
5. **多进程**: 默认使用3进程并行，可通过 `--processes N` 调整
6. **进程数建议**: 根据CPU核心数设置，通常设为核心数的50-80%
7. **内存占用**: 多进程会增加内存占用，每个进程约需500MB
8. **调试模式**: 调试时建议使用 `--no-multiprocess` 单进程运行
