# 第16课：算法思维：排序与查找

## 什么是算法？

**算法**就是解决问题的步骤清单。就像做蛋炒饭的菜谱，一步一步来。

## 线性查找

在列表里找一个数——从头开始一个个看：

```python demo title="线性查找"
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i    # 找到了，返回下标
    return -1           # 没找到

numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]
result = linear_search(numbers, 9)
print(f"找到 9，在第 {result} 个位置（下标从0开始）")
print(f"查找了 {numbers.index(9) + 1} 次")
```

## 冒泡排序

像泡泡从水底浮上来一样，大的数逐渐"浮"到后面：

```python demo title="冒泡排序（带步骤展示）"
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
print("排序前：", data)
sorted_data = bubble_sort(data.copy())
print("排序后：", sorted_data)
```

## Python 内置排序（更厉害的算法）

```python demo title="Python 内置 sort"
data = [5, 3, 8, 1, 9, 2]
data.sort()
print("从小到大：", data)
data.sort(reverse=True)
print("从大到小：", data)
```

## 算法的效率

查找10个数：最多看10次。查找100个数：最多看100次。这叫 **O(n)**。

好的算法能大大减少步骤。这就是为什么程序员要学算法！

## 练习

```python exercise title="找最大值（不用 max()）"
def my_max(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num
    return biggest

numbers = [3, 7, 1, 9, 4, 6, 2]
print("最大值：", my_max(numbers))
print("验证：", max(numbers))
```
