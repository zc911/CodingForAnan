# 第14课练习：文件读写
# 在 Thonny 里运行

# 1. 写入一个购物清单
items = []
print("输入购物清单（输入 q 结束）：")
while True:
    item = input("- ")
    if item.lower() == "q":
        break
    items.append(item)

with open("shopping.txt", "w", encoding="utf-8") as f:
    for item in items:
        f.write(item + "\n")
print("购物清单已保存到 shopping.txt！")

# 2. 读取并显示
print("\n购物清单内容：")
with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("✓", line.strip())
