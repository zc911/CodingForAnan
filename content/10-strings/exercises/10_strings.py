# 第10课练习：字符串操作

name = input("输入你的名字（英文）：")

print(f"正着：{name}")
print(f"倒着：{name[::-1]}")
print(f"大写：{name.upper()}")
print(f"长度：{len(name)} 个字母")

# 统计元音
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in name if c in vowels)
print(f"元音字母数：{vowel_count}")

# 回文判断
if name.lower() == name.lower()[::-1]:
    print(f"哇！'{name}' 是回文名字！")
