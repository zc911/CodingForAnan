# 第11课：模块与 import

## 什么是模块？

Python 自带了很多"工具箱"（模块），用 `import` 打开就能用里面的工具。

## random 模块

```python demo title="random 模块"
import random

print(random.randint(1, 10))       # 1到10的随机整数
print(random.random())             # 0到1之间的随机小数

fruits = ["苹果", "香蕉", "草莓", "西瓜"]
print(random.choice(fruits))       # 随机选一个

random.shuffle(fruits)             # 随机打乱顺序
print(fruits)
```

## math 模块

```python demo title="math 模块"
import math

print(math.pi)              # 圆周率 π
print(math.sqrt(16))        # 开平方根
print(math.ceil(3.2))       # 向上取整 → 4
print(math.floor(3.8))      # 向下取整 → 3
print(math.pow(2, 10))      # 2的10次方
```

## 随机出题小程序

```python demo title="随机加法出题"
import random

num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
answer = int(input(f"{num1} + {num2} = ？"))

if answer == num1 + num2:
    print("✅ 答对了！")
else:
    print(f"❌ 答错了，正确答案是 {num1 + num2}")
```

## 练习

```python exercise title="用 random 做一道乘法题"
import random

a = random.randint(2, 9)
b = random.randint(2, 9)
answer = int(input(f"{a} × {b} = ？"))

if answer == a * b:
    print("🎉 答对了！太棒了！")
else:
    print(f"再想想，{a} × {b} = {a * b}")
```
