# 第30课：正则表达式：文字侦探的放大镜

## 比字符串查找更强大的武器

你已经学过 `"hello" in text` 来检查一段文字里有没有某个词。但如果要找"所有手机号"呢？手机号的规律是：1开头、11位数字——用 `in` 可做不了！

**正则表达式**（Regular Expression，简称 regex）就是描述"文字长什么样"的模式语言。

```python demo title="正则初体验"
import re

text = "我的手机号是 13812345678，电话是 010-12345678"
phones = re.findall(r"1\d{10}", text)
print("找到的手机号：", phones)
```

> 🖥️ **计算机小知识**
>
> 正则表达式的底层是一种叫**有限状态机**的计算模型。想象一个机器人沿着文字一个字符一个字符地走，每走一步根据当前字符决定"继续走"还是"找到了"——这就是状态机的工作方式。
>
> 有限状态机是计算机科学最基础的模型之一，不光正则表达式在用，电路设计、游戏AI、文本编辑器……到处都有它的身影。你写的每一个正则，背后都有一个状态机在跑！

## 基础语法：特殊字符

正则用**特殊字符**来描述模式：

| 符号 | 含义 | 例子 | 匹配 |
|------|------|------|------|
| `.` | 任意一个字符 | `a.c` | abc, a1c, a c |
| `\d` | 一个数字 | `\d\d` | 37, 99 |
| `\w` | 一个字母/数字/下划线 | `\w+` | hello_123 |
| `\s` | 一个空白（空格、换行） | `a\sb` | a b |
| `*` | 前面那个重复 0 次或更多 | `ab*c` | ac, abc, abbc |
| `+` | 前面那个重复 1 次或更多 | `ab+c` | abc, abbc |
| `?` | 前面那个出现 0 或 1 次 | `colou?r` | color, colour |

```python demo title="用特殊字符匹配"
import re

# \d+ 匹配连续数字
print(re.findall(r"\d+", "我今年9岁，身高132厘米"))

# \w+ 匹配连续字母数字
print(re.findall(r"\w+", "Hello, Python 3!"))

# a.*z 匹配 a 到 z 之间的所有内容
print(re.findall(r"a.*z", "abcdefghijklmnopqrstuvwxyz"))
```

## re 模块三大招

```python demo title="search、findall、sub"
import re

text = "苹果3个，香蕉5根，橘子8个"

# search：找到第一个匹配
m = re.search(r"\d+", text)
if m:
    print("第一个数字：", m.group())

# findall：找到所有匹配
print("所有数字：", re.findall(r"\d+", text))

# sub：替换匹配的部分
print(re.sub(r"\d+", "很多", text))
```

## 分组与或操作

用 `()` 分组，用 `|` 表示"或"：

```python demo title="分组与或操作"
import re

# 分组：提取年月日
date = "今天是 2026-04-23"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", date)
if m:
    print("年：", m.group(1))
    print("月：", m.group(2))
    print("日：", m.group(3))

# 或操作：匹配猫或狗
text = "我家有猫和狗"
print(re.findall(r"猫|狗", text))
```

## 练习

```python exercise title="提取邮箱和电话"
import re

text = """
联系我：anan@example.com 或 test123@qq.com
电话：13812345678，公司：010-87654321
"""

# 提示：邮箱模式 = 字母数字 + @ + 字母数字 + . + 字母
# 提示：手机号 = 1 开头 + 10 位数字

emails = re.findall(r"___", text)
print("邮箱：", emails)

phones = re.findall(r"___", text)
print("手机号：", phones)
```
