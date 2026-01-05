import json
from collections import defaultdict

def analyze_results(file_path):
    """
    Analyzes the results.json file to count warnings per tool, project, and project version.

    Args:
        file_path (str): The path to the results.json file.
    """
    tool_counts = defaultdict(int)
    project_counts = defaultdict(int)
    project_version_counts = defaultdict(int)

    with open(file_path, 'r') as f:
        data = json.load(f)

    for item in data:
        tool_counts[item['tool_name']] += 1
        project_counts[item['project_name']] += 1
        project_version_counts[item['project_name_with_version']] += 1

    print("## Warning Analysis")
    print("\n### Warnings per Tool")
    print("| Tool | Warnings |")
    print("|---|---|")
    for tool, count in sorted(tool_counts.items()):
        print(f"| {tool} | {count} |")

    print("\n### Warnings per Project")
    print("| Project | Warnings |")
    print("|---|---|")
    for project, count in sorted(project_counts.items()):
        print(f"| {project} | {count} |")

    print("\n### Warnings per Project Version")
    print("| Project Version | Warnings |")
    print("|---|---|")
    for version, count in sorted(project_version_counts.items()):
        print(f"| {version} | {count} |")

if __name__ == "__main__":
    analyze_results('results.json')
