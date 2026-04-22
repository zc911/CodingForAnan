# 第8课练习：列表

# 创建一个存放你喜欢的5种食物的列表
foods = ["___", "___", "___", "___", "___"]

print("我喜欢的食物：")
for food in foods:
    print("-", food)

print("共", len(foods), "种")
print("第一种：", foods[0])
print("最后一种：", foods[-1])

# 再加一种
foods.append("___")
print("加了一种后：", foods)
