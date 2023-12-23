# 弹窗查询天气信息
import pandas as pd
from pypinyin import pinyin, Style
import tkinter as tk
from tkinter import ttk, messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("天气信息查询-21电子二王科文")

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure('TButton', padding=(10, 5, 10, 5), font='Helvetica 10')
        style.configure('TEntry', padding=(5, 5, 5, 5), font='Helvetica 10')
        style.configure('TLabel', font='Helvetica 10')
        style.configure('TFrame', relief=tk.RAISED, borderwidth=5)

        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack()

        self.entry_label = ttk.Label(self.frame, text="请输入省份名称:")
        self.entry_label.grid(row=0, column=0, pady=10)

        self.entry = ttk.Entry(self.frame)
        self.entry.grid(row=0, column=1, pady=10, padx=(0, 10))

        self.query_button = ttk.Button(self.frame, text="查询", command=self.query_weather)
        self.query_button.grid(row=1, column=0, columnspan=2, pady=10)

    def query_weather(self):
        city_name = self.entry.get()

        try:
            result = self.get_weather_data(city_name)

            if result is not None:
                self.show_message("查询成功", f"{city_name}的天气信息已保存到Excel文件。")
                if not self.show_yesno_message("继续查询", "是否继续查询？"):
                    self.root.destroy()
            else:
                self.show_message("查询失败", f"无法获取{city_name}的天气信息。")

        except Exception as e:
            self.show_message("错误", f"发生错误：{str(e)}")

    def get_weather_data(self, city_name):
        pinyin_name = ''.join([''.join(item) for item in pinyin(city_name, style=Style.NORMAL)])
        url = f"http://www.weather.com.cn/textFC/{pinyin_name}.shtml"

        tables = pd.read_html(url)

        if tables:
            all_data = pd.concat([table.iloc[:, :-1] for table in tables])
            all_data.to_excel(f'{pinyin_name}_weather.xlsx', index=False)
            return all_data

        return None

    @staticmethod
    def show_message(title, message):
        messagebox.showinfo(title, message)

    @staticmethod
    def show_yesno_message(title, message):
        return messagebox.askyesno(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()