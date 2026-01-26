#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高性能代码切片和依赖分析工具
采用"先全量索引/建图，再批量查询"的模式
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict, deque
import re
from dataclasses import dataclass, asdict
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp

# 尝试导入tree-sitter，如果没有则给出提示
try:
    from tree_sitter import Language, Parser
    import tree_sitter_c
except ImportError:
    print("需要安装tree-sitter和tree-sitter-c:")
    print("pip install tree-sitter tree-sitter-c")
    sys.exit(1)


@dataclass
class FunctionInfo:
    """函数信息"""
    name: str
    file_path: str
    start_line: int
    end_line: int
    full_text: str
    calls: List[str]  # 调用的函数名列表


class CProjectIndexer:
    """C项目索引器 - 使用tree-sitter解析C代码"""
    
    def __init__(self):
        # 兼容新版tree-sitter API
        try:
            # 新版API (>= 0.21.0)
            self.parser = Parser(Language(tree_sitter_c.language()))
        except TypeError:
            # 旧版API
            self.parser = Parser()
            self.c_language = Language(tree_sitter_c.language())
            self.parser.set_language(self.c_language)
        
        # 全局索引
        self.function_index: Dict[str, Dict[str, List[FunctionInfo]]] = {}  # {project: {func_name: [FunctionInfo]}}
        self.file_functions: Dict[str, Dict[str, List[str]]] = {}  # {project: {file_path: [func_names]}}
        
    def index_project(self, project_path: str, project_name: str) -> None:
        """索引单个项目"""
        print(f"正在索引项目: {project_name}")
        start_time = time.time()
        
        self.function_index[project_name] = defaultdict(list)
        self.file_functions[project_name] = defaultdict(list)
        
        # 查找所有C源文件
        c_files = []
        for ext in ['.c', '.h', '.cpp', '.cc', '.cxx']:
            c_files.extend(Path(project_path).rglob(f'*{ext}'))
        
        print(f"  找到 {len(c_files)} 个C/C++文件")
        
        # 解析每个文件
        for idx, file_path in enumerate(c_files):
            if idx % 100 == 0 and idx > 0:
                print(f"  已处理 {idx}/{len(c_files)} 个文件")
            
            try:
                self._index_file(file_path, project_name)
            except Exception as e:
                # 忽略单个文件的错误，继续处理
                pass
        
        elapsed = time.time() - start_time
        func_count = sum(len(funcs) for funcs in self.function_index[project_name].values())
        print(f"  完成! 索引了 {func_count} 个函数，耗时 {elapsed:.2f}秒")
    
    def _index_file(self, file_path: Path, project_name: str) -> None:
        """索引单个文件"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
        except:
            return
        
        if not code.strip():
            return
        
        # 解析AST
        tree = self.parser.parse(bytes(code, 'utf8'))
        
        # 提取所有函数定义
        functions = self._extract_functions(tree.root_node, code, str(file_path))
        
        # 建立索引
        rel_path = str(file_path.relative_to(file_path.parents[len(file_path.parts) - file_path.parts.index(project_name) - 1]))
        
        for func_info in functions:
            self.function_index[project_name][func_info.name].append(func_info)
            self.file_functions[project_name][rel_path].append(func_info.name)
    
    def _extract_functions(self, node, code: str, file_path: str) -> List[FunctionInfo]:
        """从AST中提取所有函数定义"""
        functions = []
        
        def traverse(n):
            # 检查是否是函数定义
            if n.type == 'function_definition':
                func_info = self._parse_function_definition(n, code, file_path)
                if func_info:
                    functions.append(func_info)
            
            # 递归遍历子节点
            for child in n.children:
                traverse(child)
        
        traverse(node)
        return functions
    
    def _parse_function_definition(self, node, code: str, file_path: str) -> Optional[FunctionInfo]:
        """解析单个函数定义"""
        try:
            # 获取函数名
            declarator = None
            for child in node.children:
                if child.type == 'function_declarator':
                    declarator = child
                    break
            
            if not declarator:
                return None
            
            # 提取函数名
            func_name = None
            for child in declarator.children:
                if child.type == 'identifier':
                    func_name = code[child.start_byte:child.end_byte]
                    break
                elif child.type == 'pointer_declarator':
                    # 处理指针函数
                    for subchild in child.children:
                        if subchild.type == 'identifier':
                            func_name = code[subchild.start_byte:subchild.end_byte]
                            break
            
            if not func_name:
                return None
            
            # 获取函数体
            start_line = node.start_point[0] + 1  # tree-sitter行号从0开始
            end_line = node.end_point[0] + 1
            full_text = code[node.start_byte:node.end_byte]
            
            # 提取函数调用
            calls = self._extract_function_calls(node, code)
            
            return FunctionInfo(
                name=func_name,
                file_path=file_path,
                start_line=start_line,
                end_line=end_line,
                full_text=full_text,
                calls=calls
            )
        except:
            return None
    
    def _extract_function_calls(self, node, code: str) -> List[str]:
        """提取函数体内的所有函数调用"""
        calls = []
        
        def traverse(n):
            if n.type == 'call_expression':
                # 获取被调用的函数名
                func_node = n.child_by_field_name('function')
                if func_node:
                    if func_node.type == 'identifier':
                        call_name = code[func_node.start_byte:func_node.end_byte]
                        calls.append(call_name)
                    elif func_node.type == 'field_expression':
                        # 处理结构体成员函数调用
                        field = func_node.child_by_field_name('field')
                        if field:
                            call_name = code[field.start_byte:field.end_byte]
                            calls.append(call_name)
            
            for child in n.children:
                traverse(child)
        
        traverse(node)
        return list(set(calls))  # 去重
    
    def find_function_by_line(self, project_name: str, file_path: str, line_num: int) -> Optional[FunctionInfo]:
        """根据文件和行号查找函数"""
        if project_name not in self.file_functions:
            return None
        
        # 尝试不同的路径匹配方式
        matching_files = []
        for indexed_file in self.file_functions[project_name].keys():
            if indexed_file.endswith(file_path) or file_path in indexed_file:
                matching_files.append(indexed_file)
        
        if not matching_files:
            return None
        
        # 在匹配的文件中查找包含指定行号的函数
        for matched_file in matching_files:
            func_names = self.file_functions[project_name][matched_file]
            for func_name in func_names:
                for func_info in self.function_index[project_name][func_name]:
                    if file_path in func_info.file_path:
                        if func_info.start_line <= line_num <= func_info.end_line:
                            return func_info
        
        return None
    
    def get_dependencies(self, project_name: str, func_name: str, depth: int = 3) -> List[List[FunctionInfo]]:
        """获取函数的多层依赖（BFS）"""
        if project_name not in self.function_index:
            return []
        
        result_layers = []
        visited = set()
        current_layer = [func_name]
        
        for level in range(depth):
            next_layer = []
            layer_infos = []
            
            for name in current_layer:
                if name in visited:
                    continue
                visited.add(name)
                
                # 获取该函数的所有定义
                func_infos = self.function_index[project_name].get(name, [])
                
                for func_info in func_infos:
                    layer_infos.append(func_info)
                    # 收集该函数调用的其他函数
                    for call in func_info.calls:
                        if call not in visited:
                            next_layer.append(call)
            
            if layer_infos:
                result_layers.append(layer_infos)
            
            if not next_layer:
                break
            
            current_layer = list(set(next_layer))
        
        return result_layers


class SliceAnalyzer:
    """切片分析器 - 主控制器"""
    
    def __init__(self, input_dir: str, output_dir: str, use_cache: bool = True):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.repository_dir = self.input_dir / 'repository'
        self.data_file = self.input_dir / 'data.json'
        self.use_cache = use_cache
        
        self.indexer = None
        self.cache_manager = None
        
        if use_cache:
            try:
                from cache_manager import IndexCache
                self.cache_manager = IndexCache()
            except ImportError:
                print("警告: 无法导入缓存管理器，将不使用缓存")
                self.use_cache = False
        
    def build_index(self) -> None:
        """构建全量索引"""
        print("=" * 60)
        print("阶段 1: 构建全量索引")
        print("=" * 60)
        
        # 尝试加载缓存
        if self.use_cache and self.cache_manager:
            cached_indexer, meta = self.cache_manager.load_index(self.repository_dir)
            if cached_indexer:
                self.indexer = cached_indexer
                print(f"✓ 使用缓存的索引 ({meta.get('project_count', 0)} 个项目)")
                return
        
        # 创建新索引
        self.indexer = CProjectIndexer()
        
        # 获取所有项目
        projects = [d for d in self.repository_dir.iterdir() if d.is_dir()]
        print(f"发现 {len(projects)} 个项目")
        
        # 索引每个项目
        for idx, project_dir in enumerate(sorted(projects), 1):
            print(f"\n[{idx}/{len(projects)}] ", end="")
            self.indexer.index_project(str(project_dir), project_dir.name)
        
        # 保存缓存
        if self.use_cache and self.cache_manager:
            self.cache_manager.save_index(self.indexer, self.repository_dir)
        
        print("\n" + "=" * 60)
        print("索引构建完成!")
        print("=" * 60)
    
    def process_entries(self, batch_size: int = 1000) -> None:
        """批量处理所有条目"""
        print("\n" + "=" * 60)
        print("阶段 2: 批量处理分析条目")
        print("=" * 60)
        
        # 流式读取JSON文件（处理大文件）
        print(f"正在读取 {self.data_file}")
        
        results = []
        failed_entries = []
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                entries = json.load(f)
            
            total = len(entries)
            print(f"共有 {total} 条待分析条目")
            
            # 批量处理
            for idx, entry in enumerate(entries):
                if idx % 100 == 0:
                    print(f"进度: {idx}/{total} ({idx*100//total}%)")
                
                try:
                    result = self._process_single_entry(entry)
                    if result:
                        results.append(result)
                    else:
                        failed_entries.append({**entry, 'reason': 'function_not_found'})
                except Exception as e:
                    failed_entries.append({**entry, 'reason': str(e)})
                
                # 定期保存结果
                if len(results) >= batch_size:
                    self._save_batch(results)
                    results = []
            
            # 保存剩余结果
            if results:
                self._save_batch(results)
            
            # 保存失败条目
            if failed_entries:
                failed_file = self.output_dir / 'failed_entries.json'
                with open(failed_file, 'w', encoding='utf-8') as f:
                    json.dump(failed_entries, f, ensure_ascii=False, indent=2)
                print(f"\n失败条目已保存到: {failed_file}")
            
            print(f"\n处理完成! 成功: {total - len(failed_entries)}, 失败: {len(failed_entries)}")
            
        except Exception as e:
            print(f"错误: {e}")
            raise
    
    def _process_single_entry(self, entry: Dict) -> Optional[Dict]:
        """处理单条分析条目"""
        project_name = entry['project_name_with_version']
        file_path = entry['file_path']
        line_num = entry['line_number']
        
        # 查找目标函数
        target_func = self.indexer.find_function_by_line(project_name, file_path, line_num)
        
        if not target_func:
            return None
        
        # 获取依赖（3层）
        dep_layers = self.indexer.get_dependencies(project_name, target_func.name, depth=3)
        
        # 构建结果 - 使用英文字段名
        dependency_layers = []
        for level, layer_funcs in enumerate(dep_layers[1:], 1):  # 跳过第0层（目标函数本身）
            layer_info = {
                "level": level,
                "functions": [
                    {
                        "function_name": func.name,
                        "file_path": func.file_path,
                        "start_line": func.start_line,
                        "end_line": func.end_line,
                        "source_code": func.full_text,
                        "called_functions": func.calls
                    }
                    for func in layer_funcs
                ]
            }
            dependency_layers.append(layer_info)
        
        result = {
            "tool_name": entry['tool_name'],
            "project_simple_name": entry['project_name'],
            "project_name": project_name,
            "project_version": entry['project_version'],
            "defect_file": file_path,
            "defect_line": line_num,
            "target_function": {
                "function_name": target_func.name,
                "start_line": target_func.start_line,
                "end_line": target_func.end_line,
                "source_code": target_func.full_text,
                "called_functions": target_func.calls
            },
            "dependency_analysis": dependency_layers
        }
        
        return result
    
    def _save_batch(self, results: List[Dict]) -> None:
        """保存批次结果"""
        if not results:
            return
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 使用时间戳避免文件名冲突
        timestamp = int(time.time() * 1000)
        output_file = self.output_dir / f'results_batch_{timestamp}.json'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"  已保存批次结果: {output_file} ({len(results)} 条)")
    
    def merge_results(self) -> None:
        """合并所有批次结果"""
        print("\n" + "=" * 60)
        print("阶段 3: 合并结果文件")
        print("=" * 60)
        
        result_files = list(self.output_dir.glob('results_batch_*.json'))
        
        if not result_files:
            print("没有找到结果文件")
            return
        
        print(f"找到 {len(result_files)} 个批次文件")
        
        all_results = []
        for result_file in sorted(result_files):
            with open(result_file, 'r', encoding='utf-8') as f:
                batch = json.load(f)
                all_results.extend(batch)
        
        # 保存合并结果
        final_output = self.output_dir / 'final_results.json'
        with open(final_output, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        
        print(f"合并完成! 共 {len(all_results)} 条结果")
        print(f"最终结果文件: {final_output}")
        
        # 清理批次文件
        print("\n清理临时批次文件...")
        for result_file in result_files:
            result_file.unlink()
        print("完成!")


def main():
    """主函数"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║      高性能代码切片和依赖分析工具                            ║
║      采用"先全量索引/建图，再批量查询"模式                    ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # 配置路径
    base_dir = Path(__file__).parent
    input_dir = base_dir / 'input'
    output_dir = base_dir / 'output'
    
    # 创建分析器
    analyzer = SliceAnalyzer(str(input_dir), str(output_dir))
    
    # 执行分析
    start_time = time.time()
    
    # 阶段1: 构建索引
    analyzer.build_index()
    
    # 阶段2: 批量处理
    analyzer.process_entries(batch_size=1000)
    
    # 阶段3: 合并结果
    analyzer.merge_results()
    
    # 统计
    total_time = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"全部完成! 总耗时: {total_time:.2f}秒 ({total_time/60:.2f}分钟)")
    print("=" * 60)


if __name__ == '__main__':
    main()
