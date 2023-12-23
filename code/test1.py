#对终端话，输入中文省份名称，获取该省份下所有城市的天气数据，并将数据保存到 Excel 文件中。
import pandas as pd
from pypinyin import pinyin, Style

def get_weather_data(city_name):
    # 将中文城市名称转换为拼音
    pinyin_name = ''.join([''.join(item) for item in pinyin(city_name, style=Style.NORMAL)])

    # 构造 URL
    url = f"http://www.weather.com.cn/textFC/{pinyin_name}.shtml"

    try:
        tables = pd.read_html(url)
    except ValueError:
        print(f"No tables found for {city_name}.")
        return

    if not tables:
        print(f"No valid tables to process for {city_name}.")
        return

    all_data = pd.concat([table.iloc[:, :-1] for table in tables])
    all_data.to_excel(f'{pinyin_name}.xlsx', index=False)

if __name__ == "__main__":
    # 获取用户输入的城市名称
    city_name = input("请输入省份名称（中文）: ")
    get_weather_data(city_name)
