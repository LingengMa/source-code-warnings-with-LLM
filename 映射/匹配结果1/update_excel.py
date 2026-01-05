import pandas as pd
import re

def parse_markdown(md_content):
    """解析Markdown文件内容，提取表格数据"""
    data = {}
    # 使用一个更简单的正则表达式直接匹配所有表格内容行
    rows = re.findall(r'^\| ([^\|]+?) *\| ([^\|]*?) *\| ([^\|]*?) *\| ([^\|]+?) *\|$', md_content, re.MULTILINE)

    for row in rows:
        identifier = row[0].strip()
        cwe_raw = row[1].strip()
        reason = row[3].strip()

        if identifier and identifier != '警告标识符':
            # 清理CWE编号，只保留数字或设置为空
            cwe_match = re.search(r'CWE-(\d+)', cwe_raw)
            cwe = cwe_match.group(1) if cwe_match else ''
            if not cwe_raw.strip(): # 如果原始cwe列为空，则cwe也为空
                cwe = ''

            data[identifier] = {
                "cwe": cwe,
                "reason": reason
            }
    return data

def update_excel(excel_path, md_data):
    """根据解析的Markdown数据更新Excel文件"""
    try:
        df = pd.read_excel(excel_path)
        
        # 假设列名是 'type', 'cwe', '原因'
        # 如果您的列名不同，请在此处修改
        id_col = 'type'
        cwe_col = 'CWE' # <--- 修改此处以匹配Excel文件
        reason_col = '原因'

        if id_col not in df.columns or cwe_col not in df.columns or reason_col not in df.columns:
            print(f"错误：Excel文件中缺少必需的列。需要 '{id_col}', '{cwe_col}', '{reason_col}'。")
            print(f"找到的列: {df.columns.tolist()}")
            return

        for index, row in df.iterrows():
            identifier = row[id_col]
            if identifier in md_data:
                df.at[index, cwe_col] = md_data[identifier]['cwe']
                df.at[index, reason_col] = md_data[identifier]['reason']
        
        df.to_excel(excel_path, index=False)
        print(f"成功更新文件: {excel_path}")

    except FileNotFoundError:
        print(f"错误：找不到Excel文件 at {excel_path}")
    except Exception as e:
        print(f"更新Excel时发生错误: {e}")


if __name__ == "__main__":
    md_file_path = 'CWE描述补充完成.md'
    excel_file_path = 'spotbugs-type-cwe - 匹配.xlsx'
    
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        markdown_data = parse_markdown(md_content)
        
        if not markdown_data:
            print("错误：未能从Markdown文件中解析出任何数据。")
        else:
            print(f"从Markdown文件中成功解析了 {len(markdown_data)} 条记录。")
            update_excel(excel_file_path, markdown_data)
            
    except FileNotFoundError:
        print(f"错误：找不到Markdown文件 at {md_file_path}")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")
