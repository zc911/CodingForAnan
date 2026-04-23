# 第22课：数据可视化（matplotlib）

## 用图表说话

数据光看数字不够直观，画成图表一目了然！

> **注意：** matplotlib 需要在 Thonny 里运行（会弹出图表窗口）。先安装：`pip install matplotlib`

> 🖥️ **计算机小知识**
>
> **数据**和**信息**是一回事吗？不是！
>
> - **数据**是原始的数字和文字：`37.2, 36.8, 38.5, 37.0`
> - **信息**是数据经过整理后，你能读懂的东西："第3天体温偏高，可能发烧了"
>
> 一堆数字本身没有意义，但画成折线图，你一眼就能看出趋势。**数据可视化**就是把数据变成信息的魔法——用图表代替数字，让人脑（而不是电脑）更快地理解。

```python thonny title="第一个柱状图"
import matplotlib.pyplot as plt

# Anan 的零花钱记录
months = ["1月", "2月", "3月", "4月", "5月", "6月"]
money = [20, 15, 30, 25, 10, 35]

plt.figure(figsize=(8, 4))
plt.bar(months, money, color='skyblue')
plt.title("Anan 的零花钱")
plt.ylabel("元")
plt.xlabel("月份")
plt.show()
```

## 饼图：时间分配

```python thonny title="饼图：一天的时间分配"
import matplotlib.pyplot as plt

activities = ["睡觉", "上学", "作业", "玩耍", "吃饭", "其他"]
hours = [9, 6, 2, 3, 2, 2]
colors = ['#FF9999', '#66B2FF', '#FFCC99', '#99FF99', '#FF99CC', '#CCCCCC']

plt.figure(figsize=(6, 6))
plt.pie(hours, labels=activities, colors=colors, autopct='%1.0f%%', startangle=90)
plt.title("Anan 一天的时间分配")
plt.show()
```

## 折线图：成绩趋势

```python thonny title="折线图：数学成绩趋势"
import matplotlib.pyplot as plt

exams = ["第1次", "第2次", "第3次", "第4次", "第5次"]
math_scores = [78, 82, 85, 88, 95]
chinese_scores = [90, 88, 92, 91, 94]

plt.figure(figsize=(8, 4))
plt.plot(exams, math_scores, 'o-', color='blue', label='数学')
plt.plot(exams, chinese_scores, 's-', color='red', label='语文')
plt.title("成绩趋势")
plt.ylabel("分数")
plt.ylim(70, 100)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## 练习

```python thonny title="画你的数据图表"
import matplotlib.pyplot as plt

# 画出你最喜欢的科目投票结果
subjects = ["语文", "数学", "英语", "科学", "美术", "体育"]
votes = [3, 8, 5, 6, 10, 12]

plt.figure(figsize=(8, 4))
plt.barh(subjects, votes, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
plt.title("最喜欢的科目投票")
plt.xlabel("票数")
plt.show()
```
