#!/usr/bin/env python3
"""
检验脚本：抽样检查 results.json 中的缺陷文件是否存在
"""
import os
import json
import random

def verify_files(results_file, repository_base, sample_size=1000):
    """
    验证缺陷文件是否存在
    
    Args:
        results_file: results.json 文件路径
        repository_base: 代码仓库根目录
        sample_size: 抽样数量
    """
    # 读取 results.json
    with open(results_file, 'r', encoding='utf-8') as f:
        all_results = json.load(f)
    
    print(f"总共有 {len(all_results)} 条记录")
    
    # 随机抽样
    if len(all_results) > sample_size:
        sample = random.sample(all_results, sample_size)
        print(f"随机抽取 {sample_size} 条记录进行检验\n")
    else:
        sample = all_results
        print(f"记录数少于 {sample_size}，检验全部 {len(sample)} 条记录\n")
    
    # 统计结果
    total = len(sample)
    success_count = 0
    error_count = 0
    errors = []
    
    # 逐条检验
    for i, result in enumerate(sample, 1):
        project_name = result.get('项目名(带版本)', '')
        file_path = result.get('缺陷所属文件', '')
        line = result.get('缺陷行', 0)
        tool = result.get('静态分析工具名', '')
        
        if not project_name or not file_path:
            error_count += 1
            errors.append({
                'index': i,
                'project': project_name,
                'file': file_path,
                'target_line': line,
                'tool': tool,
                'status': 'error',
                'error': '项目名或文件路径为空'
            })
            continue
        
        # 构建完整路径
        full_path = os.path.join(repository_base, project_name, file_path)
        
        # 检查文件是否存在
        if os.path.isfile(full_path):
            success_count += 1
            if i <= 10:  # 只打印前10条成功的
                print(f"✓ [{i}/{total}] {full_path}")
        else:
            error_count += 1
            errors.append({
                'index': i,
                'project': project_name,
                'file': file_path,
                'target_line': line,
                'tool': tool,
                'status': 'error',
                'error': f'Source file not found: {full_path}'
            })
            if error_count <= 10:  # 只打印前10条错误
                print(f"✗ [{i}/{total}] 文件不存在: {full_path}")
    
    # 输出统计结果
    print(f"\n{'='*80}")
    print(f"检验完成!")
    print(f"总计: {total} 条")
    print(f"成功: {success_count} 条 ({success_count/total*100:.2f}%)")
    print(f"失败: {error_count} 条 ({error_count/total*100:.2f}%)")
    print(f"{'='*80}\n")
    
    # 如果有错误，保存到文件
    if errors:
        error_file = os.path.join(os.path.dirname(results_file), 'verification_errors.json')
        with open(error_file, 'w', encoding='utf-8') as f:
            json.dump(errors, f, ensure_ascii=False, indent=2)
        print(f"错误详情已保存到: {error_file}")
        
        # 打印前20个错误的摘要
        print(f"\n前 {min(20, len(errors))} 个错误示例:")
        print("-" * 80)
        for err in errors[:20]:
            print(f"项目: {err['project']}")
            print(f"文件: {err['file']}")
            print(f"行号: {err['target_line']}")
            print(f"工具: {err['tool']}")
            print(f"错误: {err['error']}")
            print("-" * 80)
        
        # 统计错误类型
        print("\n错误类型统计:")
        error_by_project = {}
        for err in errors:
            project = err['project']
            if project not in error_by_project:
                error_by_project[project] = 0
            error_by_project[project] += 1
        
        for project, count in sorted(error_by_project.items(), key=lambda x: x[1], reverse=True):
            print(f"  {project}: {count} 个错误")
    
    return success_count, error_count, errors


def main():
    """主函数"""
    # 配置路径
    results_file = '/home/lg/Documents/projects/毕设/切片/data/results.json'
    repository_base = '/home/lg/Documents/projects/毕设/切片/Mystique-OpenSource-mystique-opensource.github.io-2fffb33/slice_joern/slice_input/repository'
    
    # 检查路径是否存在
    if not os.path.isfile(results_file):
        print(f"错误: results.json 文件不存在: {results_file}")
        return
    
    if not os.path.isdir(repository_base):
        print(f"错误: 代码仓库目录不存在: {repository_base}")
        return
    
    # 执行检验
    verify_files(results_file, repository_base, sample_size=1000)


if __name__ == '__main__':
    main()
