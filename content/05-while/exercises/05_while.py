# 第5课练习：while 循环

# 练习1：倒计时
n = int(input("从几开始倒计时？"))
while n > 0:
    print(n, "...")
    n = n - 1
print("时间到！⏰")

# 练习2：求 1 到 N 的和
N = int(input("计算 1 加到几？"))
total = 0
i = 1
while i <= N:
    total += i
    i += 1
print("结果：", total)
