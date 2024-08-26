# 基于Bench数据集的大模型测评

欢迎来到本项目！我们致力于探索和测评多个大型语言模型的表现，旨在为大家提供有价值的参考。这些测评基于Bench数据集，涵盖了从语文到数学等多个学科。让我们一起来看看各大模型在这些任务中的表现吧！

## 项目背景

我们在本项目中主要对三个大型语言模型进行了测评，涵盖了语文、数学、物理、化学等多个学科。通过对客观题的测试，深入分析了模型在不同领域的表现，以期为后续的模型开发与优化提供参考。

## 测评结果概览

1. **总体表现**：
    - GPT-4o：82.2%
    - GPT-4o mini：71.6%
    - GPT-3.5-turbo：53.2%

2. **学科表现**：
    - **语文**：GPT-4o（63.9%）表现最佳，GPT-3.5-turbo（34.7%）表现最差。
    - **英语**：GPT-4o mini（93.2%）与GPT-4o（93.1%）表现优秀。
    - **理科数学**：GPT-4o（69.3%）领先，GPT-4o mini次之。
    - **物理**：GPT-4o表现最佳，得分为61.5%。

## 环境配置与安装

### 克隆项目

```bash
git clone https://github.com/OpenLMLab/GAOKAO-Bench.git
```

### 安装依赖项

确保已安装Python及Pip，进入项目目录并安装依赖项：

```bash
cd GAOKAO-Bench
pip install numpy pandas scikit-learn openai
```

### 配置Linux终端（适用于Windows用户）

打开命令提示符，输入以下命令启用WSL并安装Ubuntu：

```bash
wsl --install
```

### 配置OpenAI API

在Azure AI Studio中获取API密钥和endpoint，将其加入到项目的配置文件中。在`openai_gpt4.py`文件中，替换为Azure的API调用方式，并配置好`endpoint`与`api key`。

## 运行测评

在Linux终端中运行以下指令开始测评：

```bash
cd /mnt/c/Users/你的用户名/GAOKAO-Bench-main/Bench/
python3 objective_bench.py --openai_api_key <your api key>
```

## 数据分析

- GPT-4o在绝大多数学科表现优异，特别是在生物和地理学科。
- GPT-4o mini表现亦不俗，尤其在科学类题目中表现突出。
- GPT-3.5-turbo整体表现较弱，特别是在语文和科学类题目中。
