# 第16课练习：算法思维

# 练习1：自己实现 min()
def my_min(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

# 练习2：统计列表中某个值出现的次数
def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

# 测试
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("列表：", data)
print("最小值：", my_min(data))
print("5 出现了", count_occurrences(data, 5), "次")

# Python 排序 vs 自己的冒泡排序
import time

big_list = list(range(1000, 0, -1))  # 1000到1倒序

start = time.time()
sorted(big_list)
print(f"Python 内置排序用时：{time.time()-start:.6f} 秒")
