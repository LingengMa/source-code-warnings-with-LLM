#!/usr/bin/env python3
"""
切片重构器 - 将残缺的切片恢复为语法正确的 C/C++ 代码
"""

import re
from typing import Set, Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class VariableDeclaration:
    """变量声明信息"""
    name: str
    type_str: str
    line: int
    in_slice: bool = False


@dataclass
class FunctionSkeleton:
    """函数骨架信息"""
    name: str
    return_type: str
    params: List[str]
    start_line: int
    end_line: int
    body_start: int
    body_end: int


class SliceReconstructor:
    """切片重构器：将切片结果恢复为可编译的代码"""
    
    def __init__(self, source_code: str, slice_lines: Set[int], 
                 function_map: Dict[int, str]):
        """
        Args:
            source_code: 原始源代码
            slice_lines: 切片包含的行号集合
            function_map: 行号到函数名的映射
        """
        self.source_lines = source_code.split('\n')
        self.slice_lines = slice_lines
        self.function_map = function_map
        
        # 分析结果
        self.functions = {}  # {func_name: FunctionSkeleton}
        self.variables = []  # List[VariableDeclaration]
        self.global_vars = []  # 全局变量
        
    def reconstruct(self) -> str:
        """重构切片为语法正确的代码"""
        # 1. 分析函数结构
        self._analyze_functions()
        
        # 2. 生成重构代码（不再需要全局变量分析）
        reconstructed = self._generate_code()
        
        return reconstructed
    
    def _analyze_functions(self):
        """分析所有涉及的函数"""
        # 找出所有涉及的函数
        involved_functions = set(self.function_map.values())
        
        for func_name in involved_functions:
            skeleton = self._extract_function_skeleton(func_name)
            if skeleton:
                self.functions[func_name] = skeleton
    
    def _extract_function_skeleton(self, func_name: str) -> Optional[FunctionSkeleton]:
        """提取函数的骨架信息"""
        # 找到函数的起始和结束行
        func_lines = [line for line, fn in self.function_map.items() if fn == func_name]
        if not func_lines:
            return None
        
        start_line = min(func_lines)
        end_line = max(func_lines)
        
        # 向前查找函数签名
        signature_line = start_line
        for i in range(start_line - 1, max(0, start_line - 10), -1):
            line_text = self.source_lines[i].strip()
            if '{' in line_text or self._looks_like_function_start(line_text):
                signature_line = i + 1
                break
        
        # 提取函数签名
        signature = self._extract_function_signature(signature_line, start_line)
        
        # 解析签名
        return_type, params = self._parse_signature(signature, func_name)
        
        # 找函数体的大括号
        body_start = self._find_opening_brace(signature_line, start_line)
        body_end = self._find_closing_brace(body_start, end_line)
        
        return FunctionSkeleton(
            name=func_name,
            return_type=return_type or "void",
            params=params,
            start_line=signature_line,
            end_line=body_end,
            body_start=body_start,
            body_end=body_end
        )
    
    def _looks_like_function_start(self, line: str) -> bool:
        """判断是否像函数开始"""
        # 简单启发式：包含括号且不是纯空白
        return '(' in line and ')' in line and not line.startswith('//')
    
    def _extract_function_signature(self, start: int, end: int) -> str:
        """提取函数签名（可能跨多行）"""
        signature_parts = []
        for i in range(start, min(end + 5, len(self.source_lines))):
            line = self.source_lines[i]
            signature_parts.append(line)
            if '{' in line:
                break
        return ' '.join(signature_parts)
    
    def _parse_signature(self, signature: str, func_name: str) -> Tuple[str, List[str]]:
        """解析函数签名，提取返回类型和参数"""
        # 简化处理：找到函数名之前的部分作为返回类型
        # 找到括号内的部分作为参数
        
        # 移除大括号
        signature = signature.split('{')[0].strip()
        
        # 找返回类型
        pattern = rf'(.*?)\s+{re.escape(func_name)}\s*\('
        match = re.search(pattern, signature)
        return_type = match.group(1).strip() if match else "void"
        
        # 找参数
        param_pattern = rf'{re.escape(func_name)}\s*\((.*?)\)'
        param_match = re.search(param_pattern, signature)
        params_str = param_match.group(1).strip() if param_match else ""
        
        # 解析参数列表
        if params_str and params_str != "void":
            params = [p.strip() for p in params_str.split(',')]
        else:
            params = []
        
        return return_type, params
    
    def _find_opening_brace(self, start: int, limit: int) -> int:
        """找到函数体的开始大括号"""
        for i in range(start, min(limit + 10, len(self.source_lines))):
            if '{' in self.source_lines[i]:
                return i + 1
        return start + 1
    
    def _find_closing_brace(self, start: int, hint: int) -> int:
        """找到函数体的结束大括号"""
        # 从hint开始向后查找
        brace_count = 1
        for i in range(start, min(hint + 20, len(self.source_lines))):
            line = self.source_lines[i]
            brace_count += line.count('{')
            brace_count -= line.count('}')
            if brace_count == 0:
                return i + 1
        return hint + 1
    
    # 移除旧的全局变量分析方法（已由新方法替代）
    
    def _extract_declarations(self, line: str, line_num: int) -> List[VariableDeclaration]:
        """从代码行中提取变量声明（严格模式）"""
        declarations = []
        
        # 跳过函数调用、控制语句等
        if any(keyword in line for keyword in ['if', 'while', 'for', 'switch', 'return', '(']):
            # 可能不是声明
            pass
        
        # 匹配常见的声明模式（必须有类型关键字）
        # 示例: int x = 5; char *p; struct Point pt;
        type_pattern = r'\b(int|char|float|double|long|short|unsigned|signed|void|struct\s+\w+|enum\s+\w+)\s+'
        var_pattern = r'(\**)(\w+)(\s*\[.*?\])?'
        
        # 完整模式
        full_pattern = type_pattern + var_pattern
        
        matches = re.finditer(full_pattern, line)
        for match in matches:
            type_str = match.group(1).strip()
            pointers = match.group(2) if match.group(2) else ''
            var_name = match.group(3).strip()
            array_part = match.group(4) if match.group(4) else ''
            
            # 构建完整类型
            full_type = f"{type_str} {pointers}".strip()
            if array_part:
                full_type += array_part
            
            # 验证是否真的是声明（后面应该是 =, ;, 或 ,）
            after_match = line[match.end():].strip()
            if after_match and after_match[0] in '=;,':
                declarations.append(VariableDeclaration(
                    name=var_name,
                    type_str=full_type,
                    line=line_num
                ))
        
        return declarations
    
    def _is_function_call_context(self, line: str, pos: int) -> bool:
        """判断是否在函数调用上下文中"""
        # 简单检查：后面是否紧跟括号
        after = line[pos:].strip()
        return after.startswith('(')
    
    # 旧方法已被 _find_used_variables_in_slice 和 _find_variable_declaration_in_function 替代
    
    def _generate_code(self) -> str:
        """生成重构后的代码 - 基于原始源码裁剪"""
        lines = []
        
        # 添加注释说明
        lines.append("/* Reconstructed slice - Syntax-correct but semantically incomplete */")
        lines.append("")
        
        # 添加必要的头文件（基本的）
        lines.append("#include <stdio.h>")
        lines.append("#include <stdlib.h>")
        lines.append("#include <string.h>")
        lines.append("")
        
        # 从原始源码中提取切片范围内的全局声明（保守策略）
        global_decls = self._extract_global_declarations_from_slice()
        if global_decls:
            lines.extend(global_decls)
            lines.append("")
        
        # 生成每个函数
        for func_name in sorted(self.functions.keys()):
            func_code = self._generate_function(func_name)
            lines.extend(func_code)
            lines.append("")
        
        return '\n'.join(lines)
    
    def _extract_struct_definitions(self) -> List[str]:
        """提取结构体定义（仅提取切片中实际包含的）"""
        structs = []
        seen_structs = set()
        
        # 扫描切片行中的 struct 定义
        in_struct = False
        struct_lines = []
        struct_name = None
        
        for line_num in sorted(self.slice_lines):
            if line_num <= 0 or line_num > len(self.source_lines):
                continue
            
            line = self.source_lines[line_num - 1]
            
            # 检测 struct 定义的开始
            struct_match = re.search(r'\bstruct\s+(\w+)\s*{', line)
            if struct_match and not in_struct:
                struct_name = struct_match.group(1)
                if struct_name not in seen_structs:
                    in_struct = True
                    struct_lines = [line.strip()]
            elif in_struct:
                struct_lines.append(line.strip())
                if '};' in line:
                    structs.append(' '.join(struct_lines))
                    seen_structs.add(struct_name)
                    in_struct = False
                    struct_lines = []
                    struct_name = None
        
        return structs
    
    def _extract_global_declarations_from_slice(self) -> List[str]:
        """从切片中提取全局声明（极度保守策略）"""
        global_decls = []
        seen_decls = set()
        
        # 找到第一个函数的起始行
        first_func_line = float('inf')
        for func in self.functions.values():
            first_func_line = min(first_func_line, func.start_line)
        
        if first_func_line == float('inf'):
            first_func_line = len(self.source_lines)
        
        # 只处理切片中在第一个函数之前的行
        for line_num in sorted(self.slice_lines):
            if line_num >= first_func_line:
                break
            
            if line_num <= 0 or line_num > len(self.source_lines):
                continue
            
            line = self.source_lines[line_num - 1].strip()
            
            # 跳过空行、注释、预处理指令
            if not line or line.startswith('//') or line.startswith('/*') or line.startswith('#'):
                continue
            
            # 跳过 struct/enum/typedef 定义（由专门函数处理）
            if line.startswith('struct') or line.startswith('enum') or line.startswith('typedef'):
                continue
            
            # 检查是否是全局变量声明
            if self._is_global_declaration(line):
                # 移除初始化表达式，只保留声明
                clean_decl = self._clean_global_declaration(line)
                
                # 提取变量名用于去重
                var_name = self._extract_var_name_from_decl(clean_decl)
                if var_name and var_name not in seen_decls:
                    global_decls.append(clean_decl)
                    seen_decls.add(var_name)
        
        return global_decls
    
    def _is_global_declaration(self, line: str) -> bool:
        """判断是否是全局变量声明"""
        # 必须包含分号
        if ';' not in line:
            return False
        
        # 检查是否符合声明模式
        decl_pattern = r'^(static\s+)?(const\s+)?(extern\s+)?' \
                      r'(int|char|float|double|long|short|unsigned|signed|void|struct\s+\w+|enum\s+\w+)' \
                      r'\s+[\*\s]*\w+'
        
        return bool(re.match(decl_pattern, line))
    
    def _clean_global_declaration(self, line: str) -> str:
        """清理全局声明，移除初始化表达式"""
        # 移除初始化部分（= 之后的内容）
        if '=' in line:
            # 找到第一个 = 的位置
            eq_pos = line.index('=')
            # 找到对应的分号
            semicolon_pos = line.rindex(';')
            # 只保留声明部分
            line = line[:eq_pos].strip() + ';'
            # 添加注释说明
            line += '  /* initializer removed */'
        
        return line
    
    def _extract_var_name_from_decl(self, decl: str) -> Optional[str]:
        """从声明中提取变量名"""
        # 移除注释
        decl = re.sub(r'/\*.*?\*/', '', decl)
        decl = re.sub(r'//.*', '', decl)
        
        # 移除分号
        decl = decl.replace(';', '').strip()
        
        # 提取最后一个标识符作为变量名
        tokens = re.findall(r'\w+', decl)
        if tokens:
            # 排除类型关键字
            type_keywords = {'int', 'char', 'float', 'double', 'long', 'short', 
                           'unsigned', 'signed', 'void', 'const', 'static', 'extern',
                           'struct', 'enum', 'union'}
            for token in reversed(tokens):
                if token not in type_keywords:
                    return token
        
        return None
    
    def _generate_function(self, func_name: str) -> List[str]:
        """生成单个函数的代码"""
        func = self.functions[func_name]
        lines = []
        
        # 函数签名
        params_str = ', '.join(func.params) if func.params else 'void'
        signature = f"{func.return_type} {func_name}({params_str})"
        lines.append(signature)
        lines.append("{")
        
        # 收集这个函数的切片行
        func_slice_lines = sorted([
            line for line in self.slice_lines 
            if line in self.function_map and self.function_map[line] == func_name
        ])
        
        if not func_slice_lines:
            lines.append("    /* Empty slice */")
            lines.append("}")
            return lines
        
        # 添加变量声明（不在切片中但需要的）
        missing_decls = self._get_missing_declarations(func_name, func_slice_lines)
        if missing_decls:
            lines.append("    /* Auto-recovered variable declarations */")
            for decl in missing_decls:
                lines.append(f"    {decl.type_str} {decl.name};")
            lines.append("")
        
        # 生成函数体
        body_lines = self._generate_function_body(func_name, func_slice_lines)
        lines.extend(body_lines)
        
        lines.append("}")
        return lines
    
    def _get_missing_declarations(self, func_name: str, 
                                  slice_lines: List[int]) -> List[VariableDeclaration]:
        """获取需要补充的变量声明（极度保守策略）"""
        # 收集切片中已声明的变量
        declared_in_slice = set()
        for line_num in slice_lines:
            if line_num <= 0 or line_num >= len(self.source_lines):
                continue
            line = self.source_lines[line_num - 1]
            # 提取该行声明的变量
            decls = self._extract_declarations(line, line_num)
            for decl in decls:
                declared_in_slice.add(decl.name)
        
        # 收集函数体内所有声明的变量（包括切片外的）
        func = self.functions[func_name]
        all_declarations_in_func = {}  # {var_name: VariableDeclaration}
        
        for i in range(func.body_start, min(func.body_end, len(self.source_lines))):
            line = self.source_lines[i]
            decls = self._extract_declarations(line, i + 1)
            for decl in decls:
                if decl.name not in all_declarations_in_func:
                    all_declarations_in_func[decl.name] = decl
        
        # 收集使用但未在切片中声明的变量
        used_vars = self._find_used_variables_in_slice(slice_lines)
        missing_var_names = used_vars - declared_in_slice
        
        # 只补充在函数体内实际声明过的变量
        missing_decls = []
        for var_name in missing_var_names:
            if var_name in all_declarations_in_func:
                missing_decls.append(all_declarations_in_func[var_name])
        
        return missing_decls
    
    def _find_used_variables_in_slice(self, slice_lines: List[int]) -> Set[str]:
        """查找切片中使用的变量（仅在函数内，严格过滤）"""
        used = set()
        
        for line_num in slice_lines:
            if line_num <= 0 or line_num > len(self.source_lines):
                continue
            
            line = self.source_lines[line_num - 1]
            
            # 提取标识符
            identifiers = re.findall(r'\b([a-zA-Z_]\w*)\b', line)
            used.update(identifiers)
        
        # 过滤掉关键字
        keywords = {'if', 'else', 'while', 'for', 'do', 'switch', 'case', 
                   'break', 'continue', 'return', 'goto', 'sizeof', 'typedef',
                   'struct', 'union', 'enum', 'int', 'char', 'float', 'double',
                   'void', 'long', 'short', 'unsigned', 'signed', 'const', 'static',
                   'extern', 'auto', 'register', 'volatile', 'inline', 'restrict',
                   'class', 'public', 'private', 'protected', 'virtual', 'template',
                   'namespace', 'using', 'try', 'catch', 'throw', 'new', 'delete'}
        
        # 过滤掉函数名
        used -= keywords
        used -= set(self.functions.keys())
        
        # 过滤掉常见的库函数（标准C库 + POSIX + 常见第三方库）
        common_functions = {
            # stdio.h
            'printf', 'scanf', 'sprintf', 'snprintf', 'fprintf', 'fscanf',
            'sscanf', 'vprintf', 'vsprintf', 'vsnprintf', 'vfprintf',
            'fopen', 'fclose', 'fread', 'fwrite', 'fgets', 'fputs', 'fgetc', 'fputc',
            'fseek', 'ftell', 'rewind', 'feof', 'ferror', 'clearerr',
            'putchar', 'getchar', 'puts', 'gets', 'perror',
            # stdlib.h
            'malloc', 'calloc', 'realloc', 'free', 'exit', 'abort', 'atexit',
            'atoi', 'atof', 'atol', 'strtod', 'strtol', 'strtoul',
            'rand', 'srand', 'system', 'getenv', 'qsort', 'bsearch',
            'abs', 'labs', 'div', 'ldiv',
            # string.h
            'strlen', 'strcpy', 'strncpy', 'strcat', 'strncat',
            'strcmp', 'strncmp', 'strchr', 'strrchr', 'strstr', 'strtok',
            'memcpy', 'memmove', 'memset', 'memcmp', 'memchr',
            'strdup', 'strerror', 'strcoll', 'strxfrm', 'strspn', 'strcspn', 'strpbrk',
            # ctype.h
            'isalpha', 'isdigit', 'isalnum', 'isspace', 'isupper', 'islower',
            'isprint', 'isgraph', 'iscntrl', 'ispunct', 'isxdigit',
            'toupper', 'tolower',
            # math.h
            'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2',
            'sinh', 'cosh', 'tanh', 'exp', 'log', 'log10', 'pow', 'sqrt',
            'ceil', 'floor', 'fabs', 'fmod',
            # time.h
            'time', 'clock', 'difftime', 'mktime', 'strftime', 'asctime', 'ctime',
            'gmtime', 'localtime',
            # assert.h
            'assert',
            # POSIX and common extensions
            'open', 'close', 'read', 'write', 'lseek', 'fcntl', 'ioctl',
            'fork', 'exec', 'wait', 'pipe', 'dup', 'dup2',
            'chdir', 'getcwd', 'mkdir', 'rmdir', 'unlink', 'rename',
            'stat', 'fstat', 'access', 'chmod', 'chown',
            'getpid', 'getppid', 'getuid', 'getgid', 'setuid', 'setgid',
            'signal', 'kill', 'alarm', 'sleep', 'usleep',
            'pthread_create', 'pthread_join', 'pthread_exit', 'pthread_mutex_lock',
            # 常见Vim函数前缀
            'vim_', 'do_', 'ex_', 'ui_', 'ml_', 'msg_', 'buf_', 'win_',
        }
        
        # 过滤掉常见的宏和常量
        common_macros = {
            # 标准宏
            'NULL', 'TRUE', 'FALSE', 'EOF', 'BUFSIZ',
            'STDIN', 'STDOUT', 'STDERR', 
            'SEEK_SET', 'SEEK_CUR', 'SEEK_END',
            # 数值极限
            'SIZE_MAX', 'SSIZE_MAX',
            'INT_MAX', 'INT_MIN', 'UINT_MAX',
            'LONG_MAX', 'LONG_MIN', 'ULONG_MAX',
            'CHAR_MAX', 'CHAR_MIN', 'UCHAR_MAX',
            'SHRT_MAX', 'SHRT_MIN', 'USHRT_MAX',
            'FLT_MAX', 'FLT_MIN', 'DBL_MAX', 'DBL_MIN',
            # 文件权限和标志
            'O_RDONLY', 'O_WRONLY', 'O_RDWR', 'O_CREAT', 'O_TRUNC', 'O_APPEND',
            'S_IRUSR', 'S_IWUSR', 'S_IXUSR', 'S_IRWXU',
            'S_IRGRP', 'S_IWGRP', 'S_IXGRP', 'S_IRWXG',
            'S_IROTH', 'S_IWOTH', 'S_IXOTH', 'S_IRWXO',
            # 错误码
            'ENOENT', 'EACCES', 'EINVAL', 'ENOMEM', 'EEXIST',
            # Vim特定宏
            'NUL', 'NL', 'TAB', 'ESC', 'CR', 'BS',
            'MAPTYPE_', 'MODE_', 'KEYBUFLEN', 'MAXPATHL',
        }
        
        used -= common_functions
        used -= common_macros
        
        # 进一步过滤: 移除包含常见前缀的标识符(很可能是外部函数)
        external_prefixes = {'vim_', 'do_', 'ex_', 'ui_', 'ml_', 'msg_', 
                            'buf_', 'win_', 'nb_', 'gui_', 'syn_', 'eval_',
                            'get_', 'set_', 'find_', 'check_', 'init_', 'free_',
                            'alloc_', 'read_', 'write_', 'open_', 'close_'}
        
        filtered_used = set()
        for var in used:
            # 检查是否以外部函数前缀开头
            is_external = any(var.startswith(prefix) for prefix in external_prefixes)
            # 检查是否全大写(很可能是宏)
            is_macro = var.isupper() and len(var) > 1
            # 检查是否首字母大写(很可能是类型名)
            is_type = var[0].isupper() and not var.isupper()
            
            if not (is_external or is_macro or is_type):
                filtered_used.add(var)
        
        return filtered_used
    
    def _find_variable_declaration_in_function(self, var_name: str, 
                                               func: FunctionSkeleton) -> Optional[VariableDeclaration]:
        """在函数体内查找变量的声明"""
        # 在函数体范围内查找
        for i in range(func.body_start, min(func.body_end, len(self.source_lines))):
            line = self.source_lines[i]
            
            # 检查是否声明了该变量
            if re.search(rf'\b{re.escape(var_name)}\b', line):
                decls = self._extract_declarations(line, i + 1)
                for decl in decls:
                    if decl.name == var_name:
                        return decl
        
        # 检查是否是函数参数
        if var_name in func.params or any(var_name in p for p in func.params):
            # 是参数，不需要补充声明
            return None
        
        # 未找到声明，生成一个占位声明
        return VariableDeclaration(
            name=var_name,
            type_str='int',  # 默认类型
            line=func.body_start,
            in_slice=False
        )
    
    def _generate_function_body(self, func_name: str, 
                                slice_lines: List[int]) -> List[str]:
        """生成函数体"""
        lines = []
        
        # 使用状态机处理嵌套结构
        indent_level = 1
        prev_line = 0
        
        for line_num in slice_lines:
            if line_num <= 0 or line_num > len(self.source_lines):
                continue
            
            source_line = self.source_lines[line_num - 1]
            
            # 处理行间跳跃
            if prev_line > 0 and line_num - prev_line > 1:
                lines.append("")
                lines.append("    /* ... */")
                lines.append("")
            
            # 调整缩进
            indent = self._calculate_indent(source_line, indent_level)
            
            # 清理并格式化行
            cleaned = source_line.strip()
            if cleaned:
                # 添加行号注释
                indented_line = "    " * indent + cleaned
                indented_line += f"  // Line {line_num}"
                lines.append(indented_line)
            
            # 更新缩进级别
            indent_level = self._update_indent_level(source_line, indent_level)
            
            prev_line = line_num
        
        return lines
    
    def _calculate_indent(self, line: str, current_level: int) -> int:
        """计算缩进级别"""
        # 简单处理：基于当前级别
        stripped = line.strip()
        
        # 如果是结束括号，减少缩进
        if stripped.startswith('}'):
            return max(1, current_level - 1)
        
        return current_level
    
    def _update_indent_level(self, line: str, current_level: int) -> int:
        """更新缩进级别"""
        # 统计大括号
        open_count = line.count('{')
        close_count = line.count('}')
        
        return max(1, current_level + open_count - close_count)


def reconstruct_slice(source_code: str, slice_result: dict) -> str:
    """
    重构切片为语法正确的代码
    
    Args:
        source_code: 原始源代码
        slice_result: 切片结果字典（包含slice_lines和function_map）
    
    Returns:
        重构后的代码字符串
    """
    reconstructor = SliceReconstructor(
        source_code=source_code,
        slice_lines=set(slice_result['slice_lines']),
        function_map={int(k): v for k, v in slice_result['function_map'].items()}
    )
    
    return reconstructor.reconstruct()


if __name__ == '__main__':
    # 测试代码
    test_source = """
#include <stdio.h>

int global_var = 0;

struct Point {
    int x;
    int y;
};

void test_function(int param) {
    int local_var = 10;
    int x = param + local_var;
    
    if (x > 5) {
        printf("%d", x);
    }
    
    for (int i = 0; i < x; i++) {
        global_var += i;
    }
}

int main() {
    test_function(5);
    return 0;
}
"""
    
    # 模拟切片结果
    test_slice = {
        'slice_lines': [11, 12, 13, 15, 16],
        'function_map': {
            '11': 'test_function',
            '12': 'test_function',
            '13': 'test_function',
            '15': 'test_function',
            '16': 'test_function'
        }
    }
    
    result = reconstruct_slice(test_source, test_slice)
    print(result)
