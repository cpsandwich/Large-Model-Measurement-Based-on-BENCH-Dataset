import sys
import os
import json
import argparse
from Models.openai_gpt4 import OpenaiAPI
from bench_function import export_distribute_json, export_union_json

def load_prompt_data(file_path):
    """加载JSON文件中的提示数据。"""
    with open(file_path, "r", encoding='utf-8') as f:
        return json.load(f)['examples']

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--openai_api_key', type=str, required=True, help="OpenAI API key")
    args = parser.parse_args()

    # 获取OpenAI API密钥和初始化模型
    openai_api_key = args.openai_api_key
    model_name = "gpt-4o"
    model_api = OpenaiAPI([openai_api_key], model_name=model_name)

    # 加载提示数据
    data = load_prompt_data("Obj_Prompt.json")

    # 定义保存目录
    output_directory = "../Data/Objective_Questions"

    # 生成和保存JSON文件
    for item in data:
        keyword = item['keyword']
        question_type = item['type']
        zero_shot_prompt_text = item['prefix_prompt']

        print(f"Model: {model_name}\nKeyword: {keyword}\nType: {question_type}")

        export_distribute_json(
            model_api,
            model_name,
            output_directory,
            keyword,
            zero_shot_prompt_text,
            question_type,
            parallel_num=1
        )

        export_union_json(
            output_directory,
            model_name,
            keyword,
            zero_shot_prompt_text,
            question_type
        )

if __name__ == "__main__":
    main()
