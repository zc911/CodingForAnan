# 第27课：tkinter 窗口程序入门

之前我们的程序都在终端里运行（打字输入、文字输出）。**tkinter** 让你做真正的窗口程序——有按钮、输入框、文字显示！

> **注意：** tkinter 需要在 Thonny 里运行（需要窗口），不能在网页里演示。把代码下载到 Thonny 试试！

## 第一个窗口程序

```python exercise title="Hello tkinter！（在 Thonny 运行）"
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title("我的第一个窗口")
window.geometry("300x200")

# 添加一个标签
label = tk.Label(window, text="你好，Anan！🎉", font=("Arial", 18))
label.pack(pady=30)

# 添加一个按钮
def say_hi():
    label.config(text="你点了按钮！✨")

button = tk.Button(window, text="点我！", command=say_hi, font=("Arial", 14))
button.pack()

# 运行主循环
window.mainloop()
```

## tkinter 基本组件

| 组件 | 英文 | 用途 |
|------|------|------|
| 窗口 | `Tk()` | 程序的主窗口 |
| 标签 | `Label` | 显示文字 |
| 按钮 | `Button` | 点击触发动作 |
| 输入框 | `Entry` | 让用户输入一行文字 |
| 文本框 | `Text` | 多行文字输入/显示 |

## 做一个简易计算器

```python exercise title="简易计算器（在 Thonny 运行）"
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "×":
            result = num1 * num2
        elif op == "÷":
            result = num1 / num2 if num2 != 0 else "不能除以零"
        result_label.config(text=f"= {result}")
    except ValueError:
        result_label.config(text="请输入数字！")

window = tk.Tk()
window.title("简易计算器")
window.geometry("320x200")

# 输入框1
entry1 = tk.Entry(window, width=10, font=("Arial", 16))
entry1.grid(row=0, column=0, padx=5, pady=10)

# 运算符选择
operation = tk.StringVar(value="+")
ops = ["+", "-", "×", "÷"]
op_menu = tk.OptionMenu(window, operation, *ops)
op_menu.config(font=("Arial", 12))
op_menu.grid(row=0, column=1, padx=5)

# 输入框2
entry2 = tk.Entry(window, width=10, font=("Arial", 16))
entry2.grid(row=0, column=2, padx=5, pady=10)

# 计算按钮
calc_btn = tk.Button(window, text="计算", command=calculate, font=("Arial", 14))
calc_btn.grid(row=1, column=0, columnspan=3, pady=10)

# 结果标签
result_label = tk.Label(window, text="= ?", font=("Arial", 20), fg="blue")
result_label.grid(row=2, column=0, columnspan=3)

window.mainloop()
```

## tkinter 程序的结构

```
1. import tkinter
2. 创建窗口 Tk()
3. 添加组件（Label、Button、Entry...）
4. 排列组件（pack / grid）
5. 绑定事件（按钮点击 → 函数）
6. mainloop() 启动主循环
```

## 练习

做一个"心情日记"程序：
- 输入框写今天的日期
- 输入框写今天的心情
- 点按钮保存，显示在下方
