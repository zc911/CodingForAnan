# 第28课练习：tkinter 游戏
# 在 Thonny 里运行！
# 改进弹球游戏——加上砖块！

import tkinter as tk

window = tk.Tk()
window.title("🧱 弹球消砖块")
canvas = tk.Canvas(window, width=500, height=400, bg="#0f3460")
canvas.pack()

# 创建砖块
bricks = []
colors = ["#e94560", "#f5a623", "#f8e71c", "#7ed321", "#4a90d9"]
for row in range(5):
    for col in range(8):
        x1 = 10 + col * 60
        y1 = 30 + row * 25
        brick = canvas.create_rectangle(x1, y1, x1 + 55, y1 + 20,
                                         fill=colors[row], outline="white")
        bricks.append(brick)

paddle = canvas.create_rectangle(200, 370, 300, 385, fill="#e94560", outline="white")
ball = canvas.create_oval(240, 350, 260, 370, fill="yellow", outline="white")

score = 0
score_text = canvas.create_text(250, 15, text=f"分数：{score}", fill="white", font=("Arial", 14))
dx, dy = 3, -3

def move_paddle(event):
    canvas.coords(paddle, event.x - 50, 370, event.x + 50, 385)

canvas.bind("<Motion>", move_paddle)

def game_loop():
    global dx, dy, score
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)

    if pos[0] <= 0 or pos[2] >= 500: dx = -dx
    if pos[1] <= 0: dy = -dy

    # 碰挡板
    pp = canvas.coords(paddle)
    if pos[3] >= pp[1] and pos[2] >= pp[0] and pos[0] <= pp[2] and dy > 0:
        dy = -dy
        score += 1
        canvas.itemconfig(score_text, text=f"分数：{score}")

    # 碰砖块
    for brick in bricks[:]:
        bp = canvas.coords(brick)
        if (pos[2] >= bp[0] and pos[0] <= bp[2] and pos[3] >= bp[1] and pos[1] <= bp[3]):
            canvas.delete(brick)
            bricks.remove(brick)
            dy = -dy
            score += 10
            canvas.itemconfig(score_text, text=f"分数：{score}")
            break

    if not bricks:
        canvas.create_text(250, 200, text="🎉 你赢了！", fill="white", font=("Arial", 30))
        return

    if pos[3] >= 400:
        canvas.create_text(250, 200, text=f"游戏结束！得分：{score}", fill="white", font=("Arial", 24))
        return

    window.after(16, game_loop)

game_loop()
window.mainloop()
