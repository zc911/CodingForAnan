# 第10课：字符串操作

## 字符串是字符的列表

字符串里的每个字符都有下标，可以用 `[]` 取出：

```python demo title="访问字符"
name = "Anan"
print(name[0])       # 'A'
print(name[-1])      # 'n'（最后一个）
print(name[1:3])     # 'na'（切片）
print(len(name))     # 4
```

> 🖥️ **计算机小知识**
>
> `len("你好")` 是 2，但你知道文件里存"你好"占了几个字节吗？答案是 6！
>
> 最早只有英文字符的编码叫 **ASCII**，每个字符 1 个字节，只能表示 256 种字符。但全世界有中文、日文、阿拉伯文……ASCII 完全不够用！
>
> 于是有了 **Unicode**——给全世界每个字符一个唯一的编号。"你"的编号是 20320，"好"是 22909。**UTF-8** 是 Unicode 最常用的存储方式：英文 1 字节，中文 3 字节，emoji 4 字节。所以 🎉 占的空间比 A 多四倍！

## 常用字符串方法

```python demo title="字符串方法"
s = "  Hello, Python!  "

print(s.upper())          # 全大写
print(s.lower())          # 全小写
print(s.strip())          # 去掉两端空格
print(s.replace("Python", "Anan"))  # 替换
print(s.count("l"))       # 统计'l'出现次数
print("Hello" in s)       # 检查是否包含
```

## f-string：更方便的格式化

```python demo title="f-string 格式化"
name = "Anan"
age = 9
score = 95.5

print(f"我叫{name}，今年{age}岁，得了{score}分")
print(f"明年我{age + 1}岁")
```

## 练习

```python exercise title="文字小游戏"
word = "Python"

# 1. 倒着打印
print(word[::-1])

# 2. 统计元音字母数量
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"'{word}' 里有 {count} 个元音字母")

# 3. 判断回文
test = "racecar"
if test == test[::-1]:
    print(f"'{test}' 是回文！")
else:
    print(f"'{test}' 不是回文")
```
