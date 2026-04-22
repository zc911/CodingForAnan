# 第15课练习：错误处理

def safe_int_input(prompt):
    """一直问直到用户输入合法整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ 请输入整数，重试：")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "❌ 不能除以零"

# 测试
a = safe_int_input("输入被除数：")
b = safe_int_input("输入除数：")
print(f"{a} ÷ {b} = {safe_divide(a, b)}")
