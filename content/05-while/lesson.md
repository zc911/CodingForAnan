# 第5课：while 循环

## 重复做同一件事

如果要打印 1 到 5，不必写 5 行代码：

```python demo title="从1数到5"
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("数完了！")
```

## while 的结构

```
while 条件:
    重复执行的代码（记得改变变量，否则会死循环！）
```

每次循环结束后，Python 回头检查条件：True 继续，False 退出。

## 倒计时

```python demo title="火箭倒计时 🚀"
n = 5
while n > 0:
    print(n, "...")
    n = n - 1
print("🚀 发射！")
```

## 累加求和

```python demo title="1 加到 100"
total = 0
i = 1
while i <= 100:
    total = total + i
    i = i + 1
print("1+2+...+100 =", total)
```

## 练习

```python exercise title="累加到 N"
# 计算 1+2+3+...+N 的和
N = 10   # 改成其他数字试试

total = 0
i = 1
while i <= N:
    total = total + i
    i = i + 1

print("1 + 2 + ... +", N, "=", total)
```
