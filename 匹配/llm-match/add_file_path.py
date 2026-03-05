"""
将 data.json 中的 file_path 添加到 output 目录下四种结果文件的对应条目中，
并添加 full_file_path 字段：input/repository/{project_name_with_version}/{file_path}
结果按原文件名原地写回。
"""

import json
import os

DATA_FILE = "input/data.json"

OUTPUT_FILES = [
    "output/results_with_unknown_without_label.json",
    "output/results_without_unknown_without_label.json",
    "output/results_with_unknown_with_label.json",
    "output/results_without_unknown_with_label.json",
]

# 读取 data.json，构建 id -> {file_path, project_name_with_version} 的映射
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

id_map = {
    item["id"]: {
        "file_path": item["file_path"],
        "project_name_with_version": item["project_name_with_version"],
    }
    for item in data
}

# 逐一处理每个输出文件
for output_filepath in OUTPUT_FILES:
    if not os.path.exists(output_filepath):
        print(f"[跳过] 文件不存在：{output_filepath}")
        continue

    with open(output_filepath, "r", encoding="utf-8") as f:
        results = json.load(f)

    updated = 0
    not_found = 0

    for entry in results:
        entry_id = entry.get("id")
        if entry_id in id_map:
            file_path = id_map[entry_id]["file_path"]
            project_name_with_version = id_map[entry_id]["project_name_with_version"]
            entry["file_path"] = file_path
            entry["full_file_path"] = f"input/repository/{project_name_with_version}/{file_path}"
            updated += 1
        else:
            print(f"  [警告] id={entry_id} 在 data.json 中未找到对应记录")
            not_found += 1

    with open(output_filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"[完成] {output_filepath}：更新 {updated} 条，未匹配 {not_found} 条")
