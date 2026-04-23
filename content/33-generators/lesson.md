# 第33课：生成器：要一个给一个的魔法

## for 循环背后发生了什么？

`for x in [1, 2, 3]` 看起来简单，但 Python 在背后做了什么？

```python thonny title="手动迭代"
nums = [1, 2, 3]
it = iter(nums)          # 获取迭代器
print(next(it))          # 1
print(next(it))          # 2
print(next(it))          # 3
# print(next(it))        # ❌ StopIteration！
```

`iter()` 把列表变成**迭代器**，`next()` 每次取一个值。`for` 循环其实就是不断调用 `next()`，直到 `StopIteration`。

## yield：让函数暂停的魔法

普通函数 `return` 一次就结束了。`yield` 让函数**暂停**，下次调用时**继续**：

```python thonny title="第一个生成器"
def count_up(max_num):
    n = 1
    while n <= max_num:
        yield n        # 暂停，把 n 交出去
        n += 1         # 下次从这里继续

for num in count_up(5):
    print(num, end=" ")
print()

# 生成器是一个迭代器
g = count_up(3)
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```

> 🖥️ **计算机小知识**
>
> 内存就像一张书桌，空间有限。如果你要处理 1 亿个数字，全部放进列表，电脑可能直接卡死！
>
> 生成器的聪明之处：不把所有数据一次性放进内存，而是**要一个算一个**。就像你吃自助餐，不用把所有菜端到桌上——吃完一盘再去拿下一盘。
>
> 这就是**内存层级**的重要性：CPU 缓存最快（但最小）→ 内存很快 → 硬盘最慢（但最大）。省内存 = 让程序跑得更快更稳！

## 生成器表达式

列表推导式用 `[]`，生成器表达式用 `()`——同样的事，但不占内存：

```python thonny title="生成器表达式 vs 列表推导式"
import sys

# 列表推导式：一次性生成所有数据
nums_list = [x * x for x in range(1000)]
print("列表大小：", sys.getsizeof(nums_list), "字节")

# 生成器表达式：按需生成
nums_gen = (x * x for x in range(1000))
print("生成器大小：", sys.getsizeof(nums_gen), "字节")

# 生成器用起来和列表一样
for i, val in enumerate(nums_gen):
    if i >= 5:
        break
    print(val, end=" ")
print("... (只算了需要的几个)")
```

## itertools：生成器的好帮手

```python thonny title="itertools 常用工具"
from itertools import count, cycle, chain, islice

# count：无限计数器
for i in islice(count(1), 5):    # 取前5个
    print(i, end=" ")
print()

# cycle：无限循环
colors = cycle(["🔴", "🔵", "🟢"])
for _ in range(6):
    print(next(colors), end=" ")
print()

# chain：把多个可迭代对象连起来
a = [1, 2, 3]
b = ["x", "y"]
print(list(chain(a, b)))
```

## 练习

```python thonny title="无限斐波那契生成器"
def fibonacci():
    """无限斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 打印前 15 个斐波那契数
for i, num in enumerate(fibonacci()):
    if i >= 15:
        break
    print(f"F({i}) = {num}")
```
