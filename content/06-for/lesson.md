# 第6课：for 循环与 range()

## for 循环更简洁

上节课的 while 循环要自己管理计数变量，`for` + `range()` 帮你搞定：

```python demo title="for 循环数数"
for i in range(1, 6):
    print(i)
```

`range(1, 6)` 产生 1, 2, 3, 4, 5（不包含6）。

## range() 三种写法

```python demo title="range() 用法"
# range(stop)：从 0 开始
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
for i in range(1, 6):
    print(i, end=" ")
print()

# range(start, stop, step)：步长
for i in range(0, 11, 2):
    print(i, end=" ")
print()
```

## 嵌套循环：九九乘法表

```python demo title="九九乘法表（部分）"
for i in range(1, 4):      # 只打印前3行试试
    for j in range(1, 10):
        print(i, "×", j, "=", i*j, "\t", end="")
    print()
```

## 遍历字符串

```python demo title="逐字打印"
name = "Anan"
for char in name:
    print(char)
```

## 练习

```python exercise title="打印星星三角形"
# 目标：
# *
# **
# ***
# ****
# *****

rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```
