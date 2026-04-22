# 第2课：变量和数据类型

## 什么是变量？

想象你有很多盒子，每个盒子贴了标签。你可以把东西放进去，也可以换成别的东西。

在 Python 里，**变量**就是这些盒子。`=` 号表示"把右边的值放进左边的变量"：

```python demo title="创建变量"
name = "Anan"
age = 9
height = 1.35

print(name)
print(age)
print(height)
```

## 四种基本数据类型

| 类型 | 英文 | 例子 | 说明 |
|------|------|------|------|
| 整数 | `int` | `9`, `100` | 没有小数点的数 |
| 小数 | `float` | `1.35`, `3.14` | 有小数点的数 |
| 文字 | `str` | `"Anan"` | 用引号包起来 |
| 真假 | `bool` | `True`, `False` | 只有这两个值 |

```python demo title="查看数据类型"
name = "Anan"
age = 9
height = 1.35
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

## 变量可以计算

```python demo title="用变量做数学"
age = 9
next_year = age + 1
print("明年我", next_year, "岁")

price = 3.5
count = 4
total = price * count
print("总价：", total, "元")
```

## 字符串拼接

用 `+` 把两段文字连在一起：

```python demo title="拼接字符串"
first_name = "An"
last_name = "an"
full_name = first_name + last_name
print("全名：" + full_name)
print("你好，" + full_name + "！")
```

## 练习

```python exercise title="关于我的变量"
# 创建下面这些变量，填入你自己的信息

name = "___"          # 你的名字（str）
age = ___             # 你的年龄（int）
height = ___          # 你的身高，单位米（float，如 1.35）
is_student = ___      # 你是不是学生？True 或 False

print("我叫", name)
print("我", age, "岁")
print("我的身高是", height, "米")
print("我是学生：", is_student)

# 计算10年后的年龄
future_age = age + 10
print("10年后我", future_age, "岁")
```
