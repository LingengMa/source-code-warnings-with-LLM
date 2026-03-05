import json
from collections import defaultdict
import os
import re

def load_top_cwes(file_path):
    """
    从文件中加载 Top CWE 列表。
    Args:
        file_path (str): 包含 Top CWE 的文件路径。
    Returns:
        set: CWE ID 的集合。
    """
    top_cwes = set()
    if not os.path.exists(file_path):
        print(f"警告: Top CWE 文件 '{file_path}' 不存在。将不进行高亮显示。")
        return top_cwes

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 使用正则表达式提取所有 CWE-ID
        found_cwes = re.findall(r'CWE-\d+', content)
        top_cwes = set(found_cwes)
        print(f"成功加载 {len(top_cwes)} 个 Top CWE。")
    except Exception as e:
        print(f"读取 Top CWE 文件时发生错误: {e}")
    
    return top_cwes

def analyze_cwe_by_tool(input_path, output_path, top_cwes_path):
    """
    分析 results.json 文件，统计每个工具检测到的 CWE 类型及其数量，并生成 Markdown 报告。

    Args:
        input_path (str): results.json 文件的路径。
        output_path (str): 输出报告文件的路径。
        top_cwes_path (str): Top CWE 文件的路径。
    """
    if not os.path.exists(input_path):
        print(f"错误: 文件 '{input_path}' 不存在。请先运行 aggregate_results.py。")
        return

    top_cwes = load_top_cwes(top_cwes_path)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"错误: 文件 '{input_path}' 不是有效的 JSON 格式。")
        return
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return

    # 使用 defaultdict 来存储每个工具的 CWE 统计信息
    # 结构: { 'tool_name': { 'CWE-ID': count } }
    tool_cwe_counts = defaultdict(lambda: defaultdict(int))

    for result in data:
        tool_name = result.get('tool_name')
        cwe_list = result.get('cwe')

        if not tool_name:
            continue

        if cwe_list and isinstance(cwe_list, list):
            for cwe in cwe_list:
                if cwe: # 确保 cwe 不是 None 或空字符串
                    tool_cwe_counts[tool_name][cwe] += 1
        else:
            # 如果 cwe 字段不存在、为 None 或为空列表，则计为 "未指定CWE"
            tool_cwe_counts[tool_name]['未指定CWE'] += 1
    
    generate_cwe_report(tool_cwe_counts, output_path, top_cwes)

def generate_cwe_report(tool_cwe_counts, output_path, top_cwes):
    """
    根据统计结果生成并保存 CWE 分析的 Markdown 报告。
    """
    report_lines = []
    report_lines.append("# CWE 类型分析报告")
    report_lines.append("\n本文档按工具详细列出了检测到的 CWE（通用缺陷枚举）类型及其出现次数。")
    report_lines.append("\n**Top 10 CWE 会以粗体显示。**")

    if not tool_cwe_counts:
        report_lines.append("\n未找到任何 CWE 数据进行分析。")
    else:
        # 按工具名称排序
        for tool, cwe_counts in sorted(tool_cwe_counts.items()):
            report_lines.append(f"\n## 工具: {tool}")
            report_lines.append("\n| CWE 类型 | 数量 |")
            report_lines.append("|---|---|")
            
            if not cwe_counts:
                report_lines.append("| *未发现任何 CWE* | 0 |")
                continue

            # 按 CWE 数量降序排序
            sorted_cwes = sorted(cwe_counts.items(), key=lambda item: item[1], reverse=True)
            
            for cwe, count in sorted_cwes:
                cwe_display = f"**{cwe}**" if cwe in top_cwes else cwe
                report_lines.append(f"| {cwe_display} | {count} |")

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(report_lines))
        print(f"报告已成功生成到: {output_path}")
    except Exception as e:
        print(f"写入报告文件时发生错误: {e}")


if __name__ == "__main__":
    # 定义输入和输出文件路径
    results_file = "results.json"
    report_file = "cwe_analysis_report.md"
    top_cwes_file = os.path.join("docs", "cwe-top10-2025")
    analyze_cwe_by_tool(results_file, report_file, top_cwes_file)
