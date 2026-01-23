"""
AST 增强模块
使用 tree-sitter 补充语法结构，确保切片代码语法正确
"""
from typing import Set, List, Dict
import logging

try:
    from tree_sitter import Parser, Node
    from tree_sitter_languages import get_parser, get_language
    TREE_SITTER_AVAILABLE = True
except ImportError:
    TREE_SITTER_AVAILABLE = False
    logging.warning("tree-sitter not available, AST enhancement disabled")


class ASTEnhancer:
    """AST 增强器"""
    
    def __init__(self, language: str = "c"):
        self.language = language
        
        if not TREE_SITTER_AVAILABLE:
            raise RuntimeError("tree-sitter is required for AST enhancement")
        
        # 使用 tree-sitter-languages 简化的 API
        try:
            self.parser = get_parser(language)
            logging.info(f"ASTEnhancer initialized for language: {language}")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize parser for {language}: {e}")
    
    def enhance_slice(self, 
                     source_code: str, 
                     slice_lines: Set[int],
                     function_start_line: int = 1) -> Set[int]:
        """
        增强切片，补充必要的语法结构
        
        Args:
            source_code: 完整的源代码
            slice_lines: 切片行号集合（绝对行号）
            function_start_line: 函数起始行号
        
        Returns:
            增强后的行号集合
        """
        if not slice_lines:
            return slice_lines
        
        # 解析 AST
        tree = self.parser.parse(bytes(source_code, "utf8"))
        root = tree.root_node
        
        # 转换为相对行号（tree-sitter 使用 0-based，源代码从第1行开始）
        rel_slice_lines = {line - function_start_line + 1 for line in slice_lines}
        
        # 查找函数节点（源代码是从函数开始的，所以目标行是1）
        function_node = self._find_function_node(root, 1)
        if not function_node:
            logging.warning(f"Function node not found in parsed tree (root type: {root.type}, children: {[c.type for c in root.children[:5]]})")
            return slice_lines
        
        logging.debug(f"Found function node: {function_node.type} at lines {function_node.start_point[0]+1}-{function_node.end_point[0]+1}")
        
        body_node = function_node.child_by_field_name("body")
        if not body_node:
            logging.warning("Function body not found")
            return slice_lines
        
        # 1. 补全函数签名
        enhanced_lines = self._complete_function_signature(function_node, rel_slice_lines)
        
        # 2. 应用增强（使用相对行号）
        enhanced_lines = self._ast_dive_c(body_node, enhanced_lines, 1)
        enhanced_lines = self._ast_add(body_node, enhanced_lines, 1)
        enhanced_lines = self._ast_trim(body_node, enhanced_lines, 1)
        
        # 转换回绝对行号
        abs_enhanced_lines = {line + function_start_line - 1 for line in enhanced_lines}
        
        logging.info(f"AST enhancement: {len(slice_lines)} -> {len(abs_enhanced_lines)} lines")
        
        return abs_enhanced_lines
    
    def _find_function_node(self, root: Node, target_line: int) -> Node:
        """查找包含目标行的函数节点"""
        
        def _search(node: Node) -> Node:
            if node.type == "function_definition":
                start_line = node.start_point[0] + 1
                end_line = node.end_point[0] + 1
                if start_line <= target_line <= end_line:
                    return node
            
            for child in node.children:
                result = _search(child)
                if result:
                    return result
            
            return None
        
        return _search(root)
    
    def _complete_function_signature(self, function_node: Node, slice_lines: Set[int]) -> Set[int]:
        """
        补全函数签名
        如果切片包含函数签名的任何部分，则添加完整的函数签名（包括所有参数和开始括号）
        
        Args:
            function_node: 函数节点
            slice_lines: 切片行号（相对行号）
        
        Returns:
            增强后的行号集合
        """
        enhanced = slice_lines.copy()
        
        # 获取函数签名的范围（从函数开始到函数体开始括号之前）
        func_start = function_node.start_point[0] + 1
        
        # 获取函数体节点
        body_node = function_node.child_by_field_name("body")
        if body_node:
            # 函数体的开始行就是 { 的位置
            body_start = body_node.start_point[0] + 1
            
            # 检查切片是否包含函数签名的任何部分
            signature_lines = set(range(func_start, body_start + 1))  # 包括开始括号
            if signature_lines & slice_lines:
                # 如果包含，则添加完整的函数签名
                logging.debug(f"Completing function signature: lines {func_start}-{body_start}")
                enhanced.update(signature_lines)
        
        return enhanced
    
    def _is_in_node(self, line: int, node: Node, offset: int) -> bool:
        """检查行号是否在节点范围内"""
        node_start = node.start_point[0] + 1 + offset - 1
        node_end = node.end_point[0] + 1 + offset - 1
        return node_start <= line <= node_end
    
    def _ast_dive_c(self, root: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """
        深入 AST，补充必要的语法结构
        
        Args:
            root: 根节点
            slice_lines: 切片行号（相对于函数）
            offset: 函数起始行偏移
        """
        enhanced_lines = slice_lines.copy()
        
        for node in root.children:
            if not node.is_named:
                continue
            
            node_start = node.start_point[0] + 1
            node_end = node.end_point[0] + 1
            
            # 检查该节点是否与切片相交
            intersect = any(self._is_in_node(line, node, offset) for line in slice_lines)
            if not intersect:
                continue
            
            # 处理不同类型的节点
            if node.type == "if_statement":
                enhanced_lines = self._handle_if_statement(node, enhanced_lines, offset)
            elif node.type == "for_statement":
                enhanced_lines = self._handle_for_statement(node, enhanced_lines, offset)
            elif node.type == "while_statement":
                enhanced_lines = self._handle_while_statement(node, enhanced_lines, offset)
            elif node.type == "switch_statement":
                enhanced_lines = self._handle_switch_statement(node, enhanced_lines, offset)
            elif node.type == "compound_statement":
                # 递归处理
                enhanced_lines.add(node_start)
                enhanced_lines.add(node_end)
                enhanced_lines = self._ast_dive_c(node, enhanced_lines, offset)
        
        return enhanced_lines
    
    def _handle_if_statement(self, node: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """处理 if 语句"""
        enhanced = slice_lines.copy()
        
        # 添加 if 关键字行
        enhanced.add(node.start_point[0] + 1)
        
        # 添加条件
        condition = node.child_by_field_name("condition")
        if condition:
            enhanced.add(condition.start_point[0] + 1)
            enhanced.add(condition.end_point[0] + 1)
        
        # 添加 consequence
        consequence = node.child_by_field_name("consequence")
        if consequence:
            enhanced.add(consequence.start_point[0] + 1)
            enhanced.add(consequence.end_point[0] + 1)
            if consequence.type == "compound_statement":
                enhanced = self._ast_dive_c(consequence, enhanced, offset)
        
        # 添加 alternative (else)
        alternative = node.child_by_field_name("alternative")
        if alternative:
            enhanced.add(alternative.start_point[0] + 1)
            if alternative.type != "if_statement":
                enhanced.add(alternative.end_point[0] + 1)
            if alternative.type == "compound_statement":
                enhanced = self._ast_dive_c(alternative, enhanced, offset)
            elif alternative.type == "if_statement":
                enhanced = self._handle_if_statement(alternative, enhanced, offset)
        
        return enhanced
    
    def _handle_for_statement(self, node: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """处理 for 循环"""
        enhanced = slice_lines.copy()
        
        # 添加 for 关键字行
        enhanced.add(node.start_point[0] + 1)
        
        # 添加循环体
        body = node.child_by_field_name("body")
        if body:
            enhanced.add(body.start_point[0] + 1)
            enhanced.add(body.end_point[0] + 1)
            if body.type == "compound_statement":
                enhanced = self._ast_dive_c(body, enhanced, offset)
        
        return enhanced
    
    def _handle_while_statement(self, node: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """处理 while 循环"""
        enhanced = slice_lines.copy()
        
        # 添加 while 关键字行
        enhanced.add(node.start_point[0] + 1)
        
        # 添加条件
        condition = node.child_by_field_name("condition")
        if condition:
            enhanced.add(condition.start_point[0] + 1)
        
        # 添加循环体
        body = node.child_by_field_name("body")
        if body:
            enhanced.add(body.start_point[0] + 1)
            enhanced.add(body.end_point[0] + 1)
            if body.type == "compound_statement":
                enhanced = self._ast_dive_c(body, enhanced, offset)
        
        return enhanced
    
    def _handle_switch_statement(self, node: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """处理 switch 语句"""
        enhanced = slice_lines.copy()
        
        # 添加 switch 关键字和条件
        enhanced.add(node.start_point[0] + 1)
        
        condition = node.child_by_field_name("condition")
        if condition:
            enhanced.add(condition.start_point[0] + 1)
        
        # 添加 body
        body = node.child_by_field_name("body")
        if body:
            enhanced.add(body.start_point[0] + 1)
            enhanced.add(body.end_point[0] + 1)
            enhanced = self._ast_dive_c(body, enhanced, offset)
        
        return enhanced
    
    def _ast_add(self, root: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """
        添加控制流关键语句
        如果切片包含某个控制结构，则添加其 break/return/goto 等
        """
        # TODO: 实现更复杂的控制流分析
        # 目前保持简单，只返回原始行集
        return slice_lines
    
    def _ast_trim(self, root: Node, slice_lines: Set[int], offset: int) -> Set[int]:
        """
        修剪不必要的节点
        例如：移除空的 if 语句
        """
        # TODO: 实现节点修剪
        return slice_lines


def enhance_slice_with_ast(source_code: str, 
                          slice_lines: Set[int],
                          language: str = "c",
                          function_start_line: int = 1) -> Set[int]:
    """
    使用 AST 增强切片的便捷函数
    
    Args:
        source_code: 完整源代码
        slice_lines: 切片行号集合
        language: 编程语言
        function_start_line: 函数起始行
    
    Returns:
        增强后的行号集合
    """
    if not TREE_SITTER_AVAILABLE:
        logging.warning("tree-sitter not available, returning original slice")
        return slice_lines
    
    try:
        enhancer = ASTEnhancer(language)
        return enhancer.enhance_slice(source_code, slice_lines, function_start_line)
    except Exception as e:
        logging.error(f"AST enhancement failed: {e}")
        return slice_lines
