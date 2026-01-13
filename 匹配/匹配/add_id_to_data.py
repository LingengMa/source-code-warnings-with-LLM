import json
import uuid
import os

def add_unique_id_to_warnings(input_file: str, output_file: str):
    """
    读取一个包含告警列表的JSON文件，为每条告警添加一个唯一的ID，
    并将结果写入新的JSON文件。

    Args:
        input_file (str): 输入的JSON文件路径。
        output_file (str): 输出的JSON文件路径。
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            warnings = json.load(f)
        
        print(f"从 {input_file} 中读取了 {len(warnings)} 条告警。")

        processed_warnings = []
        for warning in warnings:
            # 为每条告警记录添加一个基于UUID的唯一ID
            new_warning = {'id': str(uuid.uuid4())}
            
            # 统一字段名：'filename' -> 'file', 'line_number' -> 'line'
            for key, value in warning.items():
                if key == 'filename':
                    new_warning['file'] = value
                elif key == 'line_number':
                    new_warning['line'] = value
                else:
                    new_warning[key] = value
            
            processed_warnings.append(new_warning)

        # 确保输出目录存在
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(processed_warnings, f, indent=4, ensure_ascii=False)
            
        print(f"成功为所有告警添加了唯一ID并统一了字段名，并已保存到 {output_file}")
        print(f"现在共有 {len(processed_warnings)} 条带ID的告警。")

    except FileNotFoundError:
        print(f"错误: 输入文件 {input_file} 未找到。")
    except json.JSONDecodeError:
        print(f"错误: 输入文件 {input_file} 不是有效的JSON格式。")
    except Exception as e:
        print(f"处理过程中发生未知错误: {e}")

if __name__ == '__main__':
    # 定义输入和输出文件路径
    # 假设此脚本与 input 文件夹在同一目录下
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_json_path = os.path.join(base_dir, 'input', 'data.json')
    output_json_path = os.path.join(base_dir, 'input', 'data_with_id.json')
    
    # 执行添加ID的功能
    add_unique_id_to_warnings(input_json_path, output_json_path)
