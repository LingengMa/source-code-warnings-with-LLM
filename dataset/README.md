初始数据条目 -> 55298

- 去除
  - 最后一版本
  - #include
  - test_files
- 仅保留 CWE Top25

最终剩余条目 -> 2510

---

- `data_all_55298.json`: 原始总数据
- `data_with_fcg_and_bfs_55298.json`: 附带 bfs 和 fcg 切片结果的数据 (数据量过大, 放在南大云盘 https://box.nju.edu.cn/f/97ad5420808641e98d50/)
- `data_with_slice_2510.json`: 过滤后使用 joern 切片并且修复得到的数据
- `llm_results_with_annotated_data_1025.json`: 附带四种大模型匹配策略结果, 以及人工标注结果的数据