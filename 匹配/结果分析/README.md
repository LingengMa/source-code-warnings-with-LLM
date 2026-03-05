# 警告标注工具

一个基于 Flask 的 Web 应用，用于对静态分析工具的警告进行人工标注。

## 功能特性

- ✅ **浏览警告**: 查看详细的警告信息、代码片段、LLM分析等
- 🏷️ **标注功能**: 将警告标注为 TP（真阳性）、FP（假阳性）或 Unknown
- ⌨️ **快捷键支持**: 支持键盘快捷键快速操作
- 💾 **持久化存储**: 标注数据保存到本地 JSON 文件
- 📊 **统计信息**: 实时显示标注进度和统计数据
- 📥 **导出功能**: 导出包含标注的完整数据

## 安装

1. 安装依赖:
```bash
pip install -r requirements.txt
```

## 使用方法

1. 启动服务:
```bash
python app.py
```

2. 打开浏览器访问:
```
http://localhost:5000
```

3. 开始标注！

## 快捷键

- `A` - 上一个警告
- `D` - 下一个警告
- `T` - 标记为 TP（真阳性）
- `F` - 标记为 FP（假阳性）
- `U` - 标记为 Unknown
- `N` - 跳到下一个未标注的警告
- `Delete` - 删除当前标注

## API 接口

### 获取所有警告
```
GET /api/warnings
```

### 获取所有标注
```
GET /api/annotations
```

### 添加/更新标注
```
POST /api/annotate
Body: {
    "id": 1,
    "label": "TP"
}
```

### 删除标注
```
DELETE /api/delete_annotation/<warning_id>
```

### 导出数据
```
GET /api/export
```

### 获取统计信息
```
GET /api/stats
```

## 文件说明

- `app.py` - Flask 应用主文件
- `templates/index.html` - Web 界面模板
- `inconsistent_labels.json` - 原始警告数据
- `annotations.json` - 标注数据（自动生成）
- `requirements.txt` - Python 依赖

## 数据格式

### 标注数据格式 (annotations.json)
```json
{
  "1": {
    "label": "TP",
    "timestamp": "2026-02-03T12:00:00"
  },
  "2": {
    "label": "FP",
    "timestamp": "2026-02-03T12:01:00"
  }
}
```

### 导出数据格式
导出的 JSON 文件会在每条警告中添加以下字段:
- `manual_annotation` - 人工标注的标签
- `annotation_timestamp` - 标注时间

## 注意事项

- 标注数据会自动保存到 `annotations.json` 文件
- 请定期备份标注数据
- 导出的文件会保存到系统临时目录
