# 爬虫山东重庆各地区天气预报

![Alt text](https://img-blog.csdnimg.cn/direct/55357f61faf34994ba93c845e0ff8542.png)

## 天气数据获取工具

这个简单的Python脚本用于从[中国天气网](http://www.weather.com.cn/textFC/chongqing.shtml)获取天气数据，并将数据保存到Excel文件中。

### 功能
输入中文省份名称，获取该省份下所有城市的天气数据。    
数据保存到指定文件夹中，文件名格式为：时间_省份_城市.xlsx。  

### 使用方法
安装必要的库

```bash
pip install -r requirements.txt
```

运行code文件下的weather.py脚本：

```bash
python weather.py
```

输入中文省份名称，脚本会自动获取天气数据并保存到天气数据文件夹。

### 运行程序
双击weather.exe运行程序，输入中文省份名称，会自动获取天气数据并保存为excel文件。

### 配置
默认输出文件夹：天气数据  
默认输出文件名：当天日期-当前时间-省份.xlsx

### 依赖
```
pandas
openpyxl
pypinyin
```
### 注意事项
请确保网络连接正常，否则无法从中国天气网获取数据。  
确保已经安装所需的依赖。