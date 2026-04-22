# 第27课练习：tkinter 基础
# 在 Thonny 里运行！

import tkinter as tk

def add_item():
    text = entry.get()
    if text.strip():
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

def clear_all():
    listbox.delete(0, tk.END)

window = tk.Tk()
window.title("我的待办清单")
window.geometry("300x350")

# 输入区域
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.X)
entry.bind("<Return>", lambda e: add_item())  # 按回车也能添加

# 按钮区域
frame = tk.Frame(window)
frame.pack()
tk.Button(frame, text="添加", command=add_item, font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="清空", command=clear_all, font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

# 列表区域
listbox = tk.Listbox(window, font=("Arial", 14))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

window.mainloop()
