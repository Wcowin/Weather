import os
import pandas as pd
from datetime import datetime
from pypinyin import pinyin, Style

# 获取指定省份的天气数据，并保存到指定文件夹中
def get_weather_data(province_name, output_folder='天气数据', output_filename='output.xlsx'):
    # 将中文省份名称转换为拼音
    pinyin_name = ''.join([''.join(item) for item in pinyin(province_name, style=Style.NORMAL)])

    # 构造天气数据的URL
    url = f"http://www.weather.com.cn/textFC/{pinyin_name}.shtml"

    try:
        # 使用pandas的read_html函数读取网页中的表格数据
        tables = pd.read_html(url)
    except Exception as e:
        print(f"Error: {e}")
        return None

    if not tables:
        print(f"No valid tables to process for {province_name}.")
        return None

    # 合并所有表格的数据
    all_data = pd.concat([table.iloc[:, :-1] for table in tables])

    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 生成带有路径的输出文件名
    output_filename = generate_output_filename(output_folder, pinyin_name, output_filename)

    # 将数据保存到Excel文件中
    all_data.to_excel(output_filename, index=False)
    return output_filename

# 生成带有时间戳和省份拼音的输出文件名
def generate_output_filename(output_folder, pinyin_name, base_filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(output_folder, f"{timestamp}_{pinyin_name}_{base_filename}")

if __name__ == "__main__":
    # 从终端输入省份名称
    province_name = input("请输入省份名称（中文）: ")
    output_folder = '天气数据'
    # 获取天气数据并保存到文件中
    output_filename = get_weather_data(province_name, output_folder=output_folder)
    if output_filename:
        print(f"Data saved to {output_filename}")