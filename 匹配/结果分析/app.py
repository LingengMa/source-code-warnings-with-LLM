from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# 定义文件路径
INPUT_JSON = 'output/formatted_inconsistent_labels.json'
OUTPUT_JSON = 'output/manual_labeled_data.json'
PROGRESS_FILE = 'output/progress.json'

# --- 数据加载与保存 ---

def load_source_data():
    """加载原始数据"""
    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_labeled_data():
    """加载已标注的数据到字典中，以ID为键"""
    if not os.path.exists(OUTPUT_JSON):
        return {}
    with open(OUTPUT_JSON, 'r', encoding='utf-8') as f:
        try:
            labeled_list = json.load(f)
            return {item['id']: item for item in labeled_list}
        except (json.JSONDecodeError, TypeError):
            return {}

def save_labeled_data(labeled_dict):
    """将标注数据字典转换回列表并保存"""
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        # 按ID排序，保持文件内容稳定
        sorted_list = sorted(labeled_dict.values(), key=lambda x: x['id'])
        json.dump(sorted_list, f, indent=2, ensure_ascii=False)

def save_progress(index):
    """保存当前浏览的索引"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump({'current_index': index}, f)

def load_progress():
    """加载进度"""
    if not os.path.exists(PROGRESS_FILE):
        return None
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f).get('current_index', 0)
        except json.JSONDecodeError:
            return None

def find_first_unlabeled_index(source, labeled):
    """查找第一个未被标注的条目的索引"""
    for i, item in enumerate(source):
        if item['id'] not in labeled:
            return i
    return 0 # 如果都标完了，从头开始

# --- 初始化 ---

source_data = load_source_data()
labeled_data_dict = load_labeled_data()

# --- 路由 ---

@app.route('/')
def index():
    current_index = load_progress()
    if current_index is None:
        current_index = find_first_unlabeled_index(source_data, labeled_data_dict)
        save_progress(current_index)

    if not 0 <= current_index < len(source_data):
        return "<h1>索引无效。</h1>"
    
    item = source_data[current_index].copy()
    if item['id'] in labeled_data_dict:
        item['manual_label'] = labeled_data_dict[item['id']].get('manual_label')

    return render_template('index.html', item=item, index=current_index, total=len(source_data))

@app.route('/label', methods=['POST'])
def label():
    item_id = int(request.form['id'])
    manual_label = request.form['label']
    current_index = int(request.form.get('current_index', 0))
    
    item_to_label = next((item for item in source_data if item['id'] == item_id), None)
    
    if item_to_label:
        labeled_item = item_to_label.copy()
        labeled_item['manual_label'] = manual_label
        labeled_data_dict[item_id] = labeled_item
        save_labeled_data(labeled_data_dict)
            
    # 自动前进到下一个
    next_index = min(current_index + 1, len(source_data) - 1)
    save_progress(next_index)
    
    return redirect(url_for('index'))

@app.route('/nav', methods=['GET'])
def nav():
    direction = request.args.get('direction')
    current_index = load_progress() or 0
    
    if direction == 'prev':
        current_index = max(0, current_index - 1)
    elif direction == 'next':
        current_index = min(len(source_data) - 1, current_index + 1)
    elif direction == 'first_unlabeled':
        current_index = find_first_unlabeled_index(source_data, labeled_data_dict)

    save_progress(current_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
