import json

# 定义输入文件路径
input_json_path = 'input/inconsistent_labels.json'

# 初始化计数器
tp_fp_count = 0
fp_tp_count = 0

# 读取JSON文件
with open(input_json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 遍历数据并进行统计
for item in data:
    llm_label = item.get('llm_label')
    label = item.get('label')

    if llm_label == 'TP' and label == 'FP':
        tp_fp_count += 1
    elif llm_label == 'FP' and label == 'TP':
        fp_tp_count += 1

# 打印结果
print(f"llm_label为'TP'且label为'FP'的数量: {tp_fp_count}")
print(f"llm_label为'FP'且label为'TP'的数量: {fp_tp_count}")
