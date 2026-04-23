# 第9课：函数（def）

## 为什么需要函数？

如果你要在程序里好几处打印欢迎语，不用每次都写一遍：

```python demo title="定义并调用函数"
def greet(name):
    print("你好，" + name + "！欢迎来学 Python！")

greet("Anan")
greet("小明")
greet("小红")
```

函数用 `def` 定义，括号里是**参数**（接收外部传入的值）。

> 🖥️ **计算机小知识**
>
> 当你调用一个函数时，内存里发生了什么？想象一叠盘子：
>
> - 每调用一个函数，就在上面放一个新盘子（叫**栈帧**），里面存着这个函数的参数和变量
> - 函数执行完，就把这个盘子拿走，回到下面那个盘子继续
> - 这叠盘子就叫**调用栈（Call Stack）**
>
> 如果函数 A 调用函数 B，函数 B 调用函数 C，栈就有三个盘子。C 执行完 → B 执行完 → 回到 A。层层返回，一个都不会乱！

## 有返回值的函数

```python demo title="计算面积"
def area(length, width):
    result = length * width
    return result

room = area(4, 5)
print("房间面积：", room, "平方米")
print("桌子面积：", area(1.2, 0.6), "平方米")
```

`return` 把计算结果"返回"给调用者。

## 函数让代码更清晰

```python demo title="判断成绩等级（用函数）"
def grade(score):
    if score >= 90:
        return "优秀 🌟"
    elif score >= 80:
        return "良好 👍"
    elif score >= 60:
        return "及格 📚"
    else:
        return "加油 💪"

for s in [95, 82, 67, 45]:
    print(s, "分 →", grade(s))
```

## 练习

```python exercise title="温度转换函数"
def celsius_to_fahrenheit(c):
    # 公式：°F = °C × 1.8 + 32
    f = c * 1.8 + 32
    return f

print(celsius_to_fahrenheit(0))    # 应该输出 32.0
print(celsius_to_fahrenheit(100))  # 应该输出 212.0
print(celsius_to_fahrenheit(37))   # 体温
```
