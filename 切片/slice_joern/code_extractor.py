"""
代码提取模块
从切片节点集合提取源代码，支持占位符模式
"""
from typing import Dict, Set, Optional, List
import logging
import config


def extract_code(slice_lines: Set[int], 
                source_lines: Dict[int, str], 
                placeholder: Optional[str] = None) -> str:
    """
    从切片行号集合生成源代码
    
    Args:
        slice_lines: 切片包含的行号集合
        source_lines: 原始源代码行字典 {行号: 代码行}
        placeholder: 占位符字符串（可选）
    
    Returns:
        切片代码字符串
    """
    if not slice_lines:
        return ""
    
    # 按行号排序
    sorted_lines = sorted(slice_lines)
    
    # 无占位符模式：直接拼接
    if not placeholder:
        code_parts = []
        for line in sorted_lines:
            if line in source_lines:
                code_parts.append(source_lines[line].rstrip('\n'))
        return "\n".join(code_parts) + "\n" if code_parts else ""
    
    # 占位符模式：间隔处插入占位符
    code = ""
    last_line = 0
    placeholder_count = 0
    
    for line in sorted_lines:
        if line not in source_lines:
            continue
        
        # 检查是否需要插入占位符
        if line - last_line > 1:
            # 检查间隔是否值得插入占位符
            if _should_insert_placeholder(source_lines, last_line + 1, line - 1):
                code += placeholder + "\n"
                placeholder_count += 1
        
        code += source_lines[line].rstrip('\n') + "\n"
        last_line = line
    
    logging.debug(f"Extracted code with {placeholder_count} placeholders")
    return code


def _should_insert_placeholder(source_lines: Dict[int, str], 
                              start_line: int, 
                              end_line: int) -> bool:
    """
    判断是否应该在代码间隙插入占位符
    
    Args:
        source_lines: 源代码行字典
        start_line: 间隙起始行
        end_line: 间隙结束行
    
    Returns:
        True 如果应该插入占位符
    """
    # 如果间隙只有一行
    if end_line - start_line == 0:
        line = start_line
        if line not in source_lines:
            return False
        
        line_content = source_lines[line].strip()
        
        # 空行或只有注释 - 不插入占位符
        if not line_content or line_content.startswith('//'):
            return False
    
    # 检查间隙中是否全是空行或注释
    has_code = False
    for line in range(start_line, end_line + 1):
        if line not in source_lines:
            continue
        
        content = source_lines[line].strip()
        if content and not content.startswith('//') and not content.startswith('/*'):
            has_code = True
            break
    
    return has_code


def reduced_hunks(slice_lines: Set[int], 
                 source_lines: Dict[int, str],
                 all_lines: Set[int]) -> List[str]:
    """
    生成被省略的代码块列表
    用于占位符恢复
    
    Args:
        slice_lines: 切片包含的行号
        source_lines: 源代码行字典
        all_lines: 方法的所有行号
    
    Returns:
        被省略的代码块列表
    """
    placeholder_lines = all_lines - slice_lines
    hunks = []
    
    # 将连续的行分组
    groups = _group_consecutive_lines(sorted(placeholder_lines))
    
    for group in groups:
        hunk = ""
        for line in group:
            if line in source_lines:
                hunk += source_lines[line].rstrip('\n') + "\n"
        if hunk:
            hunks.append(hunk)
    
    return hunks


def _group_consecutive_lines(lines: List[int]) -> List[List[int]]:
    """
    将连续的行号分组
    
    Args:
        lines: 已排序的行号列表
    
    Returns:
        分组后的列表，每组是连续的行号
    """
    if not lines:
        return []
    
    groups = []
    current_group = [lines[0]]
    
    for i in range(1, len(lines)):
        if lines[i] == lines[i-1] + 1:
            # 连续
            current_group.append(lines[i])
        else:
            # 不连续，开始新组
            groups.append(current_group)
            current_group = [lines[i]]
    
    # 添加最后一组
    groups.append(current_group)
    
    return groups


def extract_code_with_mapping(slice_lines: Set[int],
                              source_lines: Dict[int, str],
                              placeholder: Optional[str] = None) -> tuple[str, Dict[str, str]]:
    """
    提取代码并返回占位符映射
    
    Args:
        slice_lines: 切片行号集合
        source_lines: 源代码行字典
        placeholder: 占位符前缀
    
    Returns:
        (切片代码, 占位符映射字典)
    """
    if not placeholder:
        code = extract_code(slice_lines, source_lines, None)
        return code, {}
    
    placeholder_map = {}
    code = ""
    last_line = 0
    placeholder_counter = 0
    sorted_lines = sorted(slice_lines)
    
    for line in sorted_lines:
        if line not in source_lines:
            continue
        
        # 检查间隙
        if line - last_line > 1:
            if _should_insert_placeholder(source_lines, last_line + 1, line - 1):
                ph_key = f"/* Placeholder_{placeholder_counter} */"
                code += ph_key + "\n"
                
                # 记录被省略的代码
                omitted = ""
                for omit_line in range(last_line + 1, line):
                    if omit_line in source_lines:
                        omitted += source_lines[omit_line]
                
                placeholder_map[ph_key] = omitted
                placeholder_counter += 1
        
        code += source_lines[line].rstrip('\n') + "\n"
        last_line = line
    
    return code, placeholder_map
