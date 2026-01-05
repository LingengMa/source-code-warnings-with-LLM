#!/usr/bin/env python3
"""
C/C++ Semantic Slicer - Single-file, multi-function semantic slicing
"""

import os
import json
from typing import Set, Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import tree_sitter_c as tsc
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser, Node


@dataclass
class SliceResult:
    """切片结果"""
    target_line: int
    target_file: str
    anchors: Set[str]  # 语义锚点
    slice_lines: Set[int]  # 切片包含的行号
    function_map: Dict[int, str]  # 行号到函数名的映射
    
    def to_dict(self):
        return {
            'target_line': self.target_line,
            'target_file': self.target_file,
            'anchors': list(self.anchors),
            'slice_lines': sorted(list(self.slice_lines)),
            'function_map': {str(k): v for k, v in self.function_map.items()}
        }


@dataclass
class Statement:
    """语句信息"""
    node: Node
    start_line: int
    end_line: int
    function_name: Optional[str] = None
    defs: Set[str] = field(default_factory=set)  # 定义的变量
    uses: Set[str] = field(default_factory=set)  # 使用的变量
    control_deps: Set[int] = field(default_factory=set)  # 控制依赖的语句行号
    called_functions: Set[str] = field(default_factory=set)  # 调用的函数
    is_global_access: bool = False  # 是否访问全局变量
    pointer_defs: Set[str] = field(default_factory=set)  # 通过指针定义的变量
    pointer_uses: Set[str] = field(default_factory=set)  # 通过指针使用的变量
    may_alias: Dict[str, Set[str]] = field(default_factory=dict)  # 可能的别名关系
    array_accesses: Set[str] = field(default_factory=set)  # 数组访问
    field_accesses: Dict[str, Set[str]] = field(default_factory=dict)  # 结构体字段访问 {obj: {fields}}
    modified_by_call: Set[str] = field(default_factory=set)  # 通过函数调用可能修改的变量


@dataclass
class FunctionInfo:
    """函数信息"""
    name: str
    start_line: int
    end_line: int
    params: List[str] = field(default_factory=list)  # 参数列表（有序）
    param_types: Dict[str, str] = field(default_factory=dict)  # 参数类型
    pointer_params: Set[str] = field(default_factory=set)  # 指针/引用参数
    return_vars: Set[str] = field(default_factory=set)  # 返回语句中的变量
    return_type: Optional[str] = None  # 返回类型
    modifies_globals: Set[str] = field(default_factory=set)  # 修改的全局变量
    may_modify_params: Set[str] = field(default_factory=set)  # 可能修改的指针/引用参数
    calls: Set[str] = field(default_factory=set)  # 直接调用的函数
    is_recursive: bool = False  # 是否递归


class CSemanticSlicer:
    """C/C++ 语义切片器"""
    
    def __init__(self, is_cpp: bool = False):
        self.is_cpp = is_cpp
        if is_cpp:
            self.language = Language(tscpp.language())
        else:
            self.language = Language(tsc.language())
        self.parser = Parser(self.language)
        # 函数级作用域信息
        self.function_scopes = {}  # {function_name: {local_vars, params}}
        self.global_vars = set()  # 全局变量
        self.function_defs = {}  # {function_name: start_line}
        self.function_info = {}  # {function_name: FunctionInfo}
        self.call_graph = defaultdict(set)  # {caller: {callees}}
        self.pointer_aliases = defaultdict(set)  # {var: {possible_aliases}}
        self.type_info = {}  # {var_name: type_str}  # 变量类型信息
        self.struct_fields = defaultdict(set)  # {struct_name: {fields}}  # 结构体字段
        self.field_to_struct = {}  # {(var, field): struct_type}  # 字段访问记录
        
    def parse_file(self, file_path: str) -> Optional[Node]:
        """解析源文件"""
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            tree = self.parser.parse(content)
            return tree.root_node
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            return None
    
    def get_line_range(self, node: Node) -> Tuple[int, int]:
        """获取节点的行范围（1-based）"""
        return node.start_point[0] + 1, node.end_point[0] + 1
    
    def is_target_line_in_node(self, node: Node, target_line: int) -> bool:
        """检查目标行是否在节点范围内"""
        start_line, end_line = self.get_line_range(node)
        return start_line <= target_line <= end_line
    
    def extract_identifiers(self, node: Node) -> Set[str]:
        """提取节点中的所有标识符"""
        identifiers = set()
        
        def visit(n: Node):
            if n.type == 'identifier':
                identifiers.add(n.text.decode('utf-8'))
            for child in n.children:
                visit(child)
        
        visit(node)
        return identifiers
    
    def extract_anchors(self, node: Node, source_code: bytes, target_line: int) -> Set[str]:
        """提取目标行的语义锚点"""
        anchors = set()
        
        # 查找包含目标行的最小语句节点
        target_node = self.find_statement_at_line(node, target_line)
        if not target_node:
            return anchors
        
        def visit(n: Node):
            start_line, end_line = self.get_line_range(n)
            
            # 只处理在目标行上的节点
            if start_line > target_line or end_line < target_line:
                return
            
            # 变量声明
            if n.type in ['declaration', 'init_declarator']:
                for child in n.children:
                    if child.type == 'identifier':
                        anchors.add(child.text.decode('utf-8'))
            
            # 赋值表达式
            elif n.type == 'assignment_expression':
                left = n.child_by_field_name('left')
                if left:
                    identifiers = self.extract_identifiers(left)
                    anchors.update(identifiers)
            
            # 函数调用
            elif n.type == 'call_expression':
                func = n.child_by_field_name('function')
                if func and func.type == 'identifier':
                    anchors.add(func.text.decode('utf-8'))
                # 参数中的标识符
                args = n.child_by_field_name('arguments')
                if args:
                    identifiers = self.extract_identifiers(args)
                    anchors.update(identifiers)
            
            # 变量引用
            elif n.type == 'identifier':
                anchors.add(n.text.decode('utf-8'))
            
            for child in n.children:
                visit(child)
        
        visit(target_node)
        return anchors
    
    def find_statement_at_line(self, root: Node, target_line: int) -> Optional[Node]:
        """查找包含目标行的语句节点"""
        candidates = []
        
        def visit(n: Node):
            start_line, end_line = self.get_line_range(n)
            if start_line <= target_line <= end_line:
                if n.type in ['expression_statement', 'declaration', 'return_statement',
                              'if_statement', 'while_statement', 'for_statement',
                              'assignment_expression', 'call_expression']:
                    candidates.append(n)
                for child in n.children:
                    visit(child)
        
        visit(root)
        
        # 返回最小的包含节点
        if candidates:
            return min(candidates, key=lambda n: n.end_byte - n.start_byte)
        return None
    
    def extract_definitions(self, node: Node) -> Set[str]:
        """提取节点中定义的变量"""
        defs = set()
        
        # 声明语句
        if node.type == 'declaration':
            for child in node.children:
                if child.type == 'init_declarator':
                    declarator = child.child_by_field_name('declarator')
                    if declarator:
                        name = self.extract_declarator_name(declarator)
                        if name:
                            defs.add(name)
                elif child.type in ['identifier', 'pointer_declarator', 'array_declarator']:
                    name = self.extract_declarator_name(child)
                    if name:
                        defs.add(name)
        
        # 赋值表达式
        elif node.type == 'assignment_expression':
            left = node.child_by_field_name('left')
            if left:
                if left.type == 'identifier':
                    defs.add(left.text.decode('utf-8'))
                elif left.type == 'subscript_expression':
                    # 数组元素赋值，认为是对数组的修改
                    arr = left.child_by_field_name('argument')
                    if arr and arr.type == 'identifier':
                        defs.add(arr.text.decode('utf-8'))
                elif left.type == 'field_expression':
                    # 结构体字段赋值
                    # 提取最外层的对象标识符
                    obj = left.child_by_field_name('argument')
                    while obj:
                        if obj.type == 'identifier':
                            defs.add(obj.text.decode('utf-8'))
                            break
                        elif obj.type == 'field_expression':
                            obj = obj.child_by_field_name('argument')
                        else:
                            break
                elif left.type == 'pointer_expression':
                    # 指针解引用赋值
                    arg = left.child_by_field_name('argument')
                    if arg and arg.type == 'identifier':
                        defs.add(arg.text.decode('utf-8'))
        
        # 更新表达式 (++, --)
        elif node.type == 'update_expression':
            arg = node.child_by_field_name('argument')
            if arg and arg.type == 'identifier':
                defs.add(arg.text.decode('utf-8'))
        
        return defs
    
    def extract_uses(self, node: Node) -> Set[str]:
        """提取节点中使用的变量"""
        uses = set()
        defs = self.extract_definitions(node)
        
        def visit(n: Node, skip_identifier: bool = False):
            # 跳过声明中的标识符
            if n.type == 'declaration':
                # 只处理初始化表达式
                for child in n.children:
                    if child.type == 'init_declarator':
                        init = child.child_by_field_name('value')
                        if init:
                            visit(init, False)
            elif n.type == 'assignment_expression':
                # 左侧可能有使用（如数组索引、指针解引用）
                left = n.child_by_field_name('left')
                if left:
                    if left.type == 'subscript_expression':
                        # 数组名和索引都是使用
                        arr = left.child_by_field_name('argument')
                        index = left.child_by_field_name('index')
                        if arr:
                            visit(arr, False)
                        if index:
                            visit(index, False)
                    elif left.type == 'pointer_expression':
                        # 指针解引用
                        visit(left.child_by_field_name('argument'), False)
                    elif left.type == 'field_expression':
                        # 结构体字段访问，对象是使用
                        obj = left.child_by_field_name('argument')
                        if obj:
                            visit(obj, False)
                # 右侧是使用
                right = n.child_by_field_name('right')
                if right:
                    visit(right, False)
            elif n.type == 'identifier' and not skip_identifier:
                uses.add(n.text.decode('utf-8'))
            elif n.type in ['call_expression', 'subscript_expression', 
                           'field_expression', 'pointer_expression']:
                # 这些表达式中的所有标识符都是使用
                for child in n.children:
                    visit(child, False)
            else:
                for child in n.children:
                    visit(child, skip_identifier)
        
        visit(node)
        # 移除定义的变量
        return uses - defs
    
    def build_statements(self, root: Node, source_code: bytes) -> Dict[int, Statement]:
        """构建文件中所有语句的信息"""
        statements = {}
        current_function = None
        
        def extract_function_calls(node: Node) -> Set[str]:
            """提取节点中的函数调用"""
            calls = set()
            
            def visit(n: Node):
                if n.type == 'call_expression':
                    func = n.child_by_field_name('function')
                    if func and func.type == 'identifier':
                        calls.add(func.text.decode('utf-8'))
                for child in n.children:
                    visit(child)
            
            visit(node)
            return calls
        
        def visit(n: Node, func_name: Optional[str] = None):
            nonlocal current_function
            
            # 跟踪当前函数
            if n.type == 'function_definition':
                declarator = n.child_by_field_name('declarator')
                if declarator:
                    func_id = self.find_function_name(declarator)
                    if func_id:
                        func_name = func_id
                        current_function = func_name
            
            # 提取语句信息
            statement_types = [
                'expression_statement', 'declaration', 'return_statement',
                'if_statement', 'while_statement', 'for_statement',
                'do_statement', 'switch_statement', 'break_statement',
                'continue_statement', 'goto_statement', 'labeled_statement'
            ]
            
            if n.type in statement_types:
                start_line, end_line = self.get_line_range(n)
                
                # 为每个涉及的行创建或更新语句
                for line in range(start_line, end_line + 1):
                    if line not in statements:
                        stmt = Statement(
                            node=n,
                            start_line=start_line,
                            end_line=end_line,
                            function_name=func_name
                        )
                        
                        # 提取定义和使用
                        stmt.defs = self.extract_definitions(n)
                        stmt.uses = self.extract_uses(n)
                        stmt.called_functions = extract_function_calls(n)
                        
                        # 提取指针操作
                        stmt.pointer_defs, stmt.pointer_uses = self.extract_pointer_operations(n)
                        
                        # 提取数组和字段访问
                        stmt.array_accesses, stmt.field_accesses = self.extract_array_and_field_accesses(n)
                        
                        # 分析函数调用的参数传递
                        if n.type == 'expression_statement':
                            for child in n.children:
                                if child.type == 'call_expression':
                                    self.analyze_call_with_arguments(child, stmt)
                        
                        statements[line] = stmt
            
            # 递归处理子节点
            for child in n.children:
                visit(child, func_name)
        
        visit(root)
        return statements
    
    def find_function_name(self, declarator: Node) -> Optional[str]:
        """从函数声明器中提取函数名"""
        if declarator.type == 'identifier':
            return declarator.text.decode('utf-8')
        elif declarator.type == 'function_declarator':
            child_declarator = declarator.child_by_field_name('declarator')
            if child_declarator:
                return self.find_function_name(child_declarator)
        elif declarator.type == 'pointer_declarator':
            child_declarator = declarator.child_by_field_name('declarator')
            if child_declarator:
                return self.find_function_name(child_declarator)
        return None
    
    def build_control_dependencies(self, root: Node, statements: Dict[int, Statement]):
        """构建控制依赖关系"""
        
        def visit(n: Node, control_lines: Set[int] = None):
            if control_lines is None:
                control_lines = set()
            
            start_line, end_line = self.get_line_range(n)
            
            # 控制流语句
            if n.type in ['if_statement', 'while_statement', 'for_statement', 
                         'do_statement', 'switch_statement']:
                # 条件/控制表达式所在行
                cond_line = start_line
                new_control = control_lines | {cond_line}
                
                # 处理控制体内的所有语句
                if n.type == 'if_statement':
                    consequence = n.child_by_field_name('consequence')
                    alternative = n.child_by_field_name('alternative')
                    if consequence:
                        visit(consequence, new_control)
                    if alternative:
                        visit(alternative, new_control)
                elif n.type in ['while_statement', 'for_statement', 'do_statement']:
                    body = n.child_by_field_name('body')
                    if body:
                        visit(body, new_control)
                elif n.type == 'switch_statement':
                    body = n.child_by_field_name('body')
                    if body:
                        visit(body, new_control)
                
                # 处理其他子节点（但不传递控制依赖）
                for child in n.children:
                    if child not in [n.child_by_field_name('consequence'),
                                    n.child_by_field_name('alternative'),
                                    n.child_by_field_name('body')]:
                        if child.type not in ['(', ')', '{', '}', 'if', 'while', 
                                             'for', 'do', 'switch']:
                            visit(child, control_lines)
            else:
                # 为当前节点涉及的所有行添加控制依赖
                for line in range(start_line, end_line + 1):
                    if line in statements:
                        statements[line].control_deps.update(control_lines)
                
                # 递归处理子节点
                for child in n.children:
                    visit(child, control_lines)
        
        visit(root)
    
    def perform_slicing(self, statements: Dict[int, Statement], 
                       anchors: Set[str], target_line: int) -> Set[int]:
        """执行前向和后向切片（带作用域约束）"""
        slice_lines = {target_line}
        
        # 确定目标行所属的函数
        target_function = None
        if target_line in statements:
            target_function = statements[target_line].function_name
        
        # 后向切片
        worklist = {target_line}
        visited_backward = set()
        relevant_vars = set(anchors)
        
        while worklist:
            line = worklist.pop()
            if line in visited_backward:
                continue
            visited_backward.add(line)
            
            if line not in statements:
                continue
            
            stmt = statements[line]
            current_function = stmt.function_name
            
            # 收集需要追踪的变量（仅限在当前作用域内的变量）
            vars_to_track = set()
            for var in stmt.uses:
                if var in relevant_vars:
                    vars_to_track.add(var)
            
            # 后向查找定义这些变量的语句
            for var in vars_to_track:
                # 判断变量类型
                is_global = var in self.global_vars
                
                for other_line, other_stmt in statements.items():
                    if var in other_stmt.defs and other_line < line and other_line not in slice_lines:
                        other_function = other_stmt.function_name
                        
                        # 只包含满足以下条件的语句：
                        # 1. 同一函数内的局部变量
                        # 2. 全局变量（但两个语句都必须有函数上下文）
                        include_stmt = False
                        
                        if other_function == current_function:
                            # 同一函数内
                            include_stmt = True
                        elif is_global and current_function and other_function:
                            # 全局变量，但我们只在需要跨函数追踪时才包含
                            # 对于局部变量名冲突（如多个函数都有 int i），不包含
                            if current_function in self.function_scopes:
                                scope = self.function_scopes[current_function]
                                # 如果该变量在当前函数的局部作用域，则不跨函数追踪
                                if var not in scope['all_vars']:
                                    include_stmt = True
                        
                        if include_stmt:
                            slice_lines.add(other_line)
                            worklist.add(other_line)
                            # 添加新定义的变量到相关变量集
                            for used_var in other_stmt.uses:
                                relevant_vars.add(used_var)
            
            # 添加控制依赖（仅限同一函数）
            for dep_line in stmt.control_deps:
                if dep_line not in slice_lines and dep_line < line:
                    if dep_line in statements:
                        dep_stmt = statements[dep_line]
                        # 同一函数内的控制依赖
                        if dep_stmt.function_name == current_function:
                            slice_lines.add(dep_line)
                            worklist.add(dep_line)
                            # 控制条件中的变量
                            for used_var in dep_stmt.uses:
                                relevant_vars.add(used_var)
        
        # 前向切片
        worklist = {target_line}
        visited_forward = set()
        forward_vars = set(anchors)
        if target_line in statements:
            forward_vars.update(statements[target_line].defs)
        
        while worklist:
            line = worklist.pop()
            if line in visited_forward:
                continue
            visited_forward.add(line)
            
            if line not in statements:
                continue
            
            stmt = statements[line]
            current_function = stmt.function_name
            
            # 只考虑在作用域内的定义
            for var in stmt.defs:
                forward_vars.add(var)
            
            # 前向查找使用这些变量的语句
            for other_line, other_stmt in statements.items():
                if other_line > line and other_line not in slice_lines:
                    other_function = other_stmt.function_name
                    
                    # 检查是否有相关变量的使用
                    relevant_uses = set()
                    for var in other_stmt.uses:
                        if var in forward_vars:
                            # 判断是否应该包含
                            include_stmt = False
                            
                            if other_function == current_function:
                                # 同一函数内
                                include_stmt = True
                            elif var in self.global_vars:
                                # 全局变量
                                if other_function in self.function_scopes:
                                    scope = self.function_scopes[other_function]
                                    # 如果该变量在目标函数的局部作用域，不跨函数追踪
                                    if var not in scope['all_vars']:
                                        include_stmt = True
                            
                            if include_stmt:
                                relevant_uses.add(var)
                    
                    if relevant_uses:
                        slice_lines.add(other_line)
                        worklist.add(other_line)
            
            # 添加被此行控制的语句（仅限同一函数）
            for other_line, other_stmt in statements.items():
                if line in other_stmt.control_deps and other_line not in slice_lines:
                    if other_stmt.function_name == current_function:
                        slice_lines.add(other_line)
                        worklist.add(other_line)
        
        return slice_lines
    
    def perform_slicing_with_interprocedural(self, statements: Dict[int, Statement], 
                                            anchors: Set[str], target_line: int,
                                            max_call_depth: int = 1) -> Set[int]:
        """执行带有过程间分析的切片（增强版）"""
        slice_lines = {target_line}
        
        # 确定目标行所属的函数
        target_function = None
        if target_line in statements:
            target_function = statements[target_line].function_name
        
        # 后向切片
        worklist = {target_line}
        visited_backward = set()
        relevant_vars = set(anchors)
        analyzed_functions = set()  # 已分析的函数，避免递归
        
        while worklist:
            line = worklist.pop()
            if line in visited_backward:
                continue
            visited_backward.add(line)
            
            if line not in statements:
                continue
            
            stmt = statements[line]
            current_function = stmt.function_name
            
            # 收集需要追踪的变量
            vars_to_track = set()
            for var in stmt.uses:
                if var in relevant_vars:
                    vars_to_track.add(var)
            
            # 同时考虑指针使用
            pointer_vars_to_track = set()
            for ptr_var in stmt.pointer_uses:
                if ptr_var in relevant_vars:
                    pointer_vars_to_track.add(ptr_var)
                    # 添加可能的别名
                    if ptr_var in self.pointer_aliases:
                        vars_to_track.update(self.pointer_aliases[ptr_var])
            
            # 考虑数组访问
            for arr_var in stmt.array_accesses:
                if arr_var in relevant_vars:
                    vars_to_track.add(arr_var)
            
            # 考虑结构体字段访问
            for obj_var, fields in stmt.field_accesses.items():
                if obj_var in relevant_vars:
                    vars_to_track.add(obj_var)
            
            # 后向查找定义这些变量的语句
            for var in vars_to_track:
                is_global = var in self.global_vars
                
                for other_line, other_stmt in statements.items():
                    if other_line >= line or other_line in slice_lines:
                        continue
                    
                    # 检查直接定义
                    if var in other_stmt.defs:
                        other_function = other_stmt.function_name
                        include_stmt = False
                        
                        if other_function == current_function:
                            include_stmt = True
                        elif is_global and current_function and other_function:
                            if current_function in self.function_scopes:
                                scope = self.function_scopes[current_function]
                                if var not in scope['all_vars']:
                                    include_stmt = True
                        
                        if include_stmt:
                            slice_lines.add(other_line)
                            worklist.add(other_line)
                            for used_var in other_stmt.uses:
                                relevant_vars.add(used_var)
                            # 添加指针别名
                            for alias_var in other_stmt.may_alias.get(var, set()):
                                relevant_vars.add(alias_var)
                    
                    # 检查通过指针的定义
                    if var in other_stmt.pointer_defs:
                        # 如果通过指针修改了可能的别名
                        for ptr_var in other_stmt.pointer_defs:
                            if ptr_var in self.pointer_aliases:
                                if var in self.pointer_aliases[ptr_var]:
                                    if other_stmt.function_name == current_function:
                                        slice_lines.add(other_line)
                                        worklist.add(other_line)
                                        relevant_vars.add(ptr_var)
                    
                    # 检查通过函数调用的修改
                    if var in other_stmt.modified_by_call:
                        if other_stmt.function_name == current_function:
                            slice_lines.add(other_line)
                            worklist.add(other_line)
            
            # 跨函数分析：检查函数调用
            if max_call_depth > 0 and current_function:
                for called_func in stmt.called_functions:
                    if called_func in self.function_info and called_func not in analyzed_functions:
                        func_info = self.function_info[called_func]
                        
                        # 跳过递归函数
                        if func_info.is_recursive:
                            continue
                        
                        # 检查被调用函数是否修改了相关的全局变量
                        modified_relevant = func_info.modifies_globals & relevant_vars
                        if modified_relevant:
                            # 包含该函数内修改这些变量的语句
                            for other_line, other_stmt in statements.items():
                                if other_stmt.function_name == called_func:
                                    if other_stmt.defs & modified_relevant:
                                        if other_line not in slice_lines:
                                            slice_lines.add(other_line)
                                            worklist.add(other_line)
                            
                            analyzed_functions.add(called_func)
                        
                        # 检查返回值是否被使用
                        if func_info.return_vars & relevant_vars:
                            # 包含函数的返回语句
                            for other_line, other_stmt in statements.items():
                                if (other_stmt.function_name == called_func and 
                                    other_stmt.node.type == 'return_statement'):
                                    if other_line not in slice_lines:
                                        slice_lines.add(other_line)
                                        worklist.add(other_line)
            
            # 添加控制依赖（仅限同一函数）
            for dep_line in stmt.control_deps:
                if dep_line not in slice_lines and dep_line < line:
                    if dep_line in statements:
                        dep_stmt = statements[dep_line]
                        if dep_stmt.function_name == current_function:
                            slice_lines.add(dep_line)
                            worklist.add(dep_line)
                            for used_var in dep_stmt.uses:
                                relevant_vars.add(used_var)
        
        # 前向切片
        worklist = {target_line}
        visited_forward = set()
        forward_vars = set(anchors)
        if target_line in statements:
            forward_vars.update(statements[target_line].defs)
        
        while worklist:
            line = worklist.pop()
            if line in visited_forward:
                continue
            visited_forward.add(line)
            
            if line not in statements:
                continue
            
            stmt = statements[line]
            current_function = stmt.function_name
            
            # 添加定义的变量
            for var in stmt.defs:
                forward_vars.add(var)
            
            # 添加通过指针定义的变量及其别名
            for ptr_var in stmt.pointer_defs:
                forward_vars.add(ptr_var)
                if ptr_var in self.pointer_aliases:
                    forward_vars.update(self.pointer_aliases[ptr_var])
            
            # 添加通过函数调用修改的变量
            for var in stmt.modified_by_call:
                forward_vars.add(var)
            
            # 前向查找使用这些变量的语句
            for other_line, other_stmt in statements.items():
                if other_line <= line or other_line in slice_lines:
                    continue
                
                other_function = other_stmt.function_name
                relevant_uses = set()
                
                # 直接使用
                for var in other_stmt.uses:
                    if var in forward_vars:
                        include_stmt = False
                        
                        if other_function == current_function:
                            include_stmt = True
                        elif var in self.global_vars:
                            if other_function in self.function_scopes:
                                scope = self.function_scopes[other_function]
                                if var not in scope['all_vars']:
                                    include_stmt = True
                        
                        if include_stmt:
                            relevant_uses.add(var)
                
                # 通过指针使用
                for ptr_var in other_stmt.pointer_uses:
                    if ptr_var in forward_vars:
                        if other_function == current_function:
                            relevant_uses.add(ptr_var)
                
                # 数组访问
                for arr_var in other_stmt.array_accesses:
                    if arr_var in forward_vars:
                        if other_function == current_function:
                            relevant_uses.add(arr_var)
                
                # 字段访问
                for obj_var in other_stmt.field_accesses.keys():
                    if obj_var in forward_vars:
                        if other_function == current_function:
                            relevant_uses.add(obj_var)
                
                if relevant_uses:
                    slice_lines.add(other_line)
                    worklist.add(other_line)
            
            # 添加被此行控制的语句（仅限同一函数）
            for other_line, other_stmt in statements.items():
                if line in other_stmt.control_deps and other_line not in slice_lines:
                    if other_stmt.function_name == current_function:
                        slice_lines.add(other_line)
                        worklist.add(other_line)
        
        return slice_lines
    
    def slice(self, file_path: str, target_line: int, 
             enable_interprocedural: bool = True,
             max_call_depth: int = 1) -> Optional[SliceResult]:
        """对指定文件和行执行切片
        
        Args:
            file_path: 源文件路径
            target_line: 目标行号
            enable_interprocedural: 是否启用过程间分析
            max_call_depth: 函数调用追踪的最大深度
        """
        # 解析文件
        root = self.parse_file(file_path)
        if not root:
            return None
        
        with open(file_path, 'rb') as f:
            source_code = f.read()
        
        # 分析作用域
        self.analyze_scopes(root)
        
        # 分析结构体定义
        self.analyze_struct_definitions(root)
        
        # 分析类型信息
        self.analyze_type_information(root)
        
        # 分析函数信息
        self.analyze_functions(root)
        
        # 分析函数副作用
        self.analyze_function_side_effects(root)
        
        # 检测递归调用
        self.detect_recursive_calls()
        
        # 提取语义锚点
        anchors = self.extract_anchors(root, source_code, target_line)
        if not anchors:
            print(f"Warning: No anchors found at line {target_line} in {file_path}")
            anchors = set(['__dummy__'])
        
        # 构建语句信息
        statements = self.build_statements(root, source_code)
        
        # 分析指针别名
        self.analyze_pointer_aliases(statements)
        
        # 构建控制依赖
        self.build_control_dependencies(root, statements)
        
        # 执行切片
        if enable_interprocedural:
            slice_lines = self.perform_slicing_with_interprocedural(
                statements, anchors, target_line, max_call_depth
            )
        else:
            slice_lines = self.perform_slicing(statements, anchors, target_line)
        
        # 构建函数映射
        function_map = {}
        for line in slice_lines:
            if line in statements and statements[line].function_name:
                function_map[line] = statements[line].function_name
        
        return SliceResult(
            target_line=target_line,
            target_file=file_path,
            anchors=anchors,
            slice_lines=slice_lines,
            function_map=function_map
        )
    
    def analyze_scopes(self, root: Node):
        """分析变量作用域"""
        self.function_scopes = {}
        self.global_vars = set()
        self.function_defs = {}
        
        def extract_params(declarator: Node) -> Set[str]:
            """提取函数参数"""
            params = set()
            if declarator.type == 'function_declarator':
                param_list = declarator.child_by_field_name('parameters')
                if param_list:
                    for child in param_list.children:
                        if child.type == 'parameter_declaration':
                            declarator_node = child.child_by_field_name('declarator')
                            if declarator_node:
                                param_name = self.extract_declarator_name(declarator_node)
                                if param_name:
                                    params.add(param_name)
            elif declarator.type in ['pointer_declarator', 'array_declarator']:
                for child in declarator.children:
                    params.update(extract_params(child))
            return params
        
        def extract_local_vars(body: Node) -> Set[str]:
            """提取函数体中的局部变量"""
            local_vars = set()
            
            def visit(n: Node):
                if n.type == 'declaration':
                    for child in n.children:
                        if child.type == 'init_declarator':
                            declarator = child.child_by_field_name('declarator')
                            if declarator:
                                var_name = self.extract_declarator_name(declarator)
                                if var_name:
                                    local_vars.add(var_name)
                
                # 递归处理子节点，但不进入嵌套函数
                if n.type != 'function_definition':
                    for child in n.children:
                        visit(child)
            
            visit(body)
            return local_vars
        
        def visit_top_level(n: Node):
            """访问顶层节点"""
            if n.type == 'function_definition':
                declarator = n.child_by_field_name('declarator')
                body = n.child_by_field_name('body')
                
                if declarator:
                    func_name = self.find_function_name(declarator)
                    if func_name:
                        start_line = self.get_line_range(n)[0]
                        self.function_defs[func_name] = start_line
                        
                        # 提取参数
                        params = extract_params(declarator)
                        
                        # 提取局部变量
                        local_vars = set()
                        if body:
                            local_vars = extract_local_vars(body)
                        
                        self.function_scopes[func_name] = {
                            'params': params,
                            'locals': local_vars,
                            'all_vars': params | local_vars
                        }
            
            elif n.type == 'declaration':
                # 全局变量
                for child in n.children:
                    if child.type == 'init_declarator':
                        declarator = child.child_by_field_name('declarator')
                        if declarator:
                            var_name = self.extract_declarator_name(declarator)
                            if var_name:
                                self.global_vars.add(var_name)
            
            for child in n.children:
                visit_top_level(child)
        
        visit_top_level(root)
    
    def extract_declarator_name(self, declarator: Node) -> Optional[str]:
        """从声明器中提取变量名"""
        if declarator.type == 'identifier':
            return declarator.text.decode('utf-8')
        elif declarator.type in ['pointer_declarator', 'array_declarator', 
                                 'function_declarator', 'parenthesized_declarator']:
            for child in declarator.children:
                name = self.extract_declarator_name(child)
                if name:
                    return name
        return None
    
    def is_variable_in_scope(self, var_name: str, function_name: Optional[str]) -> bool:
        """检查变量是否在指定函数的作用域内"""
        if not function_name:
            return var_name in self.global_vars
        
        if function_name in self.function_scopes:
            scope = self.function_scopes[function_name]
            return var_name in scope['all_vars'] or var_name in self.global_vars
        
        return False
    
    def analyze_functions(self, root: Node):
        """分析所有函数的详细信息"""
        self.function_info = {}
        self.call_graph = defaultdict(set)
        
        def is_pointer_type(type_node: Node) -> bool:
            """判断是否为指针或引用类型"""
            if not type_node:
                return False
            
            type_text = type_node.text.decode('utf-8')
            return '*' in type_text or '&' in type_text or type_text.endswith('*')
        
        def extract_param_info(param_node: Node) -> Tuple[Optional[str], bool]:
            """提取参数名和是否为指针"""
            param_name = None
            is_pointer = False
            
            declarator = param_node.child_by_field_name('declarator')
            type_node = param_node.child_by_field_name('type')
            
            if type_node:
                is_pointer = is_pointer_type(type_node)
            
            if declarator:
                if declarator.type == 'pointer_declarator':
                    is_pointer = True
                    # 提取指针声明器中的名字
                    for child in declarator.children:
                        if child.type == 'identifier':
                            param_name = child.text.decode('utf-8')
                            break
                elif declarator.type == 'identifier':
                    param_name = declarator.text.decode('utf-8')
                else:
                    param_name = self.extract_declarator_name(declarator)
            
            return param_name, is_pointer
        
        def analyze_function(node: Node):
            """分析单个函数"""
            declarator = node.child_by_field_name('declarator')
            body = node.child_by_field_name('body')
            type_node = node.child_by_field_name('type')
            
            if not declarator:
                return
            
            func_name = self.find_function_name(declarator)
            if not func_name:
                return
            
            start_line, end_line = self.get_line_range(node)
            
            func_info = FunctionInfo(
                name=func_name,
                start_line=start_line,
                end_line=end_line
            )
            
            # 提取返回类型
            if type_node:
                func_info.return_type = self.extract_type_from_node(type_node)
            
            # 提取参数信息
            if declarator.type == 'function_declarator':
                params = declarator.child_by_field_name('parameters')
                if params:
                    for child in params.children:
                        if child.type == 'parameter_declaration':
                            param_name, is_pointer = extract_param_info(child)
                            if param_name:
                                func_info.params.append(param_name)
                                if is_pointer:
                                    func_info.pointer_params.add(param_name)
                                
                                # 提取参数类型
                                type_node = child.child_by_field_name('type')
                                if type_node:
                                    func_info.param_types[param_name] = self.extract_type_from_node(type_node)
            
            # 提取返回变量、修改的全局变量和函数调用
            if body:
                def visit_body(n: Node):
                    if n.type == 'return_statement':
                        # 提取返回值中的变量
                        identifiers = self.extract_identifiers(n)
                        func_info.return_vars.update(identifiers)
                    
                    elif n.type == 'assignment_expression':
                        # 检查是否修改全局变量
                        left = n.child_by_field_name('left')
                        if left and left.type == 'identifier':
                            var_name = left.text.decode('utf-8')
                            if var_name in self.global_vars:
                                func_info.modifies_globals.add(var_name)
                    
                    elif n.type == 'call_expression':
                        # 构建调用图
                        func = n.child_by_field_name('function')
                        if func and func.type == 'identifier':
                            callee = func.text.decode('utf-8')
                            self.call_graph[func_name].add(callee)
                            func_info.calls.add(callee)
                    
                    for child in n.children:
                        visit_body(child)
                
                visit_body(body)
            
            self.function_info[func_name] = func_info
        
        def visit(n: Node):
            if n.type == 'function_definition':
                analyze_function(n)
            
            for child in n.children:
                visit(child)
        
        visit(root)
    
    def analyze_pointer_aliases(self, statements: Dict[int, Statement]):
        """分析指针别名关系（使用增强版本）"""
        self.analyze_enhanced_pointer_aliases(statements)
    
    def extract_pointer_operations(self, node: Node) -> Tuple[Set[str], Set[str]]:
        """提取指针解引用的定义和使用"""
        pointer_defs = set()
        pointer_uses = set()
        
        def visit(n: Node, in_assignment_lhs: bool = False):
            if n.type == 'pointer_expression':
                # 指针解引用: *p
                arg = n.child_by_field_name('argument')
                if arg and arg.type == 'identifier':
                    ptr_var = arg.text.decode('utf-8')
                    if in_assignment_lhs:
                        pointer_defs.add(ptr_var)
                    else:
                        pointer_uses.add(ptr_var)
            
            elif n.type == 'assignment_expression':
                left = n.child_by_field_name('left')
                right = n.child_by_field_name('right')
                
                if left:
                    visit(left, True)
                if right:
                    visit(right, False)
            
            else:
                for child in n.children:
                    visit(child, in_assignment_lhs)
        
        visit(node)
        return pointer_defs, pointer_uses
    
    def extract_type_from_node(self, type_node: Node) -> str:
        """从类型节点提取类型字符串"""
        if not type_node:
            return ""
        return type_node.text.decode('utf-8').strip()
    
    def get_pointer_level(self, type_str: str) -> int:
        """获取指针层级"""
        return type_str.count('*')
    
    def is_pointer_or_array_type(self, type_str: str) -> bool:
        """判断是否为指针或数组类型"""
        return '*' in type_str or '[' in type_str
    
    def extract_array_and_field_accesses(self, node: Node) -> Tuple[Set[str], Dict[str, Set[str]]]:
        """提取数组访问和结构体字段访问"""
        array_accesses = set()
        field_accesses = defaultdict(set)
        
        def visit(n: Node):
            if n.type == 'subscript_expression':
                # 数组访问: arr[i]
                arr = n.child_by_field_name('argument')
                if arr and arr.type == 'identifier':
                    array_accesses.add(arr.text.decode('utf-8'))
            
            elif n.type == 'field_expression':
                # 结构体字段访问: obj.field 或 ptr->field
                obj = n.child_by_field_name('argument')
                field = n.child_by_field_name('field')
                
                if field and field.type == 'field_identifier':
                    field_name = field.text.decode('utf-8')
                    
                    # 递归提取最外层对象
                    base_obj = self.extract_base_object(obj)
                    if base_obj:
                        field_accesses[base_obj].add(field_name)
            
            for child in n.children:
                visit(child)
        
        visit(node)
        return array_accesses, dict(field_accesses)
    
    def extract_base_object(self, node: Node) -> Optional[str]:
        """从字段表达式中提取基对象名"""
        if not node:
            return None
        
        if node.type == 'identifier':
            return node.text.decode('utf-8')
        elif node.type == 'field_expression':
            return self.extract_base_object(node.child_by_field_name('argument'))
        elif node.type == 'pointer_expression':
            arg = node.child_by_field_name('argument')
            if arg and arg.type == 'identifier':
                return arg.text.decode('utf-8')
        elif node.type == 'subscript_expression':
            arr = node.child_by_field_name('argument')
            if arr and arr.type == 'identifier':
                return arr.text.decode('utf-8')
        
        return None
    
    def analyze_struct_definitions(self, root: Node):
        """分析结构体定义"""
        self.struct_fields = defaultdict(set)
        
        def visit(n: Node):
            if n.type in ['struct_specifier', 'union_specifier']:
                # 提取结构体名
                struct_name = None
                for child in n.children:
                    if child.type == 'type_identifier':
                        struct_name = child.text.decode('utf-8')
                        break
                
                # 提取字段列表
                field_decl_list = n.child_by_field_name('body')
                if field_decl_list and struct_name:
                    for field_node in field_decl_list.children:
                        if field_node.type == 'field_declaration':
                            # 提取字段名
                            for child in field_node.children:
                                if child.type == 'field_declarator':
                                    field_name = self.extract_declarator_name(child)
                                    if field_name:
                                        self.struct_fields[struct_name].add(field_name)
            
            for child in n.children:
                visit(child)
        
        visit(root)
    
    def analyze_type_information(self, root: Node):
        """分析变量类型信息"""
        self.type_info = {}
        
        def analyze_declaration(decl_node: Node):
            """分析声明语句"""
            type_node = decl_node.child_by_field_name('type')
            if not type_node:
                return
            
            type_str = self.extract_type_from_node(type_node)
            
            # 遍历声明器
            for child in decl_node.children:
                if child.type == 'init_declarator':
                    declarator = child.child_by_field_name('declarator')
                    if declarator:
                        var_name, full_type = self.extract_declarator_with_type(declarator, type_str)
                        if var_name:
                            self.type_info[var_name] = full_type
                elif child.type in ['pointer_declarator', 'array_declarator', 'identifier']:
                    var_name, full_type = self.extract_declarator_with_type(child, type_str)
                    if var_name:
                        self.type_info[var_name] = full_type
        
        def visit(n: Node):
            if n.type == 'declaration':
                analyze_declaration(n)
            elif n.type == 'parameter_declaration':
                analyze_declaration(n)
            
            for child in n.children:
                visit(child)
        
        visit(root)
    
    def extract_declarator_with_type(self, declarator: Node, base_type: str) -> Tuple[Optional[str], str]:
        """从声明器中提取变量名和完整类型"""
        if declarator.type == 'identifier':
            return declarator.text.decode('utf-8'), base_type
        
        elif declarator.type == 'pointer_declarator':
            # 指针类型
            child_declarator = declarator.child_by_field_name('declarator')
            if child_declarator:
                var_name, _ = self.extract_declarator_with_type(child_declarator, base_type)
                return var_name, base_type + '*'
            return None, base_type + '*'
        
        elif declarator.type == 'array_declarator':
            # 数组类型
            child_declarator = declarator.child_by_field_name('declarator')
            if child_declarator:
                var_name, _ = self.extract_declarator_with_type(child_declarator, base_type)
                return var_name, base_type + '[]'
            return None, base_type + '[]'
        
        elif declarator.type == 'function_declarator':
            # 函数指针
            child_declarator = declarator.child_by_field_name('declarator')
            if child_declarator:
                return self.extract_declarator_with_type(child_declarator, base_type)
        
        return None, base_type
    
    def analyze_enhanced_pointer_aliases(self, statements: Dict[int, Statement]):
        """增强的指针别名分析"""
        self.pointer_aliases = defaultdict(set)
        
        # 第一遍：建立直接别名关系
        for line, stmt in statements.items():
            node = stmt.node
            self._analyze_pointer_assignment(node, stmt)
        
        # 第二遍：传播别名关系（处理传递性）
        changed = True
        max_iterations = 10
        iteration = 0
        
        while changed and iteration < max_iterations:
            changed = False
            iteration += 1
            
            # 创建别名关系的副本
            old_aliases = {k: v.copy() for k, v in self.pointer_aliases.items()}
            
            # 传播别名关系
            for ptr, aliases in old_aliases.items():
                for alias in aliases:
                    if alias in old_aliases:
                        # 传递性：如果 p->a 且 a->b，则 p->b
                        new_aliases = old_aliases[alias] - self.pointer_aliases[ptr]
                        if new_aliases:
                            self.pointer_aliases[ptr].update(new_aliases)
                            changed = True
    
    def _analyze_pointer_assignment(self, node: Node, stmt: Statement):
        """分析指针赋值（递归）"""
        if node.type == 'assignment_expression':
            left = node.child_by_field_name('left')
            right = node.child_by_field_name('right')
            
            if left and right:
                left_var = self._extract_lvalue(left)
                
                # 取地址操作: p = &var
                if right.type == 'unary_expression':
                    op = right.child(0)
                    if op and op.text.decode('utf-8') == '&':
                        arg = right.child_by_field_name('argument')
                        if arg:
                            right_var = self._extract_lvalue(arg)
                            if left_var and right_var:
                                self.pointer_aliases[left_var].add(right_var)
                                stmt.may_alias[left_var] = {right_var}
                
                # 指针赋值: p = q
                elif right.type == 'identifier':
                    right_var = right.text.decode('utf-8')
                    if left_var and right_var in self.pointer_aliases:
                        self.pointer_aliases[left_var].update(self.pointer_aliases[right_var])
                        stmt.may_alias[left_var] = self.pointer_aliases[right_var].copy()
                
                # 指针解引用赋值: p = *q
                elif right.type == 'pointer_expression':
                    arg = right.child_by_field_name('argument')
                    if arg and arg.type == 'identifier':
                        right_ptr = arg.text.decode('utf-8')
                        if left_var and right_ptr in self.pointer_aliases:
                            # p 指向 q 指向的对象
                            self.pointer_aliases[left_var].update(self.pointer_aliases[right_ptr])
        
        elif node.type == 'init_declarator':
            # 初始化声明: int *p = &var
            declarator = node.child_by_field_name('declarator')
            value = node.child_by_field_name('value')
            
            if declarator and value:
                left_var = self.extract_declarator_name(declarator)
                
                if value.type == 'unary_expression':
                    op = value.child(0)
                    if op and op.text.decode('utf-8') == '&':
                        arg = value.child_by_field_name('argument')
                        if arg:
                            right_var = self._extract_lvalue(arg)
                            if left_var and right_var:
                                self.pointer_aliases[left_var].add(right_var)
                                stmt.may_alias[left_var] = {right_var}
        
        # 递归处理子节点
        for child in node.children:
            self._analyze_pointer_assignment(child, stmt)
    
    def _extract_lvalue(self, node: Node) -> Optional[str]:
        """提取左值表达式的基础变量名"""
        if node.type == 'identifier':
            return node.text.decode('utf-8')
        elif node.type == 'subscript_expression':
            arr = node.child_by_field_name('argument')
            if arr and arr.type == 'identifier':
                return arr.text.decode('utf-8')
        elif node.type == 'field_expression':
            return self.extract_base_object(node)
        elif node.type == 'pointer_expression':
            arg = node.child_by_field_name('argument')
            if arg and arg.type == 'identifier':
                return arg.text.decode('utf-8')
        return None
    
    def analyze_function_side_effects(self, root: Node):
        """分析函数副作用（修改指针参数）"""
        for func_name, func_info in self.function_info.items():
            # 查找函数定义节点
            func_node = self._find_function_node(root, func_name)
            if not func_node:
                continue
            
            body = func_node.child_by_field_name('body')
            if not body:
                continue
            
            # 分析函数体中对指针参数的修改
            modified_params = set()
            
            def visit(n: Node):
                if n.type == 'assignment_expression':
                    left = n.child_by_field_name('left')
                    if left:
                        # 检查是否通过指针参数修改
                        if left.type == 'pointer_expression':
                            arg = left.child_by_field_name('argument')
                            if arg and arg.type == 'identifier':
                                param_name = arg.text.decode('utf-8')
                                if param_name in func_info.pointer_params:
                                    modified_params.add(param_name)
                        
                        # 检查是否修改指针参数指向的对象
                        base_obj = self.extract_base_object(left)
                        if base_obj and base_obj in func_info.pointer_params:
                            modified_params.add(base_obj)
                
                for child in n.children:
                    visit(child)
            
            visit(body)
            func_info.may_modify_params = modified_params
    
    def _find_function_node(self, root: Node, func_name: str) -> Optional[Node]:
        """查找函数定义节点"""
        def visit(n: Node) -> Optional[Node]:
            if n.type == 'function_definition':
                declarator = n.child_by_field_name('declarator')
                if declarator:
                    name = self.find_function_name(declarator)
                    if name == func_name:
                        return n
            
            for child in n.children:
                result = visit(child)
                if result:
                    return result
            return None
        
        return visit(root)
    
    def detect_recursive_calls(self):
        """检测递归调用"""
        for func_name in self.function_info.keys():
            if self._is_recursive(func_name, set()):
                self.function_info[func_name].is_recursive = True
    
    def _is_recursive(self, func_name: str, visited: Set[str]) -> bool:
        """检查函数是否递归（直接或间接）"""
        if func_name in visited:
            return True
        
        visited.add(func_name)
        
        if func_name in self.call_graph:
            for callee in self.call_graph[func_name]:
                if self._is_recursive(callee, visited.copy()):
                    return True
        
        return False
    
    def analyze_call_with_arguments(self, call_node: Node, stmt: Statement):
        """分析函数调用及其参数"""
        func = call_node.child_by_field_name('function')
        if not func or func.type != 'identifier':
            return
        
        func_name = func.text.decode('utf-8')
        if func_name not in self.function_info:
            return
        
        func_info = self.function_info[func_name]
        args_node = call_node.child_by_field_name('arguments')
        
        if not args_node:
            return
        
        # 提取实参列表
        actual_args = []
        for child in args_node.children:
            if child.type not in ['(', ')', ',']:
                actual_args.append(child)
        
        # 匹配形参和实参
        for i, param_name in enumerate(func_info.params):
            if i >= len(actual_args):
                break
            
            arg = actual_args[i]
            
            # 如果参数是指针类型，且函数会修改它
            if param_name in func_info.may_modify_params:
                # 提取实参变量名
                arg_var = self._extract_lvalue(arg)
                if arg_var:
                    stmt.modified_by_call.add(arg_var)


def main():
    """主函数"""
    import sys
    import argparse
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='C/C++ 语义切片工具')
    parser.add_argument('--no-interprocedural', action='store_true',
                       help='禁用过程间分析')
    parser.add_argument('--max-call-depth', type=int, default=1,
                       help='函数调用追踪的最大深度 (默认: 1)')
    parser.add_argument('--data-file', type=str, default='input/data.json',
                       help='输入数据文件路径')
    parser.add_argument('--output-dir', type=str, default='output',
                       help='输出目录')
    
    args = parser.parse_args()
    
    # 读取数据集
    data_file = args.data_file
    with open(data_file, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    
    # 创建输出目录
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    enable_interprocedural = not args.no_interprocedural
    
    print(f"配置:")
    print(f"  过程间分析: {'启用' if enable_interprocedural else '禁用'}")
    print(f"  最大调用深度: {args.max_call_depth}")
    print(f"  输入文件: {data_file}")
    print(f"  输出目录: {output_dir}")
    print()
    
    for idx, entry in enumerate(dataset):
        project_name = entry['项目名(带版本)']
        file_path = entry['缺陷所属文件']
        target_line = entry['缺陷行']
        
        # 构建完整路径
        full_path = os.path.join('input/repository', project_name, file_path)
        
        if not os.path.exists(full_path):
            print(f"[{idx+1}/{len(dataset)}] File not found: {full_path}")
            results.append({
                'project': project_name,
                'file': file_path,
                'line': target_line,
                'error': 'file_not_found'
            })
            continue
        
        # 判断是否为 C++ 文件
        is_cpp = file_path.endswith(('.cpp', '.cc', '.cxx', '.hpp', '.hxx'))
        
        print(f"[{idx+1}/{len(dataset)}] Processing {project_name}/{file_path}:{target_line}")
        
        # 执行切片
        slicer = CSemanticSlicer(is_cpp=is_cpp)
        result = slicer.slice(full_path, target_line, 
                             enable_interprocedural=enable_interprocedural,
                             max_call_depth=args.max_call_depth)
        
        if result:
            result_data = result.to_dict()
            result_data['project'] = project_name
            result_data['file'] = file_path
            result_data['config'] = {
                'interprocedural': enable_interprocedural,
                'max_call_depth': args.max_call_depth
            }
            results.append(result_data)
            print(f"  -> Anchors: {result.anchors}")
            print(f"  -> Slice size: {len(result.slice_lines)} lines")
            
            # 显示函数分布
            func_count = defaultdict(int)
            for line in result.slice_lines:
                if line in result.function_map:
                    func_count[result.function_map[line]] += 1
            if len(func_count) > 1:
                print(f"  -> Functions: {dict(func_count)}")
        else:
            results.append({
                'project': project_name,
                'file': file_path,
                'line': target_line,
                'error': 'parse_failed'
            })
            print(f"  -> Failed to parse")
    
    # 保存结果
    suffix = '_interprocedural' if enable_interprocedural else '_intraprocedural'
    output_file = os.path.join(output_dir, f'slice_results{suffix}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n完成！结果已保存到 {output_file}")
    print(f"总计处理: {len(dataset)} 个样本")
    print(f"成功: {sum(1 for r in results if 'error' not in r)} 个")
    print(f"失败: {sum(1 for r in results if 'error' in r)} 个")


if __name__ == '__main__':
    main()
