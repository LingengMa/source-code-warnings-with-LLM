import os
import json
import xml.etree.ElementTree as ET
import re
from bs4 import BeautifulSoup

def parse_cppcheck(file_path):
    """解析 cppcheck 的 XML 报告"""
    results = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for error in root.findall('.//error'):
            location = error.find('location')
            if location is not None:
                results.append({
                    'file': location.get('file'),
                    'line': int(location.get('line')),
                })
    except ET.ParseError as e:
        print(f"警告: 解析XML文件失败 {file_path}: {e}")
    except Exception as e:
        print(f"警告: 处理 cppcheck 文件时出错 {file_path}: {e}")
    return results

def parse_codeql(file_path):
    """解析 codeql 的 SARIF 报告"""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 如果文件为空，直接返回空列表
            if os.fstat(f.fileno()).st_size == 0:
                print(f"警告: 文件为空 {file_path}")
                return results
            data = json.load(f)
        
        for run in data.get('runs', []):
            # 创建 ruleId 到 CWE 的映射
            rule_to_cwe = {}
            
            # 预先填充所有规则的CWE信息
            if 'tool' in run and 'driver' in run['tool'] and 'rules' in run['tool']['driver']:
                for rule in run['tool']['driver']['rules']:
                    rule_id = rule.get('id')
                    cwe_tags = []
                    # 提取CWE信息
                    if 'properties' in rule and 'tags' in rule['properties']:
                        for tag in rule['properties']['tags']:
                            if tag.startswith('external/cwe/'):
                                cwe_id = tag.split('/')[-1].replace('cwe-', 'CWE-')
                                cwe_tags.append(cwe_id)
                    
                    if rule_id and cwe_tags:
                        rule_to_cwe[rule_id] = list(set(cwe_tags))

            for result in run.get('results', []):
                rule_id = result.get('ruleId')
                message = result.get('message', {}).get('text')
                level = result.get('level')
                cwe = rule_to_cwe.get(rule_id, []) # 直接从预填充的映射中获取

                for location in result.get('locations', []):
                    physical_location = location.get('physicalLocation')
                    if physical_location:
                        artifact_location = physical_location.get('artifactLocation')
                        region = physical_location.get('region')
                        if artifact_location and region:
                            results.append({
                                'file': artifact_location.get('uri'),
                                'line': region.get('startLine'),
                                'cwe': cwe if cwe else None,
                                'rule_id': rule_id,
                                'message': message,
                                'severity': level,
                            })
    except json.JSONDecodeError as e:
        print(f"警告: 解析JSON文件失败 {file_path}: {e}")
    except Exception as e:
        print(f"警告: 处理 codeql 文件时出错 {file_path}: {e}")
    return results

def parse_semgrep(file_path):
    """解析 semgrep 的 JSON 报告"""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for result in data.get('results', []):
            extra = result.get('extra', {})
            metadata = extra.get('metadata', {})
            cwe_info = metadata.get('cwe')
            cwe_list = []
            if cwe_info:
                if isinstance(cwe_info, list):
                    # e.g., ["CWE-476: NULL_POINTER_DEREFERENCE"]
                    for item in cwe_info:
                        match = re.match(r'CWE-\d+', item)
                        if match:
                            cwe_list.append(match.group(0))
                elif isinstance(cwe_info, str):
                    # e.g., "CWE-476"
                    match = re.match(r'CWE-\d+', cwe_info)
                    if match:
                        cwe_list.append(match.group(0))
            
            results.append({
                'file': result.get('path'),
                'line': result.get('start', {}).get('line'),
                'cwe': cwe_list if cwe_list else None,
                'rule_id': result.get('check_id'),
                'message': extra.get('message'),
                'severity': extra.get('severity'),
            })
    except json.JSONDecodeError as e:
        print(f"警告: 解析JSON文件失败 {file_path}: {e}")
    except Exception as e:
        print(f"警告: 处理 semgrep 文件时出错 {file_path}: {e}")
    return results

# CSA Bug Type 到 CWE 的映射
CSA_BUG_TYPE_TO_CWE = {
    'Dereference of null pointer': 'CWE-476',
    'Dead assignment': 'CWE-563',
    'Use of memory after it is freed': 'CWE-416',
    'Memory leak': 'CWE-401',
    'Division by zero': 'CWE-369',
    'Uninitialized value': 'CWE-457',
    'Potential leak of memory': 'CWE-401',
    # 可以根据需要添加更多映射
}

def parse_csa(file_path):
    """解析 csa (scan-build) 的 HTML 报告"""
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        # 查找包含报告的表格
        report_table = soup.find('table', class_='sortable')
        if not report_table:
            return results

        # 查找表格中的所有行
        rows = report_table.find('tbody').find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) > 4:
                bug_type_cell = cols[1]
                file_cell = cols[2]
                line_cell = cols[4]
                category_cell = cols[0]
                
                bug_type_text = bug_type_cell.get_text(strip=True)
                file_path_text = file_cell.get_text(strip=True)
                line_number_text = line_cell.get_text(strip=True)
                category_text = category_cell.get_text(strip=True)

                cwe = CSA_BUG_TYPE_TO_CWE.get(bug_type_text)

                if file_path_text and line_number_text.isdigit():
                    results.append({
                        'file': file_path_text,
                        'line': int(line_number_text),
                        'cwe': [cwe] if cwe else None,
                        'rule_id': bug_type_text,
                        'message': f"{category_text}: {bug_type_text}",
                        'severity': 'Warning', # CSA不提供严重等级，设为默认值
                    })

    except Exception as e:
        print(f"警告: 处理 csa HTML 文件时出错 {file_path}: {e}")
    return results


# 工具名与解析函数的映射
PARSERS = {
    'cppcheck': parse_cppcheck,
    'codeql': parse_codeql,
    'semgrep': parse_semgrep,
    'csa': parse_csa,
}

# 用于从项目名中提取版本号的正则表达式
VERSION_REGEX = re.compile(r'(\d+(\.\d+)*([a-zA-Z._-]\w*)?)')

def extract_project_info(filename, simple_project_name, tool_name):
    """从文件名和项目名中提取项目信息"""
    base_name = filename
    if tool_name == 'csa':
        # 对于csa，文件名是 'index.html'，我们需要从路径中获取项目名
        # file_path 类似于 /path/to/csa/curl/curl-8.11.1/index.html
        # 我们取父目录名
        base_name = os.path.basename(os.path.dirname(filename))
    else:
        # 移除工具特定的后缀
        base_name = filename.replace('_codeql.sarif', '').replace('_semgrep.json', '').replace('.xml', '').replace('.json', '').replace('.csv', '')
    
    version_match = VERSION_REGEX.search(base_name)
    version = version_match.group(0) if version_match else 'unknown'
    
    # 完整项目名通常是 简单项目名-版本号
    full_project_name = f"{simple_project_name}-{version}"
    
    return full_project_name, version, base_name

def to_relative_path(file_path, simple_project_name, version, extracted_name):
    """将绝对文件路径转换为项目内的相对路径"""
    if not file_path or not simple_project_name or not version:
        return file_path, ''

    # 尝试多种可能的项目目录名模式
    # 例如: ffmpeg-6.1.1, FFmpeg-n6.1.1, curl-curl-8_11_1 等
    possible_patterns = [
        extracted_name,  # 从文件名提取的完整名称，如 ffmpeg-6.1.1
    ]
    
    # 对于 ffmpeg，添加特殊的命名模式
    if simple_project_name.lower() == 'ffmpeg':
        # FFmpeg 使用 FFmpeg-n{version} 的命名方式
        possible_patterns.append(f"FFmpeg-n{version}")
        possible_patterns.append(f"ffmpeg-n{version}")
    
    # 对于 nginx，添加特殊的命名模式
    if simple_project_name.lower() == 'nginx':
        # nginx 可能使用 nginx-release-<version> 或 nginx-<version>
        possible_patterns.append(f"nginx-release-{version}")
        possible_patterns.append(f"nginx-{version}")
    
    # 对于 openssl，添加特殊的命名模式
    if simple_project_name.lower() == 'openssl':
        # openssl 可能使用 openssl-openssl-<version> 或 openssl-<version>
        possible_patterns.append(f"openssl-openssl-{version}")
        possible_patterns.append(f"openssl-{version}")
    
    # 使用 / 分割路径（处理跨平台的路径分隔符）
    # 同时处理 Windows 风格的路径 (/)
    parts = file_path.replace('\\', '/').split('/')
    
    # 尝试直接匹配可能的项目目录名
    for pattern in possible_patterns:
        for i in range(len(parts) - 1, -1, -1):
            # 完全匹配或包含关系
            if parts[i] == pattern or pattern == parts[i]:
                relative_parts = parts[i+1:]
                if relative_parts:
                    result = '/'.join(relative_parts)
                    return result, parts[i]
    
    # 规范化版本号, 将 '.' 替换为 '[._-]' 以匹配不同分隔符
    version_pattern = version.replace('.', r'[._-]')
    
    # 尝试使用正则表达式匹配包含项目名和版本号的路径部分
    try:
        # 构造一个更灵活的正则表达式
        pattern = re.compile(f'.*{re.escape(simple_project_name)}.*{version_pattern}.*', re.IGNORECASE)
        
        for i in range(len(parts) - 1, -1, -1):
            if pattern.match(parts[i]):
                relative_parts = parts[i+1:]
                if relative_parts:
                    return '/'.join(relative_parts), parts[i]
    except re.error as e:
        print(f"警告: 创建正则表达式时出错: {e}")
        pass

    # 如果上面的方法失败了, 回退到只查找项目名
    try:
        # 从后往前找, 找到最后一个包含项目名的部分
        for i in range(len(parts) - 1, -1, -1):
            if simple_project_name.lower() in parts[i].lower():
                relative_parts = parts[i+1:]
                if relative_parts:
                    return '/'.join(relative_parts), parts[i]
    except Exception:
        pass

    # 如果所有方法都失败, 返回原始路径和空字符串
    return file_path, ''


def main():
    """主函数"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_results = []
    
    tool_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d in PARSERS]

    for tool_name in tool_dirs:
        tool_path = os.path.join(base_dir, tool_name)
        parser = PARSERS[tool_name]
        
        project_dirs = [p for p in os.listdir(tool_path) if os.path.isdir(os.path.join(tool_path, p))]
        
        for simple_project_name in project_dirs:
            project_path = os.path.join(tool_path, simple_project_name)
            
            if tool_name == 'csa':
                # CSA 的结果在版本号目录中
                version_dirs = [v for v in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, v))]
                for version_dir in version_dirs:
                    file_path = os.path.join(project_path, version_dir, 'index.html')
                    if os.path.isfile(file_path):
                        print(f"正在处理: {file_path}")
                        
                        # 对于CSA, filename是 'index.html', 但我们需要版本目录名
                        full_project_name, version, extracted_name = extract_project_info(file_path, simple_project_name, tool_name)
                        
                        findings = parser(file_path)
                        
                        for finding in findings:
                            if finding.get('file') and finding.get('line') is not None:
                                # CSA报告中的文件路径通常已经是相对路径
                                relative_path = finding['file']
                                
                                all_results.append({
                                    'tool_name': tool_name,
                                    'project_name': simple_project_name,
                                    'project_name_with_version': full_project_name,
                                    'project_version': version,
                                    'file_path': relative_path,
                                    'line_number': finding['line'],
                                    'cwe': finding.get('cwe'),
                                    'rule_id': finding.get('rule_id'),
                                    'message': finding.get('message'),
                                    'severity': finding.get('severity'),
                                })
            else:
                for filename in os.listdir(project_path):
                    file_path = os.path.join(project_path, filename)
                    if not os.path.isfile(file_path):
                        continue

                    print(f"正在处理: {file_path}")
                    
                    full_project_name, version, extracted_name = extract_project_info(filename, simple_project_name, tool_name)
                    
                    findings = parser(file_path)
                    
                    for finding in findings:
                        if finding.get('file') and finding.get('line') is not None:
                            original_path = finding['file']
                            # 移除 'file://' 前缀
                            if original_path and original_path.startswith('file://'):
                                original_path = original_path[7:]
                            
                            relative_path, actual_project_dir = to_relative_path(original_path, simple_project_name, version, extracted_name)
                            
                            # 使用实际找到的项目目录名，如果没找到则使用默认的 full_project_name
                            final_project_name = actual_project_dir if actual_project_dir else full_project_name
                            
                            # 统一 ffmpeg 项目名称为小写格式
                            if simple_project_name.lower() == 'ffmpeg':
                                # 将 FFmpeg-n7.1.1 转换为 ffmpeg-7.1.1
                                # 将 ffmpeg-n7.1 转换为 ffmpeg-7.1
                                final_project_name = re.sub(r'^FFmpeg-n', 'ffmpeg-', final_project_name, flags=re.IGNORECASE)
                                final_project_name = re.sub(r'^ffmpeg-n', 'ffmpeg-', final_project_name, flags=re.IGNORECASE)
                            
                            # 统一 nginx 项目名称格式
                            # nginx-release-1.27.4 -> nginx-1.27.4
                            if simple_project_name.lower() == 'nginx':
                                final_project_name = re.sub(r'^nginx-release-', 'nginx-', final_project_name, flags=re.IGNORECASE)
                            
                            # 统一 openssl 项目名称格式
                            # 确保所有 openssl 项目名都使用 openssl-openssl-<version> 格式
                            if simple_project_name.lower() == 'openssl':
                                # 如果项目名是 openssl-3.4.1，转换为 openssl-openssl-3.4.1
                                # 如果已经是 openssl-openssl-3.4.1，保持不变
                                if not re.match(r'^openssl-openssl-', final_project_name, re.IGNORECASE):
                                    # 替换第一个 openssl- 为 openssl-openssl-
                                    final_project_name = re.sub(r'^openssl-', 'openssl-openssl-', final_project_name, flags=re.IGNORECASE, count=1)
                            
                            # 统一 curl 项目名称格式
                            # curl-curl-8_13_0 -> curl-8_13_0 (去除重复的 curl)
                            # 同时将版本号中的点替换为下划线: curl-8.17.0 -> curl-8_17_0
                            if simple_project_name.lower() == 'curl':
                                final_project_name = re.sub(r'^curl-curl-', 'curl-', final_project_name, flags=re.IGNORECASE)
                                # 将版本号中的点替换为下划线
                                final_project_name = re.sub(r'^(curl-)(\d+)\.(\d+)\.(\d+)$', r'\1\2_\3_\4', final_project_name, flags=re.IGNORECASE)

                            all_results.append({
                                'tool_name': tool_name,
                                'project_name': simple_project_name,
                                'project_name_with_version': final_project_name,
                                'project_version': version,
                                'file_path': relative_path,
                                'line_number': finding['line'],
                                'cwe': finding.get('cwe'),
                                'rule_id': finding.get('rule_id'),
                                'message': finding.get('message'),
                                'severity': finding.get('severity'),
                            })

    output_path = os.path.join(base_dir, 'results.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)

    print(f"\n处理完成! {len(all_results)} 条缺陷已汇总到 {output_path}")

if __name__ == '__main__':
    main()
