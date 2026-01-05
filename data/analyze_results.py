import json
from collections import defaultdict
import os

def analyze_results(file_path):
    """
    分析缺陷结果 JSON 文件并生成报告。

    Args:
        file_path (str): results.json 文件的路径。
    """
    if not os.path.exists(file_path):
        print(f"错误: 文件 '{file_path}' 不存在。")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"错误: 文件 '{file_path}' 不是有效的 JSON 格式。")
        return
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return

    tool_counts = defaultdict(int)
    project_counts = defaultdict(int)
    project_version_counts = defaultdict(lambda: defaultdict(int))

    for defect in data:
        tool_name = defect.get("静态分析工具名", "未知工具")
        project_name = defect.get("简单项目名(不带版本)", "未知项目")
        project_version = defect.get("项目版本", "未知版本")

        tool_counts[tool_name] += 1
        project_counts[project_name] += 1
        project_version_counts[project_name][project_version] += 1

    generate_report(tool_counts, project_counts, project_version_counts)

def generate_report(tool_counts, project_counts, project_version_counts):
    """
    根据分析结果生成并打印报告。
    """
    report = []
    report.append("缺陷分析报告")
    report.append("=" * 30)

    # 1. 按分析工具统计缺陷
    report.append("\n一、按静态分析工具统计缺陷数：")
    report.append("-" * 30)
    if not tool_counts:
        report.append("未找到按工具统计的缺陷数据。")
    else:
        for tool, count in sorted(tool_counts.items()):
            report.append(f"- {tool}: {count} 个缺陷")

    # 2. 按项目统计缺陷
    report.append("\n二、按项目统计缺陷总数：")
    report.append("-" * 30)
    if not project_counts:
        report.append("未找到按项目统计的缺陷数据。")
    else:
        for project, count in sorted(project_counts.items()):
            report.append(f"- {project}: {count} 个缺陷")

    # 3. 按项目及其版本统计缺陷
    report.append("\n三、按项目及版本统计缺陷数：")
    report.append("-" * 30)
    if not project_version_counts:
        report.append("未找到按项目版本统计的缺陷数据。")
    else:
        for project, versions in sorted(project_version_counts.items()):
            report.append(f"\n项目: {project}")
            if not versions:
                report.append("  - 无版本信息")
            else:
                for version, count in sorted(versions.items()):
                    report.append(f"  - 版本 {version}: {count} 个缺陷")
    
    report.append("\n" + "=" * 30)
    report.append("报告生成完毕。")

    print("\n".join(report))

if __name__ == "__main__":
    # 假设 results.json 在脚本所在的同一目录下
    file_to_analyze = "results.json"
    analyze_results(file_to_analyze)
