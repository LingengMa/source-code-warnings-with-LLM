import json
from openai import OpenAI
import os
from prompt import PROMPT_TEMPLATE
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置API密钥（从环境变量获取）
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def process_data_with_llm(data, retries=3, retry_delay=5):
    """
    使用LLM处理单条数据，包含重试机制
    """
    # 构造发送给LLM的完整提示词
    prompt = PROMPT_TEMPLATE + json.dumps(data, indent=2, ensure_ascii=False)
    
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",  # 或 "deepseek-coder"
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                temperature=0.1, # 设置较低的温度以获得更稳定的输出
            )
            
            llm_output = response.choices[0].message.content
            # 尝试解析LLM返回的JSON
            result = json.loads(llm_output)
            # 合并原始数据和LLM的返回结果
            result.update(data)
            return result # 成功则返回结果

        except json.JSONDecodeError:
            print(f"警告：ID {data.get('id')} 无法解析LLM返回的JSON，将不会重试。原始输出: {llm_output}")
            return None # JSON解析错误通常不是临时问题，直接返回None
        except Exception as e:
            print(f"错误：ID {data.get('id')} 调用API时出错: {e}。正在进行第 {attempt + 1}/{retries} 次重试...")
            if attempt < retries - 1:
                time.sleep(retry_delay)
            else:
                print(f"错误：ID {data.get('id')} 在重试 {retries} 次后仍然失败。")
                return None
    return None

def main():
    """
    主函数，用于读取数据、处理并保存结果
    """
    input_filepath = 'input/data_for_llm.json'
    output_filepath = 'output/llm_results.json'

    # 读取输入数据
    with open(input_filepath, 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    # 为每条数据添加一个唯一的ID
    for i, data_item in enumerate(input_data):
        data_item['id'] = i + 1

    results = []
    processed_ids = set()

    # 断点续传：加载已有结果
    if os.path.exists(output_filepath):
        try:
            with open(output_filepath, 'r', encoding='utf-8') as f:
                results = json.load(f)
                processed_ids = {item['id'] for item in results}
                print(f"已加载 {len(results)} 条已有结果，将从断点处继续。")
        except (json.JSONDecodeError, IOError) as e:
            print(f"警告：无法加载或解析现有结果文件，将重新开始。错误: {e}")
            results = []
            processed_ids = set()

    # 过滤掉已处理的数据
    tasks_to_process = [item for item in input_data if item['id'] not in processed_ids]
    
    if not tasks_to_process:
        print("所有数据均已处理完毕。")
        return

    total_tasks = len(tasks_to_process)
    print(f"共有 {total_tasks} 条新数据待处理。")
    
    processed_count = 0

    with ThreadPoolExecutor(max_workers=4) as executor:
        # 提交任务
        future_to_data = {executor.submit(process_data_with_llm, data_item): data_item for data_item in tasks_to_process}

        for future in as_completed(future_to_data):
            data_item = future_to_data[future]
            try:
                result = future.result()
                if result:
                    results.append(result)
                    print(f"处理成功: ID {result['id']}")
                else:
                    print(f"处理失败: ID {data_item['id']}")
                
                processed_count += 1
                
                # 每处理10条数据保存一次
                if processed_count % 10 == 0:
                    with open(output_filepath, 'w', encoding='utf-8') as f:
                        json.dump(results, f, indent=2, ensure_ascii=False)
                    print(f"--- 进度已保存：已处理 {processed_count}/{total_tasks} ---")

            except Exception as exc:
                print(f"ID {data_item['id']} 在处理时产生异常: {exc}")

    # 最终保存所有结果
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n处理完成！总共 {len(results)} 条结果已保存到 {output_filepath}")

if __name__ == "__main__":
    main()