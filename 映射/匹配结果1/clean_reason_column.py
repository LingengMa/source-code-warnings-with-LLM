import pandas as pd

def clean_reason_column(excel_path):
    """
    读取Excel文件，移除“原因”列中所有的“**”字符，
    并保存回文件。
    """
    try:
        df = pd.read_excel(excel_path)

        reason_col = '原因'

        if reason_col not in df.columns:
            print(f"错误：Excel文件中找不到 '{reason_col}' 列。")
            print(f"找到的列: {df.columns.tolist()}")
            return

        # 将“原因”列转换为字符串类型，并移除“**”
        df[reason_col] = df[reason_col].astype(str).str.replace('**', '', regex=False)

        df.to_excel(excel_path, index=False)
        print(f"成功清理 '{reason_col}' 列中的 '**' 符号。文件已保存: {excel_path}")

    except FileNotFoundError:
        print(f"错误：找不到Excel文件 at {excel_path}")
    except Exception as e:
        print(f"处理Excel时发生错误: {e}")


if __name__ == "__main__":
    excel_file_path = 'spotbugs-type-cwe - 匹配.xlsx'
    clean_reason_column(excel_file_path)
