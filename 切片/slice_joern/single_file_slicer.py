"""
单文件切片分析器
直接对单个 C/C++ 文件进行切片分析，使用 Joern 实时生成 PDG
"""
import os
import json
import logging
import subprocess
import tempfile
import shutil
from typing import Dict, List, Set, Tuple, Optional
import traceback

import config
from pdg_loader import PDG, PDGNode
from slice_engine import SliceEngine


logging.basicConfig(
    level=logging.INFO if config.VERBOSE else logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class SingleFileSlicerException(Exception):
    """单文件切片器异常"""
    pass


class JoernAnalyzer:
    """Joern 分析器 - 对单个文件生成 PDG"""
    
    def __init__(self, joern_path: str = "/opt/joern-cli"):
        self.joern_path = joern_path
        self.joern_parse = os.path.join(joern_path, "joern-parse")
        self.joern_export = os.path.join(joern_path, "joern-export")
        
        # 检查 Joern 是否可用
        if not os.path.exists(self.joern_parse):
            raise SingleFileSlicerException(f"Joern not found at {joern_path}")
    
    def analyze_file(self, source_file: str, output_dir: str) -> str:
        """
        分析单个源文件，生成 PDG
        
        Args:
            source_file: 源文件路径
            output_dir: 输出目录
            
        Returns:
            PDG 目录路径
        """
        logging.info(f"Analyzing file with Joern: {source_file}")
        
        # 创建临时目录结构
        code_dir = os.path.join(output_dir, "code")
        os.makedirs(code_dir, exist_ok=True)
        
        # 复制源文件到临时目录
        file_name = os.path.basename(source_file)
        target_file = os.path.join(code_dir, file_name)
        shutil.copy2(source_file, target_file)
        
        # 生成 CPG
        logging.info("Generating CPG...")
        try:
            subprocess.run(
                [self.joern_parse, '--language', 'c', os.path.abspath(code_dir)],
                cwd=output_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                check=True,
                timeout=60
            )
        except subprocess.TimeoutExpired:
            raise SingleFileSlicerException("Joern parse timeout")
        except subprocess.CalledProcessError as e:
            raise SingleFileSlicerException(f"Joern parse failed: {e.stderr.decode()}")
        
        # 导出 PDG
        pdg_dir = os.path.join(output_dir, 'pdg')
        logging.info("Exporting PDG...")
        try:
            subprocess.run(
                [self.joern_export, '--repr', 'pdg', '--out', os.path.abspath(pdg_dir)],
                cwd=output_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                check=True,
                timeout=60
            )
        except subprocess.TimeoutExpired:
            raise SingleFileSlicerException("Joern export timeout")
        except subprocess.CalledProcessError as e:
            raise SingleFileSlicerException(f"Joern export failed: {e.stderr.decode()}")
        
        # 导出 CFG
        cfg_dir = os.path.join(output_dir, 'cfg')
        logging.info("Exporting CFG...")
        try:
            subprocess.run(
                [self.joern_export, '--repr', 'cfg', '--out', os.path.abspath(cfg_dir)],
                cwd=output_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                check=True,
                timeout=60
            )
        except Exception as e:
            logging.warning(f"CFG export failed (non-critical): {e}")
        
        # 导出完整 CPG
        cpg_dir = os.path.join(output_dir, 'cpg')
        logging.info("Exporting CPG...")
        try:
            subprocess.run(
                [self.joern_export, '--repr', 'all', '--out', os.path.abspath(cpg_dir)],
                cwd=output_dir,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                check=True,
                timeout=60
            )
        except Exception as e:
            logging.warning(f"CPG export failed (non-critical): {e}")
        
        logging.info(f"✓ Analysis complete. PDG saved to {pdg_dir}")
        return pdg_dir
    
    def preprocess_pdg(self, pdg_dir: str, cfg_dir: str, cpg_dir: str):
        """
        预处理 PDG：合并 CFG，清理无用边
        
        这个函数参考了 Mystique 项目中的 joern.py 的预处理逻辑
        """
        import networkx as nx
        
        logging.info("Preprocessing PDGs...")
        
        if not os.path.exists(cpg_dir) or not os.path.exists(os.path.join(cpg_dir, 'export.dot')):
            logging.warning("CPG not found, skipping preprocessing")
            return
        
        try:
            cpg = nx.nx_agraph.read_dot(os.path.join(cpg_dir, 'export.dot'))
        except Exception as e:
            logging.warning(f"Failed to load CPG: {e}")
            return
        
        for pdg_file in os.listdir(pdg_dir):
            if not pdg_file.endswith('-pdg.dot'):
                continue
            
            file_id = pdg_file.split('-')[0]
            pdg_path = os.path.join(pdg_dir, pdg_file)
            cfg_path = os.path.join(cfg_dir, f'{file_id}-cfg.dot')
            
            try:
                pdg_graph = nx.nx_agraph.read_dot(pdg_path)
                
                # 加载 CFG（如果存在）
                if os.path.exists(cfg_path):
                    cfg_graph = nx.nx_agraph.read_dot(cfg_path)
                    pdg_graph = nx.compose(pdg_graph, cfg_graph)
                
                # 清理空的 DDG 边
                edges_to_remove = []
                for u, v, k, d in pdg_graph.edges(data=True, keys=True):
                    label = d.get('label', '')
                    if label in ['DDG: ', 'DDG: this']:
                        edges_to_remove.append((u, v, k))
                
                pdg_graph.remove_edges_from(edges_to_remove)
                
                # 添加 CFG 标签
                for u, v, k, d in pdg_graph.edges(data=True, keys=True):
                    if 'label' not in d:
                        pdg_graph.edges[u, v, k]['label'] = 'CFG'
                
                # 从 CPG 复制节点属性
                for node in pdg_graph.nodes:
                    if node in cpg.nodes:
                        for key, value in cpg.nodes[node].items():
                            pdg_graph.nodes[node][key] = value
                    
                    # 设置 NODE_TYPE
                    if 'label' in pdg_graph.nodes[node]:
                        pdg_graph.nodes[node]['NODE_TYPE'] = pdg_graph.nodes[node]['label']
                
                # 保存处理后的 PDG
                nx.nx_agraph.write_dot(pdg_graph, pdg_path)
                
            except Exception as e:
                logging.warning(f"Failed to preprocess {pdg_file}: {e}")
        
        logging.info("✓ PDG preprocessing complete")


class SingleFileSlicer:
    """单文件切片器"""
    
    def __init__(self):
        self.joern_analyzer = JoernAnalyzer()
        self.tasks = self._load_tasks()
        self.checkpoint_data = self._load_checkpoint()
        self.processed_count = 0
        self.chunk_results = []  # 当前chunk的结果
    
    def _load_tasks(self) -> List[Dict]:
        """加载切片任务"""
        logging.info(f"Loading tasks from {config.DATA_JSON}")
        
        if not os.path.exists(config.DATA_JSON):
            logging.error(f"Data file not found: {config.DATA_JSON}")
            return []
        
        with open(config.DATA_JSON, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        logging.info(f"Loaded {len(tasks)} tasks")
        return tasks
    
    def _load_checkpoint(self) -> Dict:
        """加载断点信息"""
        if not config.ENABLE_CHECKPOINT:
            return {"processed_indices": [], "chunk_count": 0}
        
        if os.path.exists(config.CHECKPOINT_FILE):
            try:
                with open(config.CHECKPOINT_FILE, 'r', encoding='utf-8') as f:
                    checkpoint = json.load(f)
                logging.info(f"Loaded checkpoint: {len(checkpoint.get('processed_indices', []))} tasks already processed")
                return checkpoint
            except Exception as e:
                logging.warning(f"Failed to load checkpoint: {e}")
        
        return {"processed_indices": [], "chunk_count": 0}
    
    def _save_checkpoint(self, processed_index: int):
        """保存断点信息"""
        if not config.ENABLE_CHECKPOINT:
            return
        
        self.checkpoint_data["processed_indices"].append(processed_index)
        
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        try:
            with open(config.CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.checkpoint_data, f, indent=2)
        except Exception as e:
            logging.warning(f"Failed to save checkpoint: {e}")
    
    def _save_chunk(self, chunk_results: List[Dict], chunk_index: int):
        """保存一个chunk的结果"""
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        chunk_file = os.path.join(config.OUTPUT_DIR, f"slices_chunk_{chunk_index:04d}.json")
        
        try:
            with open(chunk_file, 'w', encoding='utf-8') as f:
                json.dump(chunk_results, f, indent=2, ensure_ascii=False)
            logging.info(f"✓ Saved chunk {chunk_index} ({len(chunk_results)} items) to {chunk_file}")
            
            # 更新checkpoint
            self.checkpoint_data["chunk_count"] = chunk_index
            
            # 保存简化的summary
            summary_file = os.path.join(config.OUTPUT_DIR, f"slices_chunk_{chunk_index:04d}_summary.json")
            summary = []
            for r in chunk_results:
                summary_item = {
                    "project": r.get("project"),
                    "file": r.get("file"),
                    "line": r.get("line"),
                    "status": r.get("status"),
                    "function_name": r.get("function_name"),
                    "slice_lines_count": len(r.get("slice_lines", [])),
                    "enhanced_lines_count": len(r.get("enhanced_slice_lines", []))
                }
                if r.get("status") == "error":
                    summary_item["error"] = r.get("error")
                summary.append(summary_item)
            
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            
        except Exception as e:
            logging.error(f"Failed to save chunk {chunk_index}: {e}")
    
    def _save_progress(self, current_index: int, total: int, success: int, failed: int):
        """保存处理进度"""
        progress = {
            "current_index": current_index,
            "total_tasks": total,
            "processed": current_index + 1,
            "success": success,
            "failed": failed,
            "progress_percentage": ((current_index + 1) / total * 100) if total > 0 else 0,
            "timestamp": json.dumps(None)  # Will be replaced below
        }
        
        # Add timestamp
        import datetime
        progress["timestamp"] = datetime.datetime.now().isoformat()
        
        try:
            with open(config.PROGRESS_FILE, 'w', encoding='utf-8') as f:
                json.dump(progress, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logging.warning(f"Failed to save progress: {e}")
    
    def _load_source_file(self, project_version: str, file_path: str) -> Tuple[str, List[str]]:
        """
        加载源代码文件
        
        Returns:
            (完整文件路径, 代码行列表)
        """
        full_path = os.path.join(config.REPOSITORY_DIR, project_version, file_path)
        
        if not os.path.exists(full_path):
            raise SingleFileSlicerException(f"Source file not found: {full_path}")
        
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            return full_path, lines
        except Exception as e:
            raise SingleFileSlicerException(f"Failed to read {full_path}: {e}")
    
    def _find_pdg_for_line(self, pdg_dir: str, target_line: int, file_name: str) -> Optional[PDG]:
        """在 PDG 目录中查找包含目标行的 PDG"""
        
        for pdg_file in os.listdir(pdg_dir):
            if not pdg_file.endswith('-pdg.dot'):
                continue
            
            pdg_path = os.path.join(pdg_dir, pdg_file)
            try:
                pdg = PDG(pdg_path)
                
                # 检查文件名
                if pdg.filename and not pdg.filename.endswith(file_name):
                    continue
                
                # 检查行号范围
                if pdg.start_line and pdg.end_line:
                    if pdg.start_line <= target_line <= pdg.end_line:
                        return pdg
            except Exception as e:
                logging.debug(f"Failed to load {pdg_file}: {e}")
                continue
        
        return None
    
    def slice_one(self, task: Dict) -> Dict:
        """对单个任务执行切片"""
        project_name = task.get('project_name_with_version', 'unknown')
        file_path = task.get('file_path', 'unknown')
        target_line = task.get('line_number', 0)
        
        logging.info("\n" + "=" * 60)
        logging.info(f"Processing: {project_name} - {file_path}:{target_line}")
        
        result = {
            "project": project_name,
            "file": file_path,
            "line": target_line,
            "status": "pending"
        }
        
        temp_dir = None
        
        try:
            # 1. 加载源文件
            full_path, code_lines = self._load_source_file(project_name, file_path)
            logging.info(f"Loaded source file: {len(code_lines)} lines")
            
            # 2. 创建临时目录
            temp_dir = tempfile.mkdtemp(prefix="slice_")
            logging.info(f"Created temp directory: {temp_dir}")
            
            # 3. 使用 Joern 分析文件
            pdg_dir = self.joern_analyzer.analyze_file(full_path, temp_dir)
            
            # 4. 预处理 PDG
            cfg_dir = os.path.join(temp_dir, 'cfg')
            cpg_dir = os.path.join(temp_dir, 'cpg')
            if os.path.exists(cfg_dir) and os.path.exists(cpg_dir):
                self.joern_analyzer.preprocess_pdg(pdg_dir, cfg_dir, cpg_dir)
            
            # 5. 查找包含目标行的 PDG
            file_name = os.path.basename(file_path)
            pdg = self._find_pdg_for_line(pdg_dir, target_line, file_name)
            
            if not pdg:
                raise SingleFileSlicerException(f"No PDG found for line {target_line}")
            
            logging.info(f"Found PDG: {pdg}")
            result["function_name"] = pdg.method_name
            result["function_start_line"] = pdg.start_line
            result["function_end_line"] = pdg.end_line
            
            # 6. 执行切片，获取节点集
            engine = SliceEngine(pdg)
            slice_nodes, metadata = engine.slice(target_line)
            
            logging.info(f"Slice engine returned {len(slice_nodes)} nodes.")
            
            # 7. 提取切片行号
            slice_lines = {node.line_number for node in slice_nodes if node.line_number}
            
            # 8. AST 增强（如果启用）
            enhanced_lines = slice_lines
            ast_enhanced_success = False
            if config.ENABLE_AST_FIX:
                try:
                    from ast_enhancer import enhance_slice_with_ast
                    # 提取函数代码（而不是整个文件）
                    func_start_idx = (pdg.start_line or 1) - 1
                    func_end_idx = (pdg.end_line or len(code_lines))
                    func_code = "".join(code_lines[func_start_idx:func_end_idx])
                    
                    enhanced_lines = enhance_slice_with_ast(
                        source_code=func_code,
                        slice_lines=slice_lines,
                        language=config.LANGUAGE,
                        function_start_line=pdg.start_line or 1
                    )
                    ast_enhanced_success = len(enhanced_lines) > len(slice_lines)
                    logging.info(f"AST enhancement: {len(slice_lines)} -> {len(enhanced_lines)} lines (added {len(enhanced_lines) - len(slice_lines)} lines)")
                except Exception as e:
                    logging.warning(f"AST enhancement failed, using original slice: {e}")
                    import traceback
                    logging.debug(traceback.format_exc())
                    enhanced_lines = slice_lines
            
            # 9. 提取切片代码
            from code_extractor import extract_code
            
            # 构建源代码行字典（1-based）
            source_line_dict = {i + 1: line for i, line in enumerate(code_lines)}
            
            # 提取代码（无占位符）
            sliced_code = extract_code(
                slice_lines=enhanced_lines,
                source_lines=source_line_dict,
                placeholder=None
            )
            
            # 提取代码（带占位符）
            sliced_code_with_placeholder = extract_code(
                slice_lines=enhanced_lines,
                source_lines=source_line_dict,
                placeholder=config.PLACEHOLDER
            )
            
            # 10. 构建结果
            result["status"] = "success"
            result["slice_lines"] = sorted(list(slice_lines))
            result["enhanced_slice_lines"] = sorted(list(enhanced_lines))
            result["sliced_code"] = sliced_code
            result["sliced_code_with_placeholder"] = sliced_code_with_placeholder
            result["metadata"] = metadata
            
            # 更新元数据
            metadata["original_slice_lines"] = len(slice_lines)
            metadata["enhanced_slice_lines"] = len(enhanced_lines)
            metadata["final_node_count"] = len(slice_nodes)
            metadata["ast_enhanced"] = ast_enhanced_success
            
            logging.info(f"✓ Slice completed successfully")
            logging.info(f"  Function: {metadata.get('function_name', 'N/A')}")
            logging.info(f"  Final Lines: {metadata.get('total_slice_lines', 0)}")
            
        except SingleFileSlicerException as e:
            result["status"] = "error"
            result["error"] = str(e)
            logging.error(f"Slice failed: {e}")
        except Exception as e:
            result["status"] = "error"
            result["error"] = str(e)
            result["traceback"] = traceback.format_exc()
            logging.error(f"Unexpected error: {e}")
            logging.error(traceback.format_exc())
        finally:
            # 清理临时目录
            if temp_dir and os.path.exists(temp_dir):
                try:
                    shutil.rmtree(temp_dir)
                    logging.debug(f"Cleaned up temp directory: {temp_dir}")
                except Exception as e:
                    logging.warning(f"Failed to clean up {temp_dir}: {e}")
        
        return result
    
    def slice_all(self) -> List[Dict]:
        """对所有任务执行切片（支持断点续传和分chunk保存）"""
        chunk_results = []
        chunk_index = self.checkpoint_data.get("chunk_count", 0) + 1
        
        processed_indices = set(self.checkpoint_data.get("processed_indices", []))
        success_count = 0
        failed_count = 0
        
        logging.info(f"\nStarting batch slicing for {len(self.tasks)} tasks...")
        if processed_indices:
            logging.info(f"Resuming from checkpoint: {len(processed_indices)} tasks already processed")
        
        for i, task in enumerate(self.tasks):
            # 跳过已处理的任务
            if i in processed_indices:
                logging.debug(f"Skipping already processed task {i+1}/{len(self.tasks)}")
                continue
            
            logging.info(f"\n[{i+1}/{len(self.tasks)}] (Success: {success_count}, Failed: {failed_count})")
            
            # 执行切片
            result = self.slice_one(task)
            
            # 统计结果
            if result['status'] == 'success':
                success_count += 1
            else:
                failed_count += 1
            
            # 添加到当前chunk
            chunk_results.append(result)
            
            # 保存断点
            self._save_checkpoint(i)
            
            # 保存进度
            self._save_progress(i, len(self.tasks), success_count, failed_count)
            
            # 如果当前chunk已满，保存并开始新chunk
            if len(chunk_results) >= config.CHUNK_SIZE:
                self._save_chunk(chunk_results, chunk_index)
                chunk_results = []
                chunk_index += 1
        
        # 保存最后一个未满的chunk
        if chunk_results:
            self._save_chunk(chunk_results, chunk_index)
        
        # 统计
        total_processed = success_count + failed_count
        
        logging.info(f"\n{'='*60}")
        logging.info(f"Batch slicing completed!")
        logging.info(f"  Total: {len(self.tasks)}")
        logging.info(f"  Processed: {total_processed}")
        logging.info(f"  Success: {success_count} ({success_count/total_processed*100:.1f}%)" if total_processed > 0 else "  Success: 0")
        logging.info(f"  Failed: {failed_count} ({failed_count/total_processed*100:.1f}%)" if total_processed > 0 else "  Failed: 0")
        logging.info(f"  Saved in {chunk_index} chunks")
        
        # 自动合并所有chunk文件
        logging.info(f"\n{'='*60}")
        logging.info("Merging all chunk files...")
        self.merge_chunks()
        
        return []  # 不再返回所有结果，因为已经分chunk保存
    
    def save_results(self, results: List[Dict]):
        """
        合并所有chunk文件并保存最终结果
        注意：由于使用了分chunk保存，这个方法主要用于合并已有的chunk文件
        """
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        # 如果没有传入results，尝试从chunk文件加载
        if not results:
            logging.info("Loading results from chunk files...")
            results = self._load_all_chunks()
        
        if not results:
            logging.warning("No results to save")
            return
        
        output_path = config.OUTPUT_JSON
        logging.info(f"\nSaving merged results to {output_path}")
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            
            logging.info(f"✓ Results saved successfully ({len(results)} items)")
        except Exception as e:
            logging.error(f"Failed to save results: {e}")
            return
        
        # 保存简化版本
        summary_path = output_path.replace('.json', '_summary.json')
        summary = []
        for r in results:
            summary_item = {
                "project": r.get("project"),
                "file": r.get("file"),
                "line": r.get("line"),
                "status": r.get("status"),
                "function_name": r.get("function_name"),
                "slice_lines_count": len(r.get("slice_lines", [])),
                "enhanced_lines_count": len(r.get("enhanced_slice_lines", [])),
                "metadata": r.get("metadata", {})
            }
            if r.get("status") == "error":
                summary_item["error"] = r.get("error")
            summary.append(summary_item)
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        logging.info(f"✓ Summary saved to {summary_path}")
    
    def _load_all_chunks(self) -> List[Dict]:
        """加载所有chunk文件并合并"""
        all_results = []
        chunk_files = sorted([f for f in os.listdir(config.OUTPUT_DIR) 
                             if f.startswith('slices_chunk_') and f.endswith('.json') 
                             and '_summary' not in f])
        
        logging.info(f"Found {len(chunk_files)} chunk files")
        
        for chunk_file in chunk_files:
            chunk_path = os.path.join(config.OUTPUT_DIR, chunk_file)
            try:
                with open(chunk_path, 'r', encoding='utf-8') as f:
                    chunk_data = json.load(f)
                all_results.extend(chunk_data)
                logging.info(f"  Loaded {chunk_file}: {len(chunk_data)} items")
            except Exception as e:
                logging.warning(f"  Failed to load {chunk_file}: {e}")
        
        return all_results
    
    def merge_chunks(self):
        """合并所有chunk文件为最终结果文件"""
        logging.info("\nMerging all chunk files...")
        results = self._load_all_chunks()
        if results:
            self.save_results(results)
            logging.info(f"✓ Merged {len(results)} results from chunk files")
        else:
            logging.warning("No chunk files found to merge")
    
    def get_progress_info(self) -> Dict:
        """获取处理进度信息"""
        if os.path.exists(config.PROGRESS_FILE):
            try:
                with open(config.PROGRESS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logging.warning(f"Failed to load progress: {e}")
        return {}
    
    def clear_checkpoint(self):
        """清除断点信息（重新开始处理）"""
        if os.path.exists(config.CHECKPOINT_FILE):
            try:
                os.remove(config.CHECKPOINT_FILE)
                logging.info("✓ Checkpoint cleared")
            except Exception as e:
                logging.warning(f"Failed to clear checkpoint: {e}")
        
        if os.path.exists(config.PROGRESS_FILE):
            try:
                os.remove(config.PROGRESS_FILE)
                logging.info("✓ Progress file cleared")
            except Exception as e:
                logging.warning(f"Failed to clear progress: {e}")
        
        self.checkpoint_data = {"processed_indices": [], "chunk_count": 0}


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Single File Slicer for C/C++ Projects')
    parser.add_argument('--clear', action='store_true', 
                       help='Clear checkpoint and restart from beginning')
    parser.add_argument('--progress', action='store_true',
                       help='Show current progress')
    parser.add_argument('--chunk-size', type=int, default=None,
                       help='Override default chunk size')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Single File Slicer for C/C++ Projects")
    print("=" * 60)
    
    try:
        slicer = SingleFileSlicer()
        
        # 显示进度
        if args.progress:
            progress = slicer.get_progress_info()
            if progress:
                print(f"\nCurrent Progress:")
                print(f"  Processed: {progress.get('processed', 0)}/{progress.get('total_tasks', 0)}")
                print(f"  Progress: {progress.get('progress_percentage', 0):.1f}%")
                print(f"  Success: {progress.get('success', 0)}")
                print(f"  Failed: {progress.get('failed', 0)}")
                print(f"  Last Update: {progress.get('timestamp', 'N/A')}")
            else:
                print("\nNo progress information available")
            return 0
        
        # 清除断点
        if args.clear:
            print("\nClearing checkpoint...")
            slicer.clear_checkpoint()
        
        # 设置chunk大小
        if args.chunk_size:
            config.CHUNK_SIZE = args.chunk_size
            print(f"\nChunk size set to: {config.CHUNK_SIZE}")
        
        # 执行切片
        print(f"\nConfiguration:")
        print(f"  Chunk Size: {config.CHUNK_SIZE}")
        print(f"  Checkpoint Enabled: {config.ENABLE_CHECKPOINT}")
        print(f"  AST Enhancement: {config.ENABLE_AST_FIX}")
        
        # 执行切片 (完成后会自动合并chunk)
        slicer.slice_all()
        
        print("\n" + "=" * 60)
        print("Done!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        print("Progress has been saved. Run again to resume from checkpoint.")
        return 1
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
