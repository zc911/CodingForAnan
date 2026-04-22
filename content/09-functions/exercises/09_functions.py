# 第9课练习：函数

def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

# 测试
print("0°C =", celsius_to_fahrenheit(0), "°F")
print("100°C =", celsius_to_fahrenheit(100), "°F")
print("98.6°F =", round(fahrenheit_to_celsius(98.6), 1), "°C")

# 挑战：写一个函数，判断一个数是不是质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(2, 20):
    if is_prime(num):
        print(num, "是质数")
