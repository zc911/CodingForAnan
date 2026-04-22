# 第22课：数据可视化（matplotlib）

## 用图表说话

数据光看数字不够直观，画成图表一目了然！

> **注意：** matplotlib 在 Pyodide 中可以运行，图表会直接显示在代码块下方。在 Thonny 里运行会弹出窗口。

```python demo title="第一个柱状图"
import matplotlib
matplotlib.use('agg')
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

```python demo title="饼图：一天的时间分配"
import matplotlib
matplotlib.use('agg')
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

```python demo title="折线图：数学成绩趋势"
import matplotlib
matplotlib.use('agg')
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

```python exercise title="画你的数据图表"
import matplotlib
matplotlib.use('agg')
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
