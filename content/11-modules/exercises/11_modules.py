# 第11课练习：模块

import random
import math

# 练习1：随机乘法出题（连续5题）
print("=== 数学小测验 ===")
correct = 0
for i in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"第{i+1}题：{a} × {b} = ？"))
    if answer == a * b:
        print("✅ 答对了！")
        correct += 1
    else:
        print(f"❌ 正确答案是 {a * b}")

print(f"\n5题答对了 {correct} 题！")

# 练习2：计算圆的面积
r = float(input("输入圆的半径："))
area = math.pi * r * r
print(f"面积 = {area:.2f}")   # :.2f 表示保留2位小数
