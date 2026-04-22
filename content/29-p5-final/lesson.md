# 🚀 项目五：自选终极大作

恭喜！你已经学完了所有课程！现在选一个你最感兴趣的终极项目来完成。

---

## 选项 A：AI 小助手

整合 AI 对话能力，做一个有特殊功能的智能助手：

```python thonny title="选项 A：AI 小助手"
import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

messages = [
    {"role": "system", "content": """你是一个全能学习助手，有以下功能：
1. 回答问题（知识问答）
2. 写诗（输入"写诗 主题"）
3. 翻译（输入"翻译 内容"）
4. 讲笑话
5. 解释代码（输入"解释 代码"）
根据用户输入自动判断功能。"""},
]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"model": "deepseek-chat", "messages": messages}
    response = requests.post(URL, headers=headers, json=data)
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

print("🤖 AI 小助手")
print("输入'退出'结束，输入'菜单'查看功能")
print("=" * 40)

while True:
    user_input = input("你：")
    if user_input.strip() in ["退出", "exit"]:
        print("再见！👋")
        break
    reply = chat(user_input)
    print(f"AI：{reply}\n")
```

---

## 选项 B：tkinter 贪吃蛇

做一个完整的贪吃蛇游戏：

```python thonny title="选项 B：贪吃蛇"
# 贪吃蛇游戏框架——完善它！
import tkinter as tk
import random

window = tk.Tk()
window.title("🐍 贪吃蛇")
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

GRID = 20  # 每格大小
snake = [(100, 100), (80, 100), (60, 100)]  # 蛇身坐标
direction = "Right"
food = None
score = 0

score_text = canvas.create_text(200, 15, text=f"分数：{score}", fill="white", font=("Arial", 14))

def draw():
    canvas.delete("snake")
    canvas.delete("food")
    # 画蛇
    for i, (x, y) in enumerate(snake):
        color = "#4CAF50" if i == 0 else "#8BC34A"
        canvas.create_rectangle(x, y, x + GRID, y + GRID, fill=color, outline="darkgreen", tags="snake")
    # 画食物
    if food:
        canvas.create_rectangle(food[0], food[1], food[0] + GRID, food[1] + GRID,
                                fill="red", tags="food")

def spawn_food():
    global food
    x = random.randint(0, 19) * GRID
    y = random.randint(1, 19) * GRID
    food = (x, y)

def change_dir(event):
    global direction
    key = event.keysym
    if key == "Up" and direction != "Down": direction = "Up"
    elif key == "Down" and direction != "Up": direction = "Down"
    elif key == "Left" and direction != "Right": direction = "Left"
    elif key == "Right" and direction != "Left": direction = "Right"

window.bind("<Key>", change_dir)

def game_loop():
    global score
    # 移动蛇头
    head_x, head_y = snake[0]
    if direction == "Up": head_y -= GRID
    elif direction == "Down": head_y += GRID
    elif direction == "Left": head_x -= GRID
    elif direction == "Right": head_x += GRID

    # 边界检测
    if head_x < 0 or head_x >= 400 or head_y < GRID or head_y >= 400:
        canvas.create_text(200, 200, text=f"游戏结束！得分：{score}", fill="white", font=("Arial", 20))
        return

    # 吃食物
    new_head = (head_x, head_y)
    snake.insert(0, new_head)
    if food and new_head == food:
        score += 10
        canvas.itemconfig(score_text, text=f"分数：{score}")
        spawn_food()
    else:
        snake.pop()

    draw()
    window.after(120, game_loop)

spawn_food()
game_loop()
window.mainloop()
```

---

## 选项 C：数据分析报告

用 matplotlib 分析数据，生成可视化报告：

```python thonny title="选项 C：数据分析"
# 分析班级成绩数据
import matplotlib.pyplot as plt
import json

# 模拟数据（可以改成你的真实数据）
students = [
    {"name": "Anan", "math": 95, "chinese": 88, "english": 92},
    {"name": "小明", "math": 78, "chinese": 95, "english": 85},
    {"name": "小红", "math": 88, "chinese": 82, "english": 98},
    {"name": "小刚", "math": 92, "chinese": 76, "english": 80},
    {"name": "小美", "math": 85, "chinese": 90, "english": 88},
]

names = [s["name"] for s in students]
math = [s["math"] for s in students]
chinese = [s["chinese"] for s in students]
english = [s["english"] for s in students]

# 1. 各科成绩对比柱状图
plt.figure(figsize=(10, 5))
x = range(len(names))
width = 0.25
plt.bar([i - width for i in x], math, width, label="数学", color="#4ECDC4")
plt.bar(x, chinese, width, label="语文", color="#FF6B6B")
plt.bar([i + width for i in x], english, width, label="英语", color="#45B7D1")
plt.xticks(x, names)
plt.title("班级成绩对比")
plt.ylabel("分数")
plt.legend()
plt.ylim(60, 100)
plt.tight_layout()
plt.show()

# 2. 平均分饼图
avg_math = sum(math) / len(math)
avg_chinese = sum(chinese) / len(chinese)
avg_english = sum(english) / len(english)

print(f"数学平均：{avg_math:.1f}")
print(f"语文平均：{avg_chinese:.1f}")
print(f"英语平均：{avg_english:.1f}")

# 3. 个人雷达图（选做）
# 提示：搜索 "matplotlib radar chart"
```
