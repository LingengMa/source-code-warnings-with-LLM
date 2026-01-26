"""
切片引擎核心逻辑
实现基于 PDG 的前向和后向切片算法
"""
import logging
from collections import deque
from typing import Set, List, Tuple, Dict, Optional
from pdg_loader import PDG, PDGNode
import config


class SliceEngine:
    """程序切片引擎"""
    
    def __init__(self, pdg: PDG):
        self.pdg = pdg
        self.visited_nodes: Set[int] = set()

    def backward_slice(self, 
                      criteria_nodes: List[PDGNode], 
                      criteria_identifier: Dict[int, Set[str]] = None,
                      depth: int = config.BACKWARD_DEPTH) -> Set[PDGNode]:
        """
        后向切片：从切片准则向上追溯依赖
        
        Args:
            criteria_nodes: 切片准则节点列表
            criteria_identifier: 行号 -> 标识符集合的映射（用于精确切片）
            depth: 切片深度
            
        Returns:
            切片节点集合
        """
        if criteria_identifier is None:
            criteria_identifier = {}
        
        result_nodes: Set[PDGNode] = set()
        queue = deque([(node, 0) for node in criteria_nodes])
        visited_ids = {node.node_id for node in criteria_nodes}
        
        while queue:
            node, current_depth = queue.popleft()
            
            result_nodes.add(node)
            
            # 达到深度限制
            if current_depth >= depth:
                continue
            
            # 获取前驱节点（DDG 和 CDG）
            preds = self.pdg.get_predecessors(node.node_id, config.DDG_LABEL)
            preds.extend(self.pdg.get_predecessors(node.node_id, config.CDG_LABEL))
            
            for pred_node, edge_label in preds:
                if pred_node.node_id in visited_ids:
                    continue
                
                # 如果指定了标识符过滤
                if node.line_number in criteria_identifier:
                    edge_var = edge_label.replace(config.DDG_LABEL + ': ', '').replace(config.CDG_LABEL + ': ', '')
                    if edge_var and edge_var not in criteria_identifier[node.line_number]:
                        continue
                
                visited_ids.add(pred_node.node_id)
                queue.append((pred_node, current_depth + 1))
        
        return result_nodes
    
    def forward_slice(self,
                     criteria_nodes: List[PDGNode],
                     criteria_identifier: Dict[int, Set[str]] = None,
                     depth: int = config.FORWARD_DEPTH) -> Set[PDGNode]:
        """
        前向切片：从切片准则向下追踪影响
        
        Args:
            criteria_nodes: 切片准则节点列表
            criteria_identifier: 行号 -> 标识符集合的映射
            depth: 切片深度
            
        Returns:
            切片节点集合
        """
        if criteria_identifier is None:
            criteria_identifier = {}
        
        result_nodes: Set[PDGNode] = set()
        queue = deque([(node, 0) for node in criteria_nodes])
        visited_ids = {node.node_id for node in criteria_nodes}
        
        while queue:
            node, current_depth = queue.popleft()
            
            result_nodes.add(node)
            
            # 达到深度限制
            if current_depth >= depth:
                continue
            
            # 获取后继节点（DDG 和 CDG）
            succs = self.pdg.get_successors(node.node_id, config.DDG_LABEL)
            succs.extend(self.pdg.get_successors(node.node_id, config.CDG_LABEL))
            
            for succ_node, edge_label in succs:
                if succ_node.node_id in visited_ids:
                    continue
                
                # 如果指定了标识符过滤
                if node.line_number in criteria_identifier:
                    edge_var = edge_label.replace(config.DDG_LABEL + ': ', '').replace(config.CDG_LABEL + ': ', '')
                    if edge_var and edge_var not in criteria_identifier[node.line_number]:
                        continue
                
                visited_ids.add(succ_node.node_id)
                queue.append((succ_node, current_depth + 1))
        
        return result_nodes
    
    def slice(self, 
             target_line: int,
             criteria_identifier: Dict[int, Set[str]] = None,
             backward_depth: int = config.BACKWARD_DEPTH,
             forward_depth: int = config.FORWARD_DEPTH) -> Tuple[Set[PDGNode], Dict]:
        """
        执行完整的双向切片，返回节点集合
        
        Args:
            target_line: 目标行号
            criteria_identifier: 标识符过滤字典
            backward_depth: 后向切片深度
            forward_depth: 前向切片深度
            
        Returns:
            (切片节点集合, 元数据字典)
        """
        # 查找目标行的节点
        criteria_nodes = self.pdg.get_nodes_by_line(target_line)
        if not criteria_nodes:
            logging.warning(f"No nodes found for line {target_line}")
            return set(), {}
        
        logging.info(f"Found {len(criteria_nodes)} nodes for line {target_line}")
        
        # 后向切片
        backward_nodes = self.backward_slice(
            criteria_nodes, criteria_identifier, backward_depth
        )
        
        # 前向切片
        forward_nodes = self.forward_slice(
            criteria_nodes, criteria_identifier, forward_depth
        )
        
        # 合并所有节点
        all_slice_nodes = backward_nodes.union(forward_nodes)
        
        # 提取行号用于元数据统计
        slice_lines = {node.line_number for node in all_slice_nodes if node.line_number}

        # 元数据
        metadata = {
            "function_name": self.pdg.method_name,
            "function_start_line": self.pdg.start_line,
            "function_end_line": self.pdg.end_line,
            "target_line": target_line,
            "backward_nodes": len(backward_nodes),
            "forward_nodes": len(forward_nodes) - len(criteria_nodes), # 减去重复的准则节点
            "total_slice_nodes": len(all_slice_nodes),
            "total_slice_lines": len(slice_lines),
            "slice_density": len(slice_lines) / (self.pdg.end_line - self.pdg.start_line + 1) if self.pdg.end_line and self.pdg.start_line else 0
        }
        
        logging.info(f"Slice complete: {len(all_slice_nodes)} nodes found.")
        
        return all_slice_nodes, metadata
