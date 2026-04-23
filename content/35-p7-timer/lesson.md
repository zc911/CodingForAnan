# 第35课：✨ 项目七：魔法计时器

## 这个项目做什么？

上节课学了装饰器，现在用装饰器做一个**实用工具箱**！每个装饰器给函数加一种超能力：

- ⏱️ @timer — 测量函数执行时间
- 🔄 @retry — 出错自动重试
- 📝 @log — 记录函数调用日志

## @timer：测量执行时间

```python thonny title="@timer 装饰器"
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱️ {func.__name__} 用了 {elapsed:.4f} 秒")
        return result
    return wrapper

@timer
def slow_count(n):
    """数到 n，每数一个稍等一下"""
    for i in range(n):
        time.sleep(0.01)
    return f"数完了 {n}！"

result = slow_count(10)
print(result)

@timer
def fast_math():
    return sum(range(1000000))

fast_math()
```

## @retry：出错自动重试

```python thonny title="@retry 装饰器"
import time
import random
from functools import wraps

def retry(max_attempts=3, delay=0.5):
    """出错时自动重试"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"❌ 第{attempt}次失败：{e}")
                    if attempt < max_attempts:
                        print(f"   ⏳ {delay}秒后重试...")
                        time.sleep(delay)
                    else:
                        print(f"💥 全部 {max_attempts} 次都失败了！")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.2)
def unstable_network():
    """模拟不稳定的网络请求（50%概率失败）"""
    if random.random() < 0.5:
        raise ConnectionError("网络连接失败")
    return "✅ 数据获取成功！"

# 试试看好不好运
try:
    result = unstable_network()
    print(result)
except ConnectionError:
    print("最终失败")
```

## @log：记录调用日志

```python thonny title="@log 装饰器"
from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%H:%M:%S")
        args_str = ", ".join(str(a) for a in args)
        print(f"[{timestamp}] 📞 调用 {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] 📤 返回 {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

add(3, 7)
print()
greet("Anan")
print()
greet("Anan", greeting="早上好")
```

## 组合使用：装饰器叠叠乐

多个装饰器可以叠在一起，**从下往上**执行：

```python thonny title="装饰器叠加"
@timer
@log
@retry(max_attempts=3, delay=0.1)
def dice_game():
    """掷骰子，掷到6才算赢"""
    import random
    result = random.randint(1, 6)
    if result != 6:
        raise ValueError(f"掷到了 {result}，不是6！")
    return f"🎉 掷到了 {result}！"

try:
    print(dice_game())
except ValueError as e:
    print(f"最终结果：{e}")
```

## 扩展挑战

- 🚦 **@rate_limit(seconds)**：限制函数每 N 秒只能调用一次
- 📊 **@count_calls**：统计函数被调用了多少次
- 🔒 **@require_auth**：模拟权限检查，只有管理员才能调用

```python thonny title="扩展挑战提示"
from functools import wraps

def count_calls(func):
    """统计函数被调用了多少次"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"📊 {func.__name__} 已被调用 {wrapper.calls} 次")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def hello():
    print("你好！")

hello()
hello()
hello()
print(f"总共调用了 {hello.calls} 次")
```
