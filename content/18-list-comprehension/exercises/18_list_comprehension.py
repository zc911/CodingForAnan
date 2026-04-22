# 第18课练习：列表推导式

# 1. 生成 1-50 中所有能被 7 整除的数
div7 = [i for i in range(1, 51) if i % 7 == 0]
print("7的倍数：", div7)

# 2. 把字符串列表的每个元素加上序号
fruits = ["苹果", "香蕉", "草莓", "西瓜"]
numbered = [f"{i+1}. {fruit}" for i, fruit in enumerate(fruits)]
print("编号水果：", numbered)

# 挑战：用推导式生成九九乘法表（二维列表）
table = [[f"{i}×{j}={i*j}" for j in range(1, 10)] for i in range(1, 10)]
for row in table:
    print("  ".join(row))
