# 项目三：知识小测验系统
# 在这里完成你的完整版——加更多题目，加计时，加难度等级！
import random

questions = [
    ("Python 用什么命令打印输出？", "print"),
    ("列表的第一个元素下标是多少？", "0"),
    ("定义函数用什么关键字？", "def"),
    ("True 和 False 是什么类型？", "bool"),
    ("模块导入用什么关键字？", "import"),
]

random.shuffle(questions)
score = 0
print("=== Python 知识小测验 ===\n")
for i, (q, a) in enumerate(questions, 1):
    ans = input(f"第{i}题：{q} ").strip().lower()
    if ans == a.lower():
        print("✅ 正确！")
        score += 1
    else:
        print(f"❌ 正确答案：{a}")
print(f"\n最终得分：{score}/{len(questions)}")
