# 🎮 项目一：猜数字游戏

恭喜完成阶段二！现在把 `if`、`while`、`random` 结合起来写一个完整游戏。

## 游戏规则

1. 电脑随机选一个 1-100 的数
2. 玩家不断猜
3. 每次猜完，电脑提示"大了"或"小了"
4. 猜对了，显示猜了几次

## 先试试浏览器演示版（1-20，更容易猜）

```python demo title="猜数字游戏（演示版，范围1-20）"
import random

secret = random.randint(1, 20)
attempts = 0
guess = 0

print("我想了一个 1 到 20 之间的数！")

while guess != secret:
    guess = int(input("你猜："))
    attempts += 1
    if guess < secret:
        print("小了！再试试 ↑")
    elif guess > secret:
        print("大了！再试试 ↓")

print("🎉 猜对了！你猜了", attempts, "次！")
```

## 在 Thonny 里跑完整版

```python exercise title="猜数字游戏（完整版，在 Thonny 运行）"
import random

secret = random.randint(1, 100)
attempts = 0
guess = 0

print("=" * 30)
print("欢迎玩猜数字游戏！")
print("我想了 1 到 100 之间的一个数")
print("=" * 30)

while guess != secret:
    guess = int(input("你猜（1-100）："))
    attempts += 1
    if guess < secret:
        print("小了！↑")
    elif guess > secret:
        print("大了！↓")

print()
print("🎉 猜对了！答案是", secret)
print("你猜了", attempts, "次")
if attempts <= 7:
    print("你真棒，猜的次数很少！🌟")
else:
    print("继续练习，下次会更快！💪")
```

## 挑战

- 加一个最多猜10次的限制，超过就输了
- 游戏结束后问"要再玩一局吗？"
