# 第8课：列表（list）

## 一个变量存多个值

之前每个变量只能存一个值。**列表**可以存很多个：

```python demo title="创建列表"
fruits = ["苹果", "香蕉", "草莓", "西瓜"]
print(fruits)
print(fruits[0])    # 第1个，下标从0开始
print(fruits[2])    # 第3个
print(len(fruits))  # 列表长度
```

> **注意：** 下标从 **0** 开始！第1个是 `[0]`，第2个是 `[1]`。

> 🖥️ **计算机小知识**
>
> 列表在内存里是怎么存的？想象一排连续的储物柜：
>
> ```
> 柜子编号:  0号   1号   2号   3号
> 里面存着: "苹果" "香蕉" "橘子" "葡萄"
> 内存地址: 100   101   102   103
> ```
>
> 这就是**数组**——数据一个挨一个排在连续的内存位置上。为什么 `fruits[0]` 这么快？因为 CPU 只要用"起始地址 + 下标"就能直接算出数据在哪，一步到位！
>
> 不过 Python 的列表比普通数组更聪明——它允许放不同类型的数据，但速度会稍慢一点点。

## 常用操作

```python demo title="列表操作"
scores = [85, 92, 78, 96, 88]

scores.append(100)        # 在末尾添加
print(scores)

scores.sort()             # 排序（从小到大）
print(scores)

print(max(scores))        # 最大值
print(min(scores))        # 最小值
print(sum(scores))        # 求和
```

## 用 for 遍历列表

```python demo title="遍历列表"
animals = ["🐶 狗", "🐱 猫", "🐰 兔", "🐼 熊猫"]
for animal in animals:
    print("我喜欢", animal)
```

## 练习

```python exercise title="我的购物清单"
shopping = ["苹果", "牛奶", "面包"]

# 1. 打印清单里的第一个和最后一个
print("第一个：", shopping[0])
print("最后一个：", shopping[-1])   # -1 表示最后一个

# 2. 添加"鸡蛋"到清单
shopping.append("鸡蛋")

# 3. 打印完整清单
print("完整清单：")
for item in shopping:
    print("-", item)
```
