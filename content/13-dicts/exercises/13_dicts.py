# 第13课练习：字典

# 建立一个关于你自己的字典
me = {
    "name": "___",
    "age": 0,
    "hobby": "___",
    "favorite_food": "___",
    "best_subject": "___"
}

print("=== 关于我 ===")
for key, value in me.items():
    print(f"{key}: {value}")

# 简单的单词测试
vocab = {"sun": "太阳", "moon": "月亮", "star": "星星", "cloud": "云"}

print("\n=== 英语小测验 ===")
for word, meaning in vocab.items():
    answer = input(f"'{word}' 是什么意思？")
    if answer.strip() == meaning:
        print("✅ 正确！")
    else:
        print(f"❌ 正确答案是：{meaning}")
