#!/usr/bin/env python3
"""
切片分析 + 代码重构 - 生成完整的切片结果（包含重构代码）
"""

import os
import json
import argparse
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from slice_analyzer import CSemanticSlicer
from slice_reconstructor import reconstruct_slice

# 尝试导入更快的JSON库
try:
    import orjson
    USE_ORJSON = True
except ImportError:
    USE_ORJSON = False

# 快速JSON序列化辅助函数
def fast_json_dump(data, file_path):
    """使用最快的可用JSON库保存数据"""
    if USE_ORJSON:
        # orjson 最快，但返回bytes
        with open(file_path, 'wb') as f:
            f.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
    else:
        # 标准库（最慢）
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def fast_json_load(file_path):
    """使用最快的可用JSON库加载数据"""
    if USE_ORJSON:
        with open(file_path, 'rb') as f:
            return orjson.loads(f.read())
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


# 线程锁用于保护共享资源
print_lock = threading.Lock()
results_lock = threading.Lock()


def process_with_reconstruction(file_path: str, target_line: int,
                                enable_interprocedural: bool = True,
                                max_call_depth: int = 1,
                                verbose: bool = False) -> dict:
    """
    执行切片分析并重构代码
    
    Returns:
        包含切片信息和重构代码的完整结果
    """
    # 读取源代码
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        source_code = f.read()
    
    # 判断文件类型
    is_cpp = file_path.endswith(('.cpp', '.cc', '.cxx', '.hpp', '.hxx'))
    
    # 执行切片分析（仅verbose模式打印）
    if verbose:
        print(f"分析文件: {file_path}")
        print(f"目标行: {target_line}")
    
    slicer = CSemanticSlicer(is_cpp=is_cpp)
    slice_result = slicer.slice(
        file_path, target_line,
        enable_interprocedural=enable_interprocedural,
        max_call_depth=max_call_depth
    )
    
    if not slice_result:
        return {
            'error': 'Slice analysis failed',
            'file': file_path,
            'target_line': target_line,
            'reconstruction_success': False
        }
    
    # 准备基础结果
    result = slice_result.to_dict()
    result['file'] = file_path
    result['config'] = {
        'interprocedural': enable_interprocedural,
        'max_call_depth': max_call_depth
    }
    
    # 提取切片对应的原始代码行
    source_lines = source_code.split('\n')
    slice_code_lines = []
    for line_num in sorted(slice_result.slice_lines):
        if 0 < line_num <= len(source_lines):
            slice_code_lines.append({
                'line_number': line_num,
                'code': source_lines[line_num - 1],
                'function': result['function_map'].get(str(line_num), 'unknown')
            })
    
    result['slice_code_lines'] = slice_code_lines
    result['slice_size'] = len(slice_result.slice_lines)
    
    # 添加目标行所在函数
    result['target_function'] = result['function_map'].get(str(target_line), 'unknown')
    
    # 执行代码重构
    if verbose:
        print("重构切片代码...")
    try:
        reconstructed_code = reconstruct_slice(source_code, result)
        result['reconstructed_code'] = reconstructed_code
        result['reconstruction_success'] = True
    except Exception as e:
        if verbose:
            print(f"重构失败: {e}")
        result['reconstructed_code'] = f"/* Reconstruction failed: {str(e)} */"
        result['reconstruction_success'] = False
    
    # 添加额外分析信息
    result['analysis_info'] = {
        'pointer_aliases': {k: list(v) for k, v in slicer.pointer_aliases.items()},
        'function_info': {},
        'type_info': slicer.type_info,
        'call_graph': {k: list(v) for k, v in slicer.call_graph.items()}
    }
    
    # 函数信息
    for func_name, func_info in slicer.function_info.items():
        result['analysis_info']['function_info'][func_name] = {
            'params': func_info.params,
            'pointer_params': list(func_info.pointer_params),
            'return_type': func_info.return_type,
            'modifies_globals': list(func_info.modifies_globals),
            'may_modify_params': list(func_info.may_modify_params),
            'is_recursive': func_info.is_recursive
        }
    
    return result


def sort_results_by_dataset_order(results: list, dataset: list) -> list:
    """按数据集原始顺序排序结果"""
    # 创建一个映射来恢复顺序
    result_map = {}
    for result in results:
        key = (result.get('project'), 
               result.get('file', result.get('target_file', '')).split('/')[-1] 
               if '/' in result.get('file', result.get('target_file', '')) 
               else result.get('file', result.get('target_file', '')),
               result.get('target_line'))
        result_map[key] = result
    
    # 按数据集顺序重新组织
    sorted_results = []
    for entry in dataset:
        project = entry['project_name_with_version'] # 使用 project_name_with_version 字段作为项目目录
        file_rel = entry['file_path']
        target_line = entry['line_number']
        
        # 尝试多种键匹配
        result = None
        for key in result_map:
            if (key[0] == project and key[2] == target_line and 
                (key[1] in file_rel or file_rel in key[1])):
                result = result_map[key]
                break
        
        if result:
            sorted_results.append(result)
    
    return sorted_results if sorted_results else results


def process_single_entry(entry: dict, idx: int, total: int,
                        enable_interprocedural: bool = True,
                        max_call_depth: int = 1,
                        verbose: bool = False) -> dict:
    """处理单个数据集条目（线程安全）"""
    project_name = entry['project_name_with_version'] # 使用 project_name_with_version 字段作为项目目录
    file_path_rel = entry['file_path']
    target_line = entry['line_number']
    
    # 构建完整路径
    full_path = os.path.join('input/repository', project_name, file_path_rel)
    
    # 只在verbose模式下打印详细信息
    if verbose:
        with print_lock:
            print(f"\n{'='*60}")
            print(f"[{idx+1}/{total}] Processing...")
            print(f"  文件: {file_path_rel}")
            print(f"  行号: {target_line}")
    
    # 检查文件是否存在
    if not os.path.exists(full_path):
        if verbose:
            with print_lock:
                print(f"  ✗ 文件不存在: {full_path}") # 打印完整路径以供调试
        return {
            'project': project_name,
            'file': file_path_rel,
            'target_line': target_line,
            'error': 'file_not_found',
            'reconstruction_success': False
        }
    
    # 检查是否为C/C++文件
    c_cpp_extensions = ('.c', '.cc', '.cpp', '.cxx', '.h', '.hpp', '.hxx')
    if not full_path.lower().endswith(c_cpp_extensions):
        if verbose:
            with print_lock:
                print(f"  ⚠ 跳过非C/C++文件")
        return {
            'project': project_name,
            'file': file_path_rel,
            'target_line': target_line,
            'error': 'not_c_cpp_file',
            'reconstruction_success': False
        }
    
    # 执行分析和重构
    try:
        result = process_with_reconstruction(
            full_path, target_line,
            enable_interprocedural=enable_interprocedural,
            max_call_depth=max_call_depth,
            verbose=verbose
        )
        
        result['project'] = project_name
        
        if verbose:
            with print_lock:
                print(f"  ✓ 切片大小: {result.get('slice_size', 0)} 行")
                print(f"  ✓ 重构: {'成功' if result.get('reconstruction_success') else '失败'}")
        
        return result
        
    except Exception as e:
        if verbose:
            with print_lock:
                print(f"  ✗ 处理失败: {e}")
        return {
            'project': project_name,
            'file': file_path_rel,
            'target_line': target_line,
            'error': str(e),
            'reconstruction_success': False
        }


def process_dataset(data_file: str, output_file: str,
                   enable_interprocedural: bool = True,
                   max_call_depth: int = 1,
                   max_samples: int = None,
                   resume: bool = True,
                   num_workers: int = None,
                   save_interval: int = 100,
                   use_processes: bool = True,
                   chunk_size: int = 1000):
    """处理整个数据集（支持断点续传、多进程/多线程和定期保存）
    
    Args:
        use_processes: True使用多进程（CPU密集型推荐），False使用多线程（I/O密集型）
        chunk_size: 分块保存大小，每N条结果保存到一个单独的chunk文件
    """
    # 自动确定worker数量
    if num_workers is None:
        if use_processes:
            num_workers = multiprocessing.cpu_count()
        else:
            num_workers = multiprocessing.cpu_count() * 2
    
    # 读取数据集
    dataset = fast_json_load(data_file)
    
    # 创建chunks目录
    chunks_dir = os.path.join(os.path.dirname(output_file) or '.', 'chunks')
    os.makedirs(chunks_dir, exist_ok=True)
    
    # 加载已有结果（断点续传 - 支持chunks）
    existing_results = {}
    if resume:
        try:
            # 优先从chunks目录加载（最新数据）
            if os.path.exists(chunks_dir):
                chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.startswith('success_chunk_')])
                if chunk_files:
                    print(f"📂 从chunks目录加载断点数据...")
                    for chunk_file in chunk_files:
                        chunk_path = os.path.join(chunks_dir, chunk_file)
                        chunk_data = fast_json_load(chunk_path)
                        for result in chunk_data:
                            project = result.get('project')
                            target_line = result.get('target_line')
                            
                            # 提取相对路径
                            file_path = result.get('file', result.get('target_file', ''))
                            if file_path.startswith('input/repository/'):
                                parts = file_path.split('/', 3)
                                if len(parts) >= 4:
                                    file_path = parts[3]
                            
                            key = (project, file_path, target_line)
                            
                            # 只保留成功的结果
                            if result.get('reconstruction_success', False):
                                existing_results[key] = result
                    print(f"   已加载: {len(existing_results)} 个成功条目")
            
            # 如果chunks目录为空，尝试从最终输出文件加载
            if not existing_results and os.path.exists(output_file):
                print(f"📂 从输出文件加载断点数据...")
                existing = fast_json_load(output_file)
                for result in existing:
                    project = result.get('project')
                    target_line = result.get('target_line')
                    
                    # 提取相对路径
                    file_path = result.get('file', result.get('target_file', ''))
                    if file_path.startswith('input/repository/'):
                        parts = file_path.split('/', 3)
                        if len(parts) >= 4:
                            file_path = parts[3]
                    
                    key = (project, file_path, target_line)
                    
                    # 只保留成功的结果
                    if result.get('reconstruction_success', False):
                        existing_results[key] = result
                
                print(f"   已加载: {len(existing_results)} 个成功条目")
        except Exception as e:
            print(f"⚠ 无法加载已有结果: {e}")
    
    # 分离已处理和待处理的条目
    to_process = []
    results = []
    skipped = 0
    
    for idx, entry in enumerate(dataset):
        project_name = entry['project_name_with_version'] # 使用 project_name_with_version 字段作为项目目录
        file_path_rel = entry['file_path']
        target_line = entry['line_number']
        
        # 检查是否已经处理过
        key = (project_name, file_path_rel, target_line)
        if key in existing_results:
            results.append(existing_results[key])
            skipped += 1
        else:
            to_process.append((idx, entry))
    
    print(f"\n📊 任务统计:")
    print(f"  总样本数: {len(dataset)}")
    print(f"  已完成: {skipped}")
    print(f"  待处理: {len(to_process)}")
    print(f"  并发模式: {'多进程' if use_processes else '多线程'} × {num_workers}")
    print(f"  自动保存: 每 {save_interval} 个样本")
    print(f"  分块保存: 每 {chunk_size} 条/文件")
    
    # 创建chunks目录
    chunks_dir = os.path.join(os.path.dirname(output_file) or '.', 'chunks')
    os.makedirs(chunks_dir, exist_ok=True)
    
    if not to_process:
        print(f"\n✓ 所有样本已处理完成!")
    else:
        # 使用进程池或线程池处理
        executor_class = ProcessPoolExecutor if use_processes else ThreadPoolExecutor
        print(f"\n🚀 开始{'多进程' if use_processes else '多线程'}处理...\n")
        
        # 定期保存配置
        last_save_count = 0
        
        def save_intermediate_results():
            """保存中间结果（分块保存优化版）"""
            with print_lock:
                print(f"\n💾 分块保存中 ({len(results)} 条)...", end='', flush=True)
            
            # 快速分离（不排序）
            with results_lock:
                success_list = []
                failed_list = []
                for result in results:
                    simplified = {k: v for k, v in result.items() 
                                       if k not in ['function_map', 'slice_code_lines', 'analysis_info']}
                    if result.get('reconstruction_success', False):
                        success_list.append(simplified)
                    else:
                        failed_list.append(simplified)
            
            # 分块保存成功结果
            chunk_id = 0
            for i in range(0, len(success_list), chunk_size):
                chunk = success_list[i:i+chunk_size]
                chunk_file = os.path.join(chunks_dir, f'success_chunk_{chunk_id:04d}.json')
                fast_json_dump(chunk, chunk_file)
                chunk_id += 1
            
            # 保存失败结果（通常很少，不分块）
            if failed_list:
                failed_file = os.path.join(chunks_dir, 'failed_all.json')
                fast_json_dump(failed_list, failed_file)
            
            with print_lock:
                print(f" 完成! ({chunk_id} 个chunk, 成功:{len(success_list)}, 失败:{len(failed_list)})")
        
        with executor_class(max_workers=num_workers) as executor:
            # 提交所有任务（禁用verbose减少输出）
            future_to_idx = {}
            for idx, entry in to_process:
                future = executor.submit(
                    process_single_entry,
                    entry, idx, len(dataset),
                    enable_interprocedural, max_call_depth,
                    False  # verbose=False 提升性能
                )
                future_to_idx[future] = idx
            
            # 收集结果（按完成顺序）
            completed = 0
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    result = future.result()
                    with results_lock:
                        results.append(result)
                    completed += 1
                    
                    # 只在特定里程碑或保存时打印
                    should_print = (completed % 50 == 0 or 
                                  completed == len(to_process) or
                                  completed - last_save_count >= save_interval)
                    
                    if should_print:
                        with print_lock:
                            print(f"\n📈 进度: {completed}/{len(to_process)} 完成 (总计: {len(results)} 条)")
                    
                    # 定期保存
                    if completed - last_save_count >= save_interval:
                        save_intermediate_results()
                        last_save_count = completed
                        
                except Exception as e:
                    with print_lock:
                        print(f"\n✗ 任务 {idx+1} 异常: {e}")
                    with results_lock:
                        results.append({
                            'project': dataset[idx]['project_name_with_version'], # 使用 project_name_with_version 字段
                            'file': dataset[idx]['file_path'],
                            'target_line': dataset[idx]['line_number'],
                            'error': f'thread_exception: {str(e)}',
                            'reconstruction_success': False
                        })
    
    # 最终保存：合并所有chunks并排序
    print(f"\n🔄 合并chunks并排序...")
    
    # 读取所有成功的chunks
    all_success = []
    chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.startswith('success_chunk_')])
    for chunk_file in chunk_files:
        chunk_path = os.path.join(chunks_dir, chunk_file)
        chunk_data = fast_json_load(chunk_path)
        all_success.extend(chunk_data)
    
    # 读取失败结果
    all_failed = []
    failed_path = os.path.join(chunks_dir, 'failed_all.json')
    if os.path.exists(failed_path):
        all_failed = fast_json_load(failed_path)
    
    # 合并并按原始顺序排序
    all_results = all_success + all_failed
    
    # 重构results列表用于排序
    results_for_sort = []
    for r in all_results:
        # 还原完整结构（添加回被删除的字段，用于排序）
        full_result = r.copy()
        results_for_sort.append(full_result)
    
    sorted_results = sort_results_by_dataset_order(results_for_sort, dataset)
    
    # 再次分离
    success_results = []
    failed_results = []
    for result in sorted_results:
        simplified = {k: v for k, v in result.items() 
                     if k not in ['function_map', 'slice_code_lines', 'analysis_info']}
        if result.get('reconstruction_success', False):
            success_results.append(simplified)
        else:
            failed_results.append(simplified)
    
    # 保存最终合并结果
    fast_json_dump(success_results, output_file)
    
    if failed_results:
        failed_file = output_file.replace('.json', '_failed.json')
        fast_json_dump(failed_results, failed_file)
        print(f"⚠️  失败结果: {failed_file}")
    
    print(f"\n{'='*60}")
    print(f"✅ 完成！结果已保存到: {output_file}")
    print(f"   Chunks目录: {chunks_dir} (可删除)")
    print(f"总计: {len(dataset)} 个样本")
    print(f"跳过: {skipped} 个（已有成功结果）")
    print(f"本次处理: {len(to_process)} 个")
    print(f"总成功: {len(success_results)} 个")
    print(f"总失败: {len(failed_results)} 个")
    if USE_ORJSON:
        print(f"JSON库: orjson (最快)")
    else:
        print(f"JSON库: 标准库 (建议: pip install orjson)")


def main():
    parser = argparse.ArgumentParser(
        description='切片分析 + 代码重构 - 生成完整结果'
    )
    parser.add_argument('--data-file', type=str, default='input/data.json',
                       help='输入数据文件')
    parser.add_argument('--output', '-o', type=str, default='output/results.json',
                       help='输出文件路径')
    parser.add_argument('--no-interprocedural', action='store_true',
                       help='禁用过程间分析')
    parser.add_argument('--max-call-depth', type=int, default=1,
                       help='最大调用深度')
    parser.add_argument('--max-samples', type=int, default=None,
                       help='最大处理样本数（用于测试）')
    parser.add_argument('--no-resume', action='store_true',
                       help='禁用断点续传（重新处理所有样本）')
    parser.add_argument('--workers', '-j', type=int, default=None,
                       help='并发worker数量（默认: 多进程=CPU核心数，多线程=CPU核心数×2）')
    parser.add_argument('--use-threads', action='store_true',
                       help='使用多线程而非多进程（不推荐，仅用于I/O密集型任务）')
    parser.add_argument('--save-interval', type=int, default=100,
                       help='自动保存间隔（处理N个样本后保存，默认: 100）')
    parser.add_argument('--chunk-size', type=int, default=1000,
                       help='分块保存大小（每N条结果保存到一个chunk文件，默认: 1000）')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='输出详细处理信息（会降低性能）')
    
    # 单文件模式
    parser.add_argument('--file', type=str,
                       help='单个文件路径（单文件模式）')
    parser.add_argument('--line', type=int,
                       help='目标行号（单文件模式）')
    
    args = parser.parse_args()
    
    # 创建输出目录
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)
    
    if args.file and args.line:
        # 单文件模式
        print("=" * 60)
        print("单文件切片 + 重构模式")
        print("=" * 60)
        
        result = process_with_reconstruction(
            args.file, args.line,
            enable_interprocedural=not args.no_interprocedural,
            max_call_depth=args.max_call_depth,
            verbose=True  # 单文件模式始终显示详细信息
        )
        
        # 简化结果：移除冗余字段
        simplified_result = {k: v for k, v in result.items() 
                           if k not in ['function_map', 'slice_code_lines', 'analysis_info']}
        
        # 保存简化后的结果
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(simplified_result, f, indent=2, ensure_ascii=False)
        
        # 同时保存重构代码到单独文件
        if result.get('reconstruction_success'):
            code_output = args.output.replace('.json', '_reconstructed.c')
            with open(code_output, 'w', encoding='utf-8') as f:
                f.write(result['reconstructed_code'])
            print(f"重构代码已保存到: {code_output}")
        
        print(f"完整结果已保存到: {args.output}")
        
    else:
        # 批量模式
        print("=" * 60)
        print("批量切片 + 重构模式")
        print("=" * 60)
        
        process_dataset(
            args.data_file, args.output,
            enable_interprocedural=not args.no_interprocedural,
            max_call_depth=args.max_call_depth,
            max_samples=args.max_samples,
            resume=not args.no_resume,
            num_workers=args.workers,
            save_interval=args.save_interval,
            use_processes=not args.use_threads,
            chunk_size=args.chunk_size
        )


if __name__ == '__main__':
    main()
