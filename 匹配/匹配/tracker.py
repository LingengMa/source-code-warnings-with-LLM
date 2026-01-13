import json
import os
from collections import defaultdict
from packaging.version import parse as parse_version
from match import Matcher

class LifecycleTracker:
    """
    负责追踪告警生命周期，并根据匹配结果标注其状态 (TP/FP/Unknown)。
    """
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file
        self.matcher = Matcher()
        self.all_warnings = self._load_warnings()
        self.warnings_by_project = self._group_and_sort_warnings()

    def _load_warnings(self) -> list:
        """从 JSON 文件加载告警数据。"""
        print(f"正在从 {self.input_file} 加载告警数据...")
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"成功加载 {len(data)} 条告警。")
                return data
        except FileNotFoundError:
            print(f"错误: 输入文件未找到 {self.input_file}")
            return []
        except json.JSONDecodeError:
            print(f"错误: 无法解析JSON文件 {self.input_file}")
            return []

    def _group_and_sort_warnings(self) -> defaultdict:
        """按项目分组并按版本排序告警。"""
        warnings_by_project = defaultdict(lambda: defaultdict(list))
        for warning in self.all_warnings:
            warnings_by_project[warning['project_name']][warning['project_version']].append(warning)

        # 对每个项目中的版本进行排序
        sorted_projects = defaultdict(dict)
        for project, versions in warnings_by_project.items():
            sorted_version_keys = sorted(versions.keys(), key=parse_version)
            sorted_versions = {key: versions[key] for key in sorted_version_keys}
            sorted_projects[project] = sorted_versions
            
        return sorted_projects

    def run(self):
        """执行告警生命周期追踪和标注。"""
        if not self.all_warnings:
            print("没有告警数据可处理。")
            return

        labeled_warnings = []
        
        # 用于存储已处理过的告警ID，避免重复处理
        processed_warnings = set()

        for project, versions in self.warnings_by_project.items():
            print(f"\n正在处理项目: {project}")
            sorted_versions = list(versions.keys())
            num_versions = len(sorted_versions)

            # 迭代处理每个版本 (除了最后一个)
            for i in range(num_versions):
                current_version = sorted_versions[i]
                current_warnings = versions[current_version]
                
                print(f"  - 版本 {current_version} ({len(current_warnings)} 条告警)")

                # 如果是最新版本，所有告警都标记为 Unknown
                if i == num_versions - 1:
                    for warning in current_warnings:
                        if warning['id'] not in processed_warnings:
                            warning['label'] = 'Unknown'
                            labeled_warnings.append(warning)
                            processed_warnings.add(warning['id'])
                    continue

                # 对当前版本的每个告警进行处理
                for warning in current_warnings:
                    if warning['id'] in processed_warnings:
                        continue

                    is_fp = False
                    # 将当前告警与所有后续版本进行匹配
                    for j in range(i + 1, num_versions):
                        next_version = sorted_versions[j]
                        next_warnings = versions[next_version]
                        
                        # 调用匹配器
                        match_result = self.matcher.match_warnings_between_versions([warning], next_warnings)
                        
                        # 如果在任何一个后续版本中找到了匹配，则为 FP
                        if match_result['matched_pairs']:
                            is_fp = True
                            break # 无需再与更后面的版本比较
                    
                    # 根据匹配结果确定标签
                    if is_fp:
                        warning['label'] = 'FP'
                    else:
                        warning['label'] = 'TP'
                    
                    labeled_warnings.append(warning)
                    processed_warnings.add(warning['id'])

        self.save_results(labeled_warnings)

    def save_results(self, labeled_warnings: list):
        """将标注好的结果保存到输出文件。"""
        # 确保输出目录存在
        output_dir = os.path.dirname(self.output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print(f"\n正在将 {len(labeled_warnings)} 条已标注的告警保存到 {self.output_file}...")
        
        # 为了保持与输入数据一致的顺序，我们创建一个ID到标签的映射
        label_map = {w['id']: w['label'] for w in labeled_warnings}
        
        final_output = []
        for original_warning in self.all_warnings:
            if original_warning['id'] in label_map:
                new_warning = original_warning.copy()
                new_warning['label'] = label_map[original_warning['id']]
                final_output.append(new_warning)

        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(final_output, f, indent=4, ensure_ascii=False)
        
        print("保存成功。")
        self._print_stats(final_output)

    def _print_stats(self, final_output: list):
        """打印最终的统计信息。"""
        stats = defaultdict(int)
        for warning in final_output:
            stats[warning['label']] += 1
        
        total = len(final_output)
        print("\n--- 最终统计 ---")
        print(f"总告警数: {total}")
        for label, count in stats.items():
            percentage = (count / total) * 100 if total > 0 else 0
            print(f"  - {label}: {count} ({percentage:.2f}%)")
        print("------------------")


if __name__ == "__main__":
    # 确保我们从项目的根目录运行
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    input_json = os.path.join(base_dir, 'input', 'data_with_id.json')
    output_json = os.path.join(base_dir, 'output', 'data_labeled.json')

    # 安装依赖
    try:
        import packaging
    except ImportError:
        print("正在安装所需的 'packaging' 库...")
        os.system('pip install packaging')

    tracker = LifecycleTracker(input_file=input_json, output_file=output_json)
    tracker.run()
