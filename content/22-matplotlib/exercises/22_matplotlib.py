# 第22课练习：数据可视化
# 在 Thonny 里运行（会弹出窗口）

import matplotlib.pyplot as plt

# 练习1：柱状图 - 家庭成员年龄
names = ["我", "爸爸", "妈妈", "爷爷", "奶奶"]
ages = [9, 38, 36, 65, 62]

plt.figure(figsize=(8, 4))
bars = plt.bar(names, ages, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
plt.title("家庭成员年龄")
plt.ylabel("岁")

# 在柱子上显示数字
for bar, age in zip(bars, ages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(age), ha='center', fontsize=12)

plt.show()

# 练习2：饼图 - 零花钱怎么花
items = ["文具", "零食", "玩具", "存起来"]
amounts = [5, 8, 7, 10]

plt.figure(figsize=(6, 6))
plt.pie(amounts, labels=items, autopct='%1.0f%%', startangle=90,
        colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
plt.title("零花钱去哪了？")
plt.show()
