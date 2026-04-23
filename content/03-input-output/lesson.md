# 第3课：输入与输出

## 让程序问问题

`input()` 让程序暂停，等你输入文字，然后把你输入的内容返回回来。

> **提示：** 点击运行后，程序会在 `input()` 处暂停，弹出输入框等你打字，按回车继续——和在 Thonny 里运行一样！

```python demo title="问名字"
name = input("你叫什么名字？")
print("你好，" + name + "！欢迎来学 Python！")
```

## input() 总是返回字符串

不管你输入数字还是文字，`input()` 拿到的**永远是字符串**。要做数学就需要转换：

```python demo title="把输入转成数字"
age_text = input("你几岁了？")
age = int(age_text)
next_year = age + 1
print("明年你", next_year, "岁！")
```

常用转换：`int("9")` → 整数 9，`float("1.5")` → 小数 1.5

> 🖥️ **计算机小知识**
>
> 所有的程序，不管多复杂，都在做同一件事：**输入 → 处理 → 输出**，这叫 **IPO 模型**。
>
> - 微信：你打字（输入）→ 服务器转发（处理）→ 朋友看到消息（输出）
> - 计算器：你按数字（输入）→ CPU 算结果（处理）→ 屏幕显示答案（输出）
> - 游戏：你按手柄（输入）→ 游戏引擎算画面（处理）→ 电视显示画面（输出）
>
> `input()` 就是输入，`print()` 就是输出，中间的代码就是处理。你已经掌握了所有程序的核心套路！

## 自我介绍生成器

```python demo title="自我介绍生成器"
name = input("你的名字：")
age = int(input("你的年龄："))
hobby = input("你的爱好：")

print("大家好！我叫" + name + "，")
print("今年", age, "岁，")
print("我喜欢" + hobby + "。")
```

## 练习

```python exercise title="自我介绍小程序"
name = input("你叫什么名字？")
age = int(input("你今年几岁？"))
hobby = input("你有什么爱好？")
food = input("你最喜欢吃什么？")

print()
print("===== 自我介绍 =====")
print("大家好！我叫", name + "。")
print("我今年", age, "岁。")
print("我喜欢", hobby + "。")
print("我最喜欢吃", food + "。")
print("很高兴认识大家！")
```
