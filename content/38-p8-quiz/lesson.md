# 第38课：🧪 项目八：单词测验生成器

## 这个项目做什么？

做一个**单词测验生成器**！它能：

- 📚 从文件读取词库
- 🎲 随机出题
- 🎯 自动判分
- ⚙️ 用命令行参数控制模式

## 需求分析

程序要实现：

1. 从 JSON 文件读取词库
2. 支持3种模式：英译中、中译英、混合
3. 用 argparse 选择模式和题目数量
4. 答完后显示得分和错题

## 第一步：设计词库格式

创建 `words.json` 文件（先在代码里创建一个示例）：

```python thonny title="创建词库文件"
import json
from pathlib import Path

# 示例词库
word_bank = [
    {"en": "apple", "cn": "苹果"},
    {"en": "cat", "cn": "猫"},
    {"en": "book", "cn": "书"},
    {"en": "water", "cn": "水"},
    {"en": "sun", "cn": "太阳"},
    {"en": "moon", "cn": "月亮"},
    {"en": "flower", "cn": "花"},
    {"en": "fish", "cn": "鱼"},
    {"en": "happy", "cn": "开心的"},
    {"en": "friend", "cn": "朋友"},
    {"en": "school", "cn": "学校"},
    {"en": "music", "cn": "音乐"},
    {"en": "computer", "cn": "电脑"},
    {"en": "dream", "cn": "梦想"},
    {"en": "animal", "cn": "动物"},
]

# 保存词库
Path("words.json").write_text(
    json.dumps(word_bank, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"✅ 词库已保存，共 {len(word_bank)} 个单词")
```

## 第二步：核心出题逻辑

```python thonny title="出题与判分"
import json
import random

def load_words(filepath="words.json"):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

def run_quiz(words, mode="en2cn", count=5):
    """运行测验"""
    score = 0
    wrong = []
    questions = random.sample(words, min(count, len(words)))

    print(f"\n📝 单词测验开始！模式：{mode}，共 {len(questions)} 题\n")

    for i, word in enumerate(questions, 1):
        if mode == "en2cn":
            question = word["en"]
            answer = word["cn"]
        else:
            question = word["cn"]
            answer = word["en"]

        user_answer = input(f"第{i}题：{question} = ")

        if user_answer.strip() == answer:
            print("  ✅ 正确！")
            score += 1
        else:
            print(f"  ❌ 错误！正确答案：{answer}")
            wrong.append({"question": question, "correct": answer,
                          "yours": user_answer})

    print(f"\n📊 得分：{score}/{len(questions)}")
    if wrong:
        print("\n❌ 错题回顾：")
        for w in wrong:
            print(f"  {w['question']} = {w['correct']}（你答了：{w['yours']}）")

    return score, wrong

# 测试（用固定数据，不用 input）
words = load_words()
print(f"词库有 {len(words)} 个单词")
sample = random.sample(words, 3)
print("随机3个词：", [(w["en"], w["cn"]) for w in sample])
```

## 第三步：加上 argparse

```python thonny title="完整程序 + argparse"
import argparse
import json
import random
import sys

def main():
    parser = argparse.ArgumentParser(description="📝 单词测验生成器")
    parser.add_argument("--mode", choices=["en2cn", "cn2en", "mix"],
                        default="en2cn", help="测验模式")
    parser.add_argument("--count", type=int, default=5, help="题目数量")
    parser.add_argument("--file", default="words.json", help="词库文件")

    # 模拟命令行（在 Thonny 中运行）
    sys.argv = ["quiz.py", "--mode", "en2cn", "--count", "3"]

    args = parser.parse_args()

    words = load_words(args.file)
    print(f"📚 词库：{len(words)} 个单词")
    print(f"📝 模式：{args.mode}，题数：{args.count}")

    if args.mode == "mix":
        # 混合模式：每题随机选方向
        for word in random.sample(words, min(args.count, len(words))):
            if random.random() < 0.5:
                print(f"  英→中：{word['en']} = ?")
            else:
                print(f"  中→英：{word['cn']} = ?")
    else:
        # 实际运行测验（需要输入，这里只展示框架）
        print("  （运行测验需要真实输入，请在终端中运行）")

if __name__ == "__main__":
    main()
```

## 扩展挑战

- 💾 **保存成绩**：把每次得分写入 `scores.json`，可以查看历史成绩
- 📓 **错题本**：把错题单独保存，下次可以专门复习错题
- 📈 **成绩趋势**：用 matplotlib 画出历次得分折线图
- 🔄 **间隔重复**：答错的词下次出现概率更高（类似 Anki）