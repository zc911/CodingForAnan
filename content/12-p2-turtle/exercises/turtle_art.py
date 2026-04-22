# 项目二：turtle 绘图
# 在 Thonny 里运行！

import turtle

t = turtle.Turtle()
t.speed(8)

# 画五角星
t.color("gold")
t.begin_fill()
for i in range(5):
    t.forward(150)
    t.right(144)
t.end_fill()

# 在星星旁边写名字
t.penup()
t.goto(-60, -180)
t.pendown()
t.color("purple")
t.write("Anan ⭐", font=("Arial", 24, "bold"))

turtle.done()
