import pandas as pd

# 获取网页的表格数据
url = "http://www.weather.com.cn/textFC/shandong.shtml"
tables = pd.read_html(url)

# 创建一个空的DataFrame来存储所有的表格数据
all_data = pd.DataFrame()

# 遍历所有的表格，将它们添加到主DataFrame中
for table in tables:
    all_data = pd.concat([all_data, table])

# 将主DataFrame保存为一个Excel文件
all_data.to_excel('SD.xlsx', index=False)