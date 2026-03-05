#!/usr/bin/env python3
"""
将 results_filtered.json 均等切分为三份
"""

import json
from pathlib import Path

def split_json(input_file, num_parts=3):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    total = len(data)
    part_size = total // num_parts
    for i in range(num_parts):
        start = i * part_size
        # 最后一份包含剩余所有数据
        end = (i + 1) * part_size if i < num_parts - 1 else total
        part_data = data[start:end]
        out_file = Path(input_file).parent / f"{Path(input_file).stem}_part{i+1}{Path(input_file).suffix}"
        with open(out_file, 'w', encoding='utf-8') as f_out:
            json.dump(part_data, f_out, indent=4, ensure_ascii=False)
        print(f"已写入: {out_file} (条目数: {len(part_data)})")

if __name__ == "__main__":
    split_json("results_filtered.json")
