# 第34课：装饰器：给函数穿新衣服

## 函数是一等公民

在 Python 里，函数和数字、字符串一样，可以**当参数传递**，也可以**当返回值**：

```python thonny title="函数当参数"
def say_hello(name):
    return f"你好，{name}！"

def say_bye(name):
    return f"再见，{name}！"

def greet(func, name):
    """接收一个函数作为参数"""
    print(func(name))

greet(say_hello, "Anan")
greet(say_bye, "Anan")
```

```python thonny title="函数当返回值"
def make_multiplier(n):
    """返回一个新函数"""
    def multiply(x):
        return x * n
    return multiply

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))   # 30
print(times_5(10))   # 50
```

> 🖥️ **计算机小知识**
>
> 把函数当变量传来传去，这不只是 Python 的花招——这是一种编程思想，叫**函数式编程**。
>
> 函数式编程的核心：函数像数据一样可以被创建、传递、组合。LISP（1958年）是第一个函数式语言，比 Python 早了30多年！Python 从函数式编程借鉴了很多好东西：`map()`、`filter()`、`lambda`、装饰器……
>
> 不同的编程思想像不同的工具：过程式 = 按步骤来，面向对象 = 分角色来，函数式 = 组合小函数来。高手会根据问题选择最合适的工具。

## 手写第一个装饰器

装饰器 = 接收一个函数，返回一个**增强版**函数：

```python thonny title="第一个装饰器"
def my_decorator(func):
    def wrapper():
        print("✨ 函数执行前")
        func()
        print("✨ 函数执行后")
    return wrapper

def say_hi():
    print("你好！")

# 手动装饰
say_hi = my_decorator(say_hi)
say_hi()
```

用 `@` 语法更优雅——效果完全一样：

```python thonny title="@ 语法糖"
def my_decorator(func):
    def wrapper():
        print("✨ 函数执行前")
        func()
        print("✨ 函数执行后")
    return wrapper

@my_decorator       # 等于 say_hi = my_decorator(say_hi)
def say_hi():
    print("你好！")

say_hi()
```

## 装饰带参数的函数

```python thonny title="装饰带参数的函数"
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} 耗时 {end-start:.4f} 秒")
        return result
    return wrapper

@timer
def slow_add(a, b):
    import time
    time.sleep(0.1)
    return a + b

result = slow_add(3, 7)
print(f"结果：{result}")
```

## 带参数的装饰器

如果装饰器自己也要接收参数，就多包一层：

```python thonny title="带参数的装饰器"
def repeat(n):
    """让函数执行 n 次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)
    return msg

say("你好！")
```

## functools.wraps

装饰器会把原函数的名字和文档覆盖掉。用 `@wraps` 修复：

```python thonny title="用 wraps 保留原函数信息"
from functools import wraps

def my_decorator(func):
    @wraps(func)           # 保留 func 的名字和文档
    def wrapper(*args, **kwargs):
        """我是 wrapper"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """打招呼的函数"""
    return f"你好，{name}！"

print(greet("Anan"))
print("函数名：", greet.__name__)       # greet（不是 wrapper）
print("文档：", greet.__doc__)           # 打招呼的函数
```

## 练习

```python thonny title="写一个 @debug 装饰器"
from functools import wraps

def debug(func):
    """打印函数调用的参数和返回值"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        print(f"🔍 调用 {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"🔍 返回 {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

add(3, 7)
print("---")
factorial(5)
```
