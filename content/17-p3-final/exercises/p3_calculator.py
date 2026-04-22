# 项目三：智能计算器
history = []

def calculate(expr):
    try:
        result = eval(expr)
        history.append(f"{expr} = {result}")
        return result
    except ZeroDivisionError:
        return "❌ 不能除以零"
    except Exception:
        return "❌ 无效表达式"

print("=== 智能计算器 === （q退出，h历史）")
while True:
    expr = input("计算：").strip()
    if expr == "q": break
    elif expr == "h":
        for item in history: print(" ", item)
    else:
        print("=", calculate(expr))
