# 第13课：字典（dict）

## 用名字而不是数字查数据

列表用数字下标：`fruits[0]`。字典用**键**（名字）查找**值**：

```python demo title="创建字典"
student = {
    "name": "Anan",
    "age": 9,
    "grade": "三年级",
    "hobby": "画画"
}

print(student["name"])
print(student["age"])
print(student["hobby"])
```

## 增加、修改、删除

```python demo title="修改字典"
scores = {"语文": 95, "数学": 88, "英语": 92}

scores["科学"] = 90        # 添加新键值对
scores["数学"] = 96        # 修改已有的值
del scores["英语"]         # 删除

print(scores)
print("科目数量：", len(scores))
```

## 遍历字典

```python demo title="遍历字典"
scores = {"语文": 95, "数学": 88, "科学": 90}

for subject, score in scores.items():
    print(f"{subject}：{score} 分")
```

## 练习

```python exercise title="单词本"
vocab = {
    "apple": "苹果",
    "cat": "猫",
    "book": "书"
}

# 查找单词
word = "apple"
if word in vocab:
    print(f"{word} 的中文是：{vocab[word]}")

# 添加新单词
vocab["dog"] = "狗"
vocab["pen"] = "钢笔"

print("单词本里共有", len(vocab), "个单词")
for eng, chn in vocab.items():
    print(f"  {eng} = {chn}")
```
