# 🛠️ 项目三：自选综合项目

恭喜！你已经学完了所有课程！现在选一个你最感兴趣的项目来完成。

---

## 选项 A：知识小测验系统

出10道题，自动判分，支持任意科目：

```python exercise title="选项 A：知识小测验（在 Thonny 运行）"
# 在 p3_quiz.py 里完成完整版
import random

questions = [
    ("Python 用什么命令打印输出？", "print"),
    ("列表的第一个元素下标是多少？", "0"),
    ("定义函数用什么关键字？", "def"),
    ("循环用什么关键字？", "for"),
    ("True 和 False 是什么数据类型？", "bool"),
]

random.shuffle(questions)
score = 0

print("=== Python 知识小测验 ===\n")
for i, (question, answer) in enumerate(questions, 1):
    user = input(f"第{i}题：{question} ").strip().lower()
    if user == answer.lower():
        print("✅ 正确！")
        score += 1
    else:
        print(f"❌ 正确答案是：{answer}")
    print()

print(f"你答对了 {score}/{len(questions)} 题！")
```

---

## 选项 B：个人日记本

可以写日记、查看历史、搜索关键词：

```python exercise title="选项 B：日记本（在 Thonny 运行）"
# 在 p3_diary.py 里完成完整版
# 功能：1-写日记 2-查看所有 3-搜索 4-退出
import datetime

DIARY_FILE = "my_diary.txt"

def write_entry():
    date = datetime.date.today()
    content = input("今天想写什么？\n> ")
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n【{date}】\n{content}\n")
    print("✅ 日记已保存！")

def read_all():
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("还没有日记，快去写第一篇！")

while True:
    print("\n1. 写日记  2. 查看所有  3. 退出")
    choice = input("选择：")
    if choice == "1": write_entry()
    elif choice == "2": read_all()
    elif choice == "3": break
```

---

## 选项 C：智能计算器

支持加减乘除，有历史记录，能处理错误输入：

```python exercise title="选项 C：计算器（在 Thonny 运行）"
# 在 p3_calculator.py 里完成完整版
history = []

def calculate(expression):
    try:
        result = eval(expression)   # eval 可以计算字符串里的数学表达式
        history.append(f"{expression} = {result}")
        return result
    except ZeroDivisionError:
        return "❌ 不能除以零"
    except Exception:
        return "❌ 无效的表达式"

print("=== 智能计算器 ===")
print("输入数学表达式（如 3 + 4 * 2），输入 q 退出，输入 h 查看历史")

while True:
    expr = input("\n计算：").strip()
    if expr.lower() == "q":
        break
    elif expr.lower() == "h":
        print("计算历史：")
        for item in history:
            print(" ", item)
    else:
        print("=", calculate(expr))
```
