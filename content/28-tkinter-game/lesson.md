# 第28课：tkinter 小游戏

## Canvas：tkinter 的画布

**Canvas** 组件可以画图形（圆形、矩形、线条），还能让图形动起来——这就是做游戏的基础！

> **注意：** tkinter 游戏需要在 Thonny 里运行。把代码下载到 Thonny 试试！

## 画布基础

```python thonny title="Canvas 画图"
import tkinter as tk

window = tk.Tk()
window.title("画布试玩")
canvas = tk.Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# 画矩形
canvas.create_rectangle(50, 50, 150, 120, fill="skyblue", outline="blue", width=2)

# 画圆形
canvas.create_oval(200, 80, 280, 160, fill="pink", outline="red", width=2)

# 画文字
canvas.create_text(200, 250, text="这是我的画布！", font=("Arial", 16), fill="purple")

# 画线条
canvas.create_line(50, 200, 350, 200, fill="green", width=3, dash=(5, 3))

window.mainloop()
```

## 让图形动起来

用 `canvas.move()` 移动图形，用 `window.after()` 定时重复——图形就"动"了：

```python thonny title="弹跳的小球"
import tkinter as tk

window = tk.Tk()
window.title("弹跳小球")
canvas = tk.Canvas(window, width=400, height=300, bg="#1a1a2e")
canvas.pack()

# 创建小球
ball = canvas.create_oval(180, 130, 220, 170, fill="#e94560", outline="white", width=2)

# 小球的速度
dx = 3   # 水平速度
dy = 2   # 垂直速度

def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)

    # 获取小球位置
    pos = canvas.coords(ball)

    # 碰到左右边界就反弹
    if pos[0] <= 0 or pos[2] >= 400:
        dx = -dx
    # 碰到上下边界就反弹
    if pos[1] <= 0 or pos[3] >= 300:
        dy = -dy

    # 每20毫秒移动一次（越小说越快）
    window.after(20, move_ball)

move_ball()   # 开始动画
window.mainloop()
```

## 完整弹球游戏

```python thonny title="弹球游戏"
import tkinter as tk

window = tk.Tk()
window.title("🏓 弹球游戏")
canvas = tk.Canvas(window, width=500, height=400, bg="#0f3460")
canvas.pack()

# 挡板
paddle = canvas.create_rectangle(200, 370, 300, 385, fill="#e94560", outline="white")

# 小球
ball = canvas.create_oval(240, 350, 260, 370, fill="yellow", outline="white")

# 分数
score = 0
score_text = canvas.create_text(250, 20, text=f"分数：{score}", fill="white", font=("Arial", 16))

# 速度
dx, dy = 3, -3

def move_paddle(event):
    # 鼠标控制挡板
    x = event.x
    canvas.coords(paddle, x - 50, 370, x + 50, 385)

canvas.bind("<Motion>", move_paddle)

def game_loop():
    global dx, dy, score
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)

    # 碰墙反弹
    if pos[0] <= 0 or pos[2] >= 500:
        dx = -dx
    if pos[1] <= 0:
        dy = -dy

    # 碰到挡板
    paddle_pos = canvas.coords(paddle)
    if (pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]
        and pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]):
        dy = -dy
        score += 1
        canvas.itemconfig(score_text, text=f"分数：{score}")

    # 掉到底部
    if pos[3] >= 400:
        canvas.create_text(250, 200, text=f"游戏结束！得分：{score}", fill="white", font=("Arial", 24))
        return

    window.after(16, game_loop)

game_loop()
window.mainloop()
```

## tkinter 游戏的关键

| 技术 | 作用 |
|------|------|
| `Canvas` | 画图形的画布 |
| `canvas.move(item, dx, dy)` | 移动图形 |
| `canvas.coords(item)` | 获取图形位置 |
| `window.after(ms, function)` | 定时调用函数（游戏循环） |
| `canvas.bind(event, handler)` | 绑定键盘/鼠标事件 |

## 练习

试着改进弹球游戏：
1. 让球速随分数增加
2. 加上砖块，球碰到砖块消除得分
3. 加上"开始"和"重新开始"按钮
