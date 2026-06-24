import json
import pandas as pd
import os

# 定义输入和输出文件路径
input_json_path = 'input/inconsistent_labels.json'
output_excel_path = 'output/formatted_inconsistent_labels.xlsx'
output_dir = os.path.dirname(output_excel_path)

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取JSON文件
with open(input_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 格式化 sliced_code 字段
for item in data:
    if 'sliced_code' in item and isinstance(item['sliced_code'], str):
        # 移除每行前后的空白符，然后重新组合
        lines = item['sliced_code'].strip().split('\n')
        stripped_lines = [line.strip() for line in lines]
        item['sliced_code'] = '\n'.join(stripped_lines)

# 将数据转换为pandas DataFrame
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件
df.to_excel(output_excel_path, index=False)

print(f"成功将格式化后的数据写入到 {output_excel_path}")
