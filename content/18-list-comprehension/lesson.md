# 第18课：列表推导式

## 还记得这样写吗？

之前我们用 for 循环来创建新列表：

```python demo title="用 for 循环创建列表"
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)
```

Python 有一种更简洁的写法——**列表推导式**（list comprehension），一行代码搞定：

```python demo title="列表推导式：一行搞定"
squares = [i ** 2 for i in range(1, 6)]
print(squares)
```

## 推导式的基本格式

```
新列表 = [表达式 for 变量 in 可迭代对象]
```

就像把 for 循环"压缩"成了一行：

```python demo title="更多推导式例子"
# 把名字都转大写
names = ["anan", "xiaoming", "xiaohong"]
big_names = [name.upper() for name in names]
print(big_names)

# 生成 1-10 的偶数
evens = [i for i in range(2, 11, 2)]
print(evens)

# 每个数字乘 3
nums = [1, 2, 3, 4, 5]
tripled = [n * 3 for n in nums]
print(tripled)
```

## 带条件过滤

还可以加 `if` 条件，只保留满足条件的元素：

```
新列表 = [表达式 for 变量 in 可迭代对象 if 条件]
```

```python demo title="过滤偶数"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 只要偶数
evens = [n for n in numbers if n % 2 == 0]
print("偶数：", evens)

# 只要大于5的数
big = [n for n in numbers if n > 5]
print("大于5：", big)

# 只要包含字母 'a' 的名字
names = ["Anan", "Bob", "Alice", "Tom", "Anna"]
has_a = [name for name in names if 'a' in name.lower()]
print("含 a 的名字：", has_a)
```

## 练习

```python exercise title="用推导式改造代码"
# 把下面的 for 循环改写成列表推导式

# 1. 生成 1-20 中所有 3 的倍数
multiples_of_3 = [i for i in range(1, 21) if i % 3 == 0]
print("3的倍数：", multiples_of_3)

# 2. 把成绩列表中不及格的找出来
scores = [85, 42, 91, 55, 78, 33, 96, 60]
failed = [s for s in scores if s < 60]
print("不及格：", failed)

# 3. 把每个单词变成首字母大写
words = ["hello", "world", "python", "is", "fun"]
capitalized = [w.capitalize() for w in words]
print("首字母大写：", capitalized)
```
