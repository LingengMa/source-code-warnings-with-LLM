#!/usr/bin/env python3
"""
切片结果统计分析
"""

import json
import argparse
import sys
from collections import defaultdict


def analyze_results(results):
    """分析切片结果"""
    stats = {
        'total': len(results),
        'success': 0,
        'failed': 0,
        'slice_sizes': [],
        'anchor_counts': [],
        'projects': defaultdict(int),
        'file_types': defaultdict(int),
        'avg_slice_size': 0,
        'avg_anchor_count': 0,
        'max_slice_size': 0,
        'min_slice_size': float('inf'),
    }
    
    for result in results:
        if 'error' in result:
            stats['failed'] += 1
            continue
        
        stats['success'] += 1
        
        # 切片大小
        slice_size = len(result['slice_lines'])
        stats['slice_sizes'].append(slice_size)
        stats['max_slice_size'] = max(stats['max_slice_size'], slice_size)
        stats['min_slice_size'] = min(stats['min_slice_size'], slice_size)
        
        # 锚点数量
        anchor_count = len(result['anchors'])
        stats['anchor_counts'].append(anchor_count)
        
        # 项目统计
        project = result.get('project', 'unknown')
        stats['projects'][project] += 1
        
        # 文件类型统计
        file_path = result.get('file', '')
        if file_path.endswith('.c'):
            stats['file_types']['C'] += 1
        elif file_path.endswith(('.cpp', '.cc', '.cxx')):
            stats['file_types']['C++'] += 1
        elif file_path.endswith('.h'):
            stats['file_types']['Header'] += 1
        else:
            ext = file_path.split('.')[-1] if '.' in file_path else 'unknown'
            stats['file_types'][ext] += 1
    
    # 计算平均值
    if stats['slice_sizes']:
        stats['avg_slice_size'] = sum(stats['slice_sizes']) / len(stats['slice_sizes'])
    if stats['anchor_counts']:
        stats['avg_anchor_count'] = sum(stats['anchor_counts']) / len(stats['anchor_counts'])
    
    if stats['min_slice_size'] == float('inf'):
        stats['min_slice_size'] = 0
    
    return stats


def print_stats(stats):
    """打印统计信息"""
    print("\n" + "="*60)
    print("切片结果统计分析")
    print("="*60)
    
    print(f"\n总体统计:")
    print(f"  总样本数: {stats['total']}")
    print(f"  成功: {stats['success']} ({stats['success']/stats['total']*100:.1f}%)")
    print(f"  失败: {stats['failed']} ({stats['failed']/stats['total']*100:.1f}%)")
    
    print(f"\n切片大小统计:")
    print(f"  平均切片大小: {stats['avg_slice_size']:.2f} 行")
    print(f"  最大切片大小: {stats['max_slice_size']} 行")
    print(f"  最小切片大小: {stats['min_slice_size']} 行")
    
    if stats['slice_sizes']:
        sorted_sizes = sorted(stats['slice_sizes'])
        median_idx = len(sorted_sizes) // 2
        median = sorted_sizes[median_idx]
        print(f"  中位数切片大小: {median} 行")
    
    print(f"\n语义锚点统计:")
    print(f"  平均锚点数量: {stats['avg_anchor_count']:.2f} 个")
    
    if stats['anchor_counts']:
        sorted_anchors = sorted(stats['anchor_counts'])
        median_idx = len(sorted_anchors) // 2
        median = sorted_anchors[median_idx]
        print(f"  中位数锚点数量: {median} 个")
        print(f"  最大锚点数量: {max(stats['anchor_counts'])} 个")
        print(f"  最小锚点数量: {min(stats['anchor_counts'])} 个")
    
    print(f"\n项目分布:")
    for project, count in sorted(stats['projects'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {project}: {count} 个样本")
    
    print(f"\n文件类型分布:")
    for file_type, count in sorted(stats['file_types'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {file_type}: {count} 个文件 ({count/stats['total']*100:.1f}%)")
    
    print("\n" + "="*60)


def analyze_single_result(result: dict) -> dict:
    """分析单个结果文件"""
    stats = {
        'project': result.get('project', 'unknown'),
        'file': result.get('file', 'unknown'),
        'target_line': result.get('target_line', -1),
        'slice_size': result.get('slice_size', 0),
        'reconstruction_success': result.get('reconstruction_success', False),
        'error': result.get('error', None)
    }
    return stats


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="切片结果统计分析")
    parser.add_argument('--results-file', type=str, default='output/results.json',
                        help='输入的切片结果文件 (JSON)')
    parser.add_argument('--data-file', type=str, default='input/data.json',
                        help='原始数据集文件 (JSON), 用于关联额外信息')
    args = parser.parse_args()

    try:
        with open(args.results_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
    except FileNotFoundError:
        print(f"错误: 结果文件未找到 {args.results_file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"错误: 无法解析结果文件 {args.results_file}")
        sys.exit(1)

    # 读取数据集
    dataset_map = {}
    try:
        with open(args.data_file, 'r', encoding='utf-8') as f:
            dataset = json.load(f)
        
        # 创建数据集的快速查找映射
        dataset_map = {
            (entry['project_name_with_version'], entry['file_path'], entry['line_number']): entry
            for entry in dataset
        }
    except Exception as e:
        print(f"警告: 无法读取或解析数据集 {args.data_file}: {e}")
        print("将继续进行分析，但不会包含原始告警信息。")

    # 分析结果
    all_stats = []
    for result in results:
        stats = analyze_single_result(result)
        
        # 从数据集中查找原始信息
        if dataset_map:
            # 构造用于在数据集中查找的键
            # 文件路径需要处理，因为结果中的路径是完整的，而数据集中的是相对的
            full_file_path = stats['file']
            project_prefix = f"input/repository/{stats['project']}/"
            relative_file_path = full_file_path.replace(project_prefix, "") if full_file_path.startswith(project_prefix) else full_file_path
            
            key = (stats['project'], relative_file_path, stats['target_line'])
            original_entry = dataset_map.get(key)
            if original_entry:
                # 根据新的 data.json 结构，message 和 rule_id 不再存在
                # 如果需要，可以从这里获取其他信息，例如 tool_name
                stats['tool_name'] = original_entry.get('tool_name', '')

        all_stats.append(stats)
    
    if not all_stats:
        print("未能分析任何结果.")
        return
    
    # 打印总体统计
    print("\n" + "="*30 + " 总体统计 " + "="*30)
    total_samples = len(all_stats)
    success_count = sum(1 for s in all_stats if s['reconstruction_success'])
    print(f"  总样本数: {total_samples}")
    print(f"  成功: {success_count} ({success_count/total_samples*100:.1f}%)")
    print(f"  失败: {total_samples - success_count} ({(total_samples - success_count)/total_samples*100:.1f}%)")
    
    # 按项目分组统计
    project_stats = {}
    for s in all_stats:
        project = s['project']
        if project not in project_stats:
            project_stats[project] = {
                'total': 0,
                'success': 0,
                'slice_sizes': [],
                'errors': {}
            }
        
        project_stats[project]['total'] += 1
        if s['reconstruction_success']:
            project_stats[project]['success'] += 1
            project_stats[project]['slice_sizes'].append(s['slice_size'])
        else:
            error_type = s.get('error', 'unknown_error')
            project_stats[project]['errors'][error_type] = project_stats[project]['errors'].get(error_type, 0) + 1

    print("\n" + "="*30 + " 按项目统计 " + "="*30)
    for project, stats in sorted(project_stats.items()):
        print(f"\n--- {project} ---")
        print(f"  总数: {stats['total']}")
        print(f"  成功: {stats['success']} ({stats['success'] / stats['total']:.2%})")
        
        if stats['slice_sizes']:
            sizes = stats['slice_sizes']
            stats['avg_slice_size'] = sum(sizes) / len(sizes)
            stats['max_slice_size'] = max(sizes)
            stats['min_slice_size'] = min(sizes)
            
            print(f"  平均切片大小: {stats['avg_slice_size']:.2f} 行")
            print(f"  最大切片大小: {stats['max_slice_size']} 行")
            print(f"  最小切片大小: {stats['min_slice_size']} 行")
            
            # 计算中位数
            sorted_sizes = sorted(sizes)
            mid = len(sorted_sizes) // 2
            if len(sorted_sizes) % 2 == 0:
                median = (sorted_sizes[mid - 1] + sorted_sizes[mid]) / 2
            else:
                median = sorted_sizes[mid]
            print(f"  中位数切片大小: {median} 行")
        
        if stats['errors']:
            print("  失败原因:")
            for error, count in stats['errors'].items():
                print(f"    - {error}: {count}")

if __name__ == '__main__':
    main()
