# 🎨 项目二：turtle 绘图

`turtle` 模块让你控制一只"小乌龟"在屏幕上画画——它走过的路就是画出的线。

> **注意：** `turtle` 需要在 Thonny 里运行（需要窗口），不能在网页里演示。把下面的代码下载到 Thonny！

## 基本命令

| 命令 | 说明 |
|------|------|
| `forward(n)` | 向前走 n 步 |
| `backward(n)` | 向后走 n 步 |
| `right(角度)` | 向右转 |
| `left(角度)` | 向左转 |
| `penup()` | 抬起画笔（移动不画线） |
| `pendown()` | 放下画笔 |
| `color("red")` | 设置颜色 |
| `speed(1~10)` | 设置速度 |

## 画一个正方形

```python thonny title="正方形"
import turtle

t = turtle.Turtle()
t.speed(5)
t.color("blue")

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

## 画一朵花

```python thonny title="旋转花朵"
import turtle

t = turtle.Turtle()
t.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.color(colors[i % len(colors)])
    t.forward(100)
    t.right(170)

turtle.done()
```

## 你的任务

选一个（或自己设计！）：
1. 用 `turtle` 画出你名字的首字母
2. 画一个五角星 ⭐（提示：每次转 144 度，画5次）
3. 画一栋小房子（正方形 + 三角形屋顶）
