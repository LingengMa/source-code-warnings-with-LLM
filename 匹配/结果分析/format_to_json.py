import json
import os

# 定义输入和输出文件路径
input_json_path = 'input/inconsistent_labels.json'
output_json_path = 'output/formatted_inconsistent_labels.json'
output_dir = os.path.dirname(output_json_path)

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取JSON文件
with open(input_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 格式化 sliced_code 字段
for item in data:
    if 'sliced_code' in item and isinstance(item['sliced_code'], str):
        # 将 sliced_code 字符串按行分割，并去除每行前后的空白
        lines = item['sliced_code'].splitlines()
        stripped_lines = [line.strip() for line in lines]
        # 将 sliced_code 的值更新为字符串列表
        item['sliced_code'] = stripped_lines

# 将格式化后的数据写入新的JSON文件
with open(output_json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"成功将格式化后的数据写入到 {output_json_path}")
