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

import networkx as nx
from tree_sitter import Language, Parser

import config
from pdg_loader import PDG, PDGNode
from slice_engine import SliceEngine


try:
    # 假设 tree-sitter-c 已经安装并可用
    # 通常需要指定 .so 文件路径，但如果已在环境中正确设置，则可以省略
    C_LANGUAGE = Language(config.TREE_SITTER_SO_FILE, 'c')
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    TREE_SITTER_AVAILABLE = True
except (ImportError, Exception) as e:
    TREE_SITTER_AVAILABLE = False
    logging.warning(f"Tree-sitter not available. Code restoration will be skipped. Error: {e}")
    logging.warning(traceback.format_exc())


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


class AstRestorer:
    """
    使用 Tree-sitter 从切片节点恢复语法正确的代码。
    """
    def __init__(self, pdg: PDG, source_lines: List[str]):
        if not TREE_SITTER_AVAILABLE:
            raise SingleFileSlicerException("Tree-sitter is not available for AstRestorer.")
        
        self.pdg = pdg
        self.source_lines = source_lines
        self.source_code_bytes = "".join(source_lines).encode('utf-8')
        self.tree = parser.parse(self.source_code_bytes)
        self.ast_closure_nodes: Set[int] = set()

    def _get_node_line_range(self, node) -> Tuple[int, int]:
        # tree-sitter 的行号是 0-indexed, Joern 是 1-indexed
        return node.start_point[0] + 1, node.end_point[0] + 1

    def restore_code(self, slice_nodes: Set[PDGNode], criterion_line: int) -> str:
        """
        将切片节点恢复为语法正确的代码块，并为切片行添加注释。
        确保代码行按原始顺序排列，且不重复。

        Args:
            slice_nodes: 切片引擎返回的节点集合。
            criterion_line: 切片准则的行号。

        Returns:
            带有注释的、恢复的代码字符串。
        """
        slice_line_numbers = {node.line_number for node in slice_nodes if node.line_number is not None}
        if not slice_line_numbers:
            return ""

        restored_lines = []
        # 遍历源文件的每一行，以保证顺序
        for i, line_content in enumerate(self.source_lines):
            current_line_num = i + 1
            if current_line_num in slice_line_numbers:
                line_to_add = line_content.rstrip()
                if current_line_num == criterion_line:
                    # 这是切片准则行，添加注释
                    line_to_add += config.CRITERION_LINE_COMMENT
                # 对于其他切片行，不再添加 SLICE_LINE_COMMENT
                restored_lines.append(line_to_add)

        # 记录最终用于恢复代码的 PDG 节点
        self.ast_closure_nodes = {
            node.node_id for node in self.pdg.nodes.values()
            if node.line_number in slice_line_numbers
        }

        return "\n".join(restored_lines)

    def _get_ancestors(self, node):
        """获取一个节点的所有祖先节点"""
        ancestors = []
        current = node.parent
        while current:
            ancestors.append(current)
            current = current.parent
        return ancestors

    def _record_final_ast_nodes(self, top_level_nodes: List):
        """
        从恢复的 AST 节点反推，记录所有涉及的 PDG 节点 ID
        """
        final_lines = set()
        for ast_node in top_level_nodes:
            start, end = self._get_node_line_range(ast_node)
            for line in range(start, end + 1):
                final_lines.add(line)
        
        self.ast_closure_nodes = {
            node.node_id for node in self.pdg.nodes.values() 
            if node.line_number in final_lines
        }


class SingleFileSlicer:
    """单文件切片器"""
    
    def __init__(self):
        self.joern_analyzer = JoernAnalyzer()
        self.tasks = self._load_tasks()
    
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
            
            # 7. 使用 AST Restorer 恢复代码
            restorer = AstRestorer(pdg, code_lines)
            sliced_code = restorer.restore_code(slice_nodes, target_line)
            
            # 8. 提取切片行号（用于元数据）
            final_node_ids = restorer.ast_closure_nodes
            slice_lines = {pdg.get_node(nid).line_number for nid in final_node_ids if pdg.get_node(nid) and pdg.get_node(nid).line_number}

            # 9. 构建结果
            result["status"] = "success"
            result["sliced_code"] = sliced_code
            result["slice_lines"] = sorted(list(slice_lines))
            
            # 将原始任务数据和新的元数据合并
            metadata["original_data"] = task
            result["metadata"] = metadata
            
            # 更新元数据
            metadata["total_slice_lines"] = len(slice_lines)
            metadata["final_node_count"] = len(final_node_ids)
            
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
    
    def _load_processed_chunks(self) -> Set[int]:
        """加载已处理的 chunk 索引"""
        processed = set()
        if os.path.exists(config.PROCESSED_LOG):
            with open(config.PROCESSED_LOG, 'r') as f:
                for line in f:
                    try:
                        processed.add(int(line.strip()))
                    except ValueError:
                        pass
        return processed

    def _log_processed_chunk(self, chunk_index: int):
        """记录已处理的 chunk"""
        with open(config.PROCESSED_LOG, 'a') as f:
            f.write(f"{chunk_index}\n")

    def slice_all(self):
        """对所有任务执行分块切片"""
        tasks = self.tasks
        total_tasks = len(tasks)
        chunk_size = config.CHUNK_SIZE
        
        processed_chunks = self._load_processed_chunks()
        logging.info(f"Found {len(processed_chunks)} already processed chunks.")

        for i in range(0, total_tasks, chunk_size):
            chunk_index = i // chunk_size
            if chunk_index in processed_chunks:
                logging.info(f"Skipping chunk {chunk_index} (tasks {i} to {i + chunk_size - 1}) as it's already processed.")
                continue

            chunk_tasks = tasks[i:i + chunk_size]
            chunk_results = []
            
            logging.info(f"\nStarting chunk {chunk_index} (tasks {i} to {i + len(chunk_tasks) - 1})")

            for j, task in enumerate(chunk_tasks, 1):
                logging.info(f"\n[Chunk {chunk_index} | Task {j}/{len(chunk_tasks)} | Total {i+j}/{total_tasks}]")
                result = self.slice_one(task)
                chunk_results.append(result)

            # 保存当前 chunk 的结果
            self.save_chunk_results(chunk_results, chunk_index)
            self._log_processed_chunk(chunk_index)

        logging.info("\nAll chunks processed.")

    def save_chunk_results(self, results: List[Dict], chunk_index: int):
        """保存单个 chunk 的结果"""
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        chunk_filename = os.path.join(config.OUTPUT_DIR, f"slices_chunk_{chunk_index}.json")
        logging.info(f"Saving chunk {chunk_index} results to {chunk_filename}")
        with open(chunk_filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        logging.info(f"✓ Chunk {chunk_index} results saved.")

    def merge_chunks(self):
        """合并所有 chunk 的结果"""
        logging.info("\nMerging all chunk results...")
        all_results = []
        output_dir = config.OUTPUT_DIR
        
        chunk_files = [f for f in os.listdir(output_dir) if f.startswith('slices_chunk_') and f.endswith('.json')]
        # 按数字顺序排序
        chunk_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

        for filename in chunk_files:
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_results.extend(data)
                logging.info(f"Loaded {len(data)} results from {filename}")
            except (json.JSONDecodeError, IOError) as e:
                logging.error(f"Failed to load or parse {filename}: {e}")

        self.save_results(all_results)
        
        # 清理 chunk 文件和日志
        if config.CLEANUP_CHUNKS:
            logging.info("Cleaning up chunk files and log...")
            for filename in chunk_files:
                os.remove(os.path.join(output_dir, filename))
            if os.path.exists(config.PROCESSED_LOG):
                os.remove(config.PROCESSED_LOG)
            logging.info("✓ Cleanup complete.")

    def save_results(self, results: List[Dict]):
        """保存最终合并的结果"""
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        
        output_path = config.MERGED_SLICES_FILE
        logging.info(f"\nSaving merged results to {output_path}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        logging.info(f"✓ Merged results saved successfully ({len(results)} items).")
        
        # 保存简化版本
        summary_path = output_path.replace('.json', '_summary.json')
        summary = []
        for r in results:
            # 提取元数据，如果不存在则为空字典
            metadata = r.get("metadata", {})
            original_data = metadata.get("original_data", {})

            summary_item = {
                "project": original_data.get("project_name_with_version"),
                "file": original_data.get("file_path"),
                "target_line": original_data.get("line_number"),
                "status": r.get("status"),
                "function_name": metadata.get("function_name"),
                "slice_lines_count": len(r.get("slice_lines", [])),
            }
            if r.get("status") == "error":
                summary_item["error"] = r.get("error")
            summary.append(summary_item)
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        logging.info(f"✓ Summary saved to {summary_path}")


def main():
    """主函数"""
    print("=" * 60)
    print("Single File Slicer for C/C++ Projects")
    print("=" * 60)
    
    try:
        slicer = SingleFileSlicer()
        slicer.slice_all()
        slicer.merge_chunks()
        
        print("\n" + "=" * 60)
        print("Done!")
        print("=" * 60)
        
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return 1
    except Exception as e:
        print(f"\n\nFatal error: {e}")
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
