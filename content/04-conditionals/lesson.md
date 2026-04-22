# 第4课：条件判断：if / elif / else

## 程序也要做选择

如果下雨就带伞，不下雨就不带——Python 也能做这种判断：

```python demo title="第一个 if 语句"
weather = "下雨"

if weather == "下雨":
    print("记得带伞！☂️")
else:
    print("今天天气不错！☀️")
```

**注意：** `==` 是"等于"（判断），`=` 是"赋值"（存值）！

## if 语句结构

```
if 条件:
    条件为真时执行（要缩进4个空格！）
elif 另一个条件:
    第二个条件为真时执行
else:
    以上都不满足时执行
```

## 比较运算符

| 符号 | 意思 | 例子 |
|------|------|------|
| `==` | 等于 | `age == 9` |
| `!=` | 不等于 | `age != 10` |
| `>` | 大于 | `score > 60` |
| `<` | 小于 | `score < 60` |
| `>=` | 大于等于 | `score >= 90` |
| `<=` | 小于等于 | `score <= 100` |

```python demo title="成绩等级判断"
score = 85

if score >= 90:
    print("优秀！🌟")
elif score >= 80:
    print("良好！👍")
elif score >= 60:
    print("及格 📚")
else:
    print("需要加油 💪")
```

试试把 `score` 改成不同数字！

## 练习

```python exercise title="奇数还是偶数？"
# % 是取余数运算符：8 % 2 = 0，7 % 2 = 1
number = 7

if number % 2 == 0:
    print(number, "是偶数")
else:
    print(number, "是奇数")
```
