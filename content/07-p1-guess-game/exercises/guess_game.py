# 项目一：猜数字游戏
# 在 Thonny 里运行！

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

print("🎉 猜对了！答案是", secret)
print("你猜了", attempts, "次")
if attempts <= 7:
    print("你真棒！🌟")
else:
    print("继续练习！💪")
