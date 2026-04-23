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

> 🖥️ **计算机小知识**
>
> 如果没有循环，编程会是什么样子？假设你要打印 1 到 100，就得写 100 行 `print()`！
>
> 早期的程序员真的这么干过。后来人们发明了**循环**这个概念，才让编程变得高效。几乎所有的编程语言都有循环——`for`、`while`、`do-while`……虽然写法不同，但核心思想一样：**告诉计算机"重复做这件事"**。
>
> 这就是**迭代**的思想——把一个大任务拆成重复的小步骤。不只在编程里，生活中也一样：读书是一页一页翻的，扫地是一块一块擦的。

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
