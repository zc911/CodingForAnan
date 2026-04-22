# 第4课练习：条件判断

# 练习1：奇偶数判断
number = int(input("输入一个整数："))
if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")

# 练习2：成绩等级
score = int(input("输入你的分数（0-100）："))
if score >= 90:
    print("优秀！🌟")
elif score >= 80:
    print("良好！👍")
elif score >= 60:
    print("及格 📚")
else:
    print("需要加油 💪")
