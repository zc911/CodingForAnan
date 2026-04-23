# 第36课：自定义异常：设计你自己的报错

## 回顾：try/except 完整语法

```python thonny title="try/except/else/finally"
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ 不能除以0！")
        return None
    else:
        print("✅ 计算成功！")
        return result
    finally:
        print("📌 无论如何都会执行")

print(divide(10, 3))
print("---")
print(divide(10, 0))
```

> 🖥️ **计算机小知识**
>
> 当程序出错时，Python 会从出错的那个函数开始，沿着**调用栈**一层层往上抛异常。
>
> 想象你请朋友A帮忙，A又请B帮忙，B又请C帮忙。如果C出了问题，C会告诉B，B告诉A，A告诉你。每个人都可以选择"处理"或者"继续往上抛"。
>
> `traceback` 那一长串错误信息，就是异常在调用栈中旅行的路径！`except` 就像在某一层放了个"拦截网"，把异常拦住处理掉。

## raise：主动抛出异常

```python thonny title="raise 主动报错"
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数！")
    if age < 0 or age > 150:
        raise ValueError(f"年龄 {age} 不合理！应该在 0-150 之间")
    print(f"✅ 年龄设置为 {age}")

set_age(9)
try:
    set_age(-5)
except ValueError as e:
    print(f"捕获到错误：{e}")

try:
    set_age("九")
except TypeError as e:
    print(f"捕获到错误：{e}")
```

## 自定义异常类

Python 内置的异常类型不够用时，自己定义！只需继承 `Exception`：

```python thonny title="自定义异常"
class DiaryError(Exception):
    """日记本相关的所有错误"""
    pass

class DiaryNotFoundError(DiaryError):
    """日记不存在"""
    def __init__(self, date):
        self.date = date
        super().__init__(f"📅 {date} 的日记不存在")

class DiaryEmptyError(DiaryError):
    """日记内容为空"""
    def __init__(self, date):
        self.date = date
        super().__init__(f"📝 {date} 的日记是空的")

# 使用自定义异常
def read_diary(date, content):
    if content is None:
        raise DiaryNotFoundError(date)
    if len(content.strip()) == 0:
        raise DiaryEmptyError(date)
    print(f"📖 {date}：{content}")

try:
    read_diary("2026-04-20", None)
except DiaryNotFoundError as e:
    print(f"错误：{e}")

try:
    read_diary("2026-04-21", "   ")
except DiaryError as e:
    print(f"日记错误：{e}")
```

## 异常链：raise ... from ...

有时候你捕获了一个异常，想换成自己的类型，但保留原始原因：

```python thonny title="异常链"
class ConfigError(Exception):
    """配置文件错误"""
    pass

def load_config():
    try:
        with open("不存在的文件.txt") as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigError("配置文件找不到") from e

try:
    load_config()
except ConfigError as e:
    print(f"自定义错误：{e}")
    print(f"原始原因：{e.__cause__}")
```

## 练习

```python thonny title="为日记本设计异常体系"
class DiaryError(Exception):
    """日记本基础异常"""
    pass

class DiaryNotFoundError(DiaryError):
    def __init__(self, date):
        super().__init__(f"📅 {date} 的日记不存在")

class DiaryEmptyError(DiaryError):
    def __init__(self, date):
        super().__init__(f"📝 {date} 的日记是空的")

class DiaryWriteError(DiaryError):
    def __init__(self, date, reason):
        super().__init__(f"✍️ 无法写入 {date} 的日记：{reason}")

def safe_write_diary(date, content):
    """安全的日记写入函数"""
    if not content or len(content.strip()) == 0:
        raise DiaryEmptyError(date)
    try:
        with open(f"diary_{date}.txt", "w") as f:
            f.write(content)
    except OSError as e:
        raise DiaryWriteError(date, str(e)) from e
    print(f"✅ {date} 的日记已保存")

# 测试
try:
    safe_write_diary("2026-04-23", "")
except DiaryError as e:
    print(f"操作失败：{e}")
```
