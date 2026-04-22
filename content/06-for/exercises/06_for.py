# 第6课练习：for 循环

# 练习1：星星三角形
rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# 练习2：打印你名字的每个字母
name = input("输入你的名字（英文）：")
for char in name:
    print(char)

# 挑战：打印九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j}", end="\t")
    print()
