"""
合并人工标注结果 (annotations.json) 和 data.json，
将 manual_annotation、annotation_reason、annotation_timestamp 字段写入每条记录，
输出到 output/annotated_data.json。
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data.json"
ANNOTATIONS_FILE = BASE_DIR / "annotations.json"
OUTPUT_FILE = BASE_DIR / "output" / "annotated_data.json"


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    with open(ANNOTATIONS_FILE, encoding="utf-8") as f:
        annotations = json.load(f)

    annotated = unannotated = 0
    for record in data:
        ann = annotations.get(str(record["id"]))
        if ann:
            record["manual_annotation"] = ann["label"]
            record["annotation_reason"] = ann.get("reason", "")
            record["annotation_timestamp"] = ann.get("timestamp", "")
            annotated += 1
        else:
            record["manual_annotation"] = None
            record["annotation_reason"] = None
            record["annotation_timestamp"] = None
            unannotated += 1

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成：共 {len(data)} 条记录，{annotated} 条已标注，{unannotated} 条未标注")
    print(f"输出文件：{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
