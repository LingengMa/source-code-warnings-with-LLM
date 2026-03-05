"""
将 data copy.json 中的 file_path 添加到 llm_results.json 对应条目中，
并添加 full_file_path 字段：input/repository/{project_name_with_version}/{file_path}
"""

import json

DATA_FILE = "input/data copy.json"
LLM_FILE = "input/llm_results.json"
OUTPUT_FILE = "input/llm_results.json"  # 原地覆盖，如需备份可改为其他路径

# 读取数据
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(LLM_FILE, "r", encoding="utf-8") as f:
    llm_results = json.load(f)

# 构建 id -> {file_path, project_name_with_version} 的映射
id_map = {
    item["id"]: {
        "file_path": item["file_path"],
        "project_name_with_version": item["project_name_with_version"],
    }
    for item in data
}

# 统计
updated = 0
not_found = 0

for entry in llm_results:
    entry_id = entry.get("id")
    if entry_id in id_map:
        file_path = id_map[entry_id]["file_path"]
        project_name_with_version = id_map[entry_id]["project_name_with_version"]
        entry["file_path"] = file_path
        entry["full_file_path"] = f"input/repository/{project_name_with_version}/{file_path}"
        updated += 1
    else:
        print(f"[警告] llm_results 中 id={entry_id} 在 data 中未找到对应记录")
        not_found += 1

# 写回
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(llm_results, f, ensure_ascii=False, indent=2)

print(f"完成！共更新 {updated} 条记录，{not_found} 条未匹配。")
print(f"结果已写入：{OUTPUT_FILE}")
