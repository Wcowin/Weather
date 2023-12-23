import pandas as pd

url = "http://www.weather.com.cn/textFC/chongqing.shtml"

try:
    tables = pd.read_html(url)
except ValueError:
    print("No tables found on the webpage.")
    tables = []

if tables:
    all_data = pd.concat([table.iloc[:, :-1] for table in tables])
    all_data.to_excel('CQ.xlsx', index=False)
else:
    print("No valid tables to process.")
