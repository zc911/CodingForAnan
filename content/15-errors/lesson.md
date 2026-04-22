# 第15课：错误处理：try / except

## 程序出错时

如果用户输入了不是数字的内容，`int()` 会报错，程序崩溃：

```python demo title="会崩溃的程序"
age = int(input("输入年龄："))   # 如果输入 "abc" 就会崩溃
print("你", age, "岁")
```

## try / except 救场

```python demo title="优雅处理错误"
try:
    age = int(input("输入年龄："))
    print("你", age, "岁")
except ValueError:
    print("❌ 请输入数字！")
```

`try` 里放可能出错的代码，`except` 里放出错后的处理。

## 常见错误类型

| 错误 | 原因 |
|------|------|
| `ValueError` | 类型转换失败（如 `int("abc")`） |
| `FileNotFoundError` | 文件不存在 |
| `IndexError` | 列表下标超出范围 |
| `KeyError` | 字典中找不到键 |
| `ZeroDivisionError` | 除以零 |

```python demo title="处理多种错误"
numbers = [10, 20, 30]

try:
    index = int(input("输入下标（0-2）："))
    result = 100 / numbers[index]
    print("结果：", result)
except ValueError:
    print("❌ 请输入整数")
except IndexError:
    print("❌ 下标超出范围（只有0、1、2）")
except ZeroDivisionError:
    print("❌ 不能除以零")
```

## 练习

```python exercise title="安全的输入函数"
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 请输入整数，重试：")

age = safe_int_input("输入你的年龄：")
print("你", age, "岁")
```
