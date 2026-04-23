# 第37课：命令行参数：让程序接受指令

## 从终端运行程序

之前你都在 Thonny 里点运行按钮。但真正的程序是在**终端**里运行的：

```
python my_program.py
```

如果程序能接收指令呢？比如：

```
python quiz.py --mode easy --count 5
```

这就是**命令行参数**！

## sys.argv：最原始的方式

```python thonny title="sys.argv"
import sys

# sys.argv 是一个列表，包含所有命令行参数
# sys.argv[0] 是程序名本身
# 在 Thonny 里运行，argv 只有程序名
print("所有参数：", sys.argv)
print("程序名：", sys.argv[0])
print("参数个数：", len(sys.argv))

# 如果有额外参数
if len(sys.argv) > 1:
    print("第一个参数：", sys.argv[1])
```

> 🖥️ **计算机小知识**
>
> 当你在终端输入命令时，是谁在听你说话？是 **Shell**！
>
> Shell 是操作系统和用户之间的翻译官。你输入 `python quiz.py`，Shell 会：
> 1. 找到 `python` 程序的位置
> 2. 启动一个新**进程**来运行它
> 3. 把 `quiz.py` 作为参数传给 Python
>
> 常见的 Shell：Windows 用 CMD/PowerShell，Mac 用 zsh，Linux 用 bash。**环境变量**（如 `PATH`）告诉 Shell 去哪里找程序——输入 `python` 时，Shell 就按 `PATH` 里的目录逐个搜索。

## argparse：参数解析神器

`sys.argv` 太原始了。`argparse` 能自动处理参数、生成帮助信息：

```python thonny title="argparse 基础"
import argparse

parser = argparse.ArgumentParser(description="一个简单的问候程序")

# 添加位置参数（必须提供）
parser.add_argument("name", help="你的名字")

# 添加可选参数（有 -- 前缀）
parser.add_argument("--times", type=int, default=1, help="问候次数")
parser.add_argument("--loud", action="store_true", help="大写输出")

# 在 Thonny 里模拟命令行参数
import sys
sys.argv = ["greet.py", "Anan", "--times", "3", "--loud"]

args = parser.parse_args()

for _ in range(args.times):
    message = f"你好，{args.name}！"
    if args.loud:
        message = message.upper()
    print(message)
```

## 位置参数、可选参数、默认值

```python thonny title="各种参数类型"
import argparse
import sys

parser = argparse.ArgumentParser(description="计算器")

# 位置参数：必须按顺序提供
parser.add_argument("x", type=float, help="第一个数")
parser.add_argument("y", type=float, help="第二个数")

# 可选参数：有默认值
parser.add_argument("--op", default="add", choices=["add", "sub", "mul", "div"],
                    help="运算类型")

# 开关参数：有/没有，不需要值
parser.add_argument("--verbose", action="store_true", help="显示详细信息")

# 模拟命令行
sys.argv = ["calc.py", "10", "3", "--op", "mul", "--verbose"]

args = parser.parse_args()

if args.op == "add":
    result = args.x + args.y
elif args.op == "sub":
    result = args.x - args.y
elif args.op == "mul":
    result = args.x * args.y
elif args.op == "div":
    result = args.x / args.y

if args.verbose:
    print(f"{args.x} {args.op} {args.y} = {result}")
else:
    print(result)
```

## 子命令：像 git 一样

```python thonny title="子命令"
import argparse
import sys

parser = argparse.ArgumentParser(description="笔记本管理器")
subparsers = parser.add_subparsers(dest="command")

# add 子命令
add_parser = subparsers.add_parser("add", help="添加笔记")
add_parser.add_argument("text", help="笔记内容")

# list 子命令
list_parser = subparsers.add_parser("list", help="列出笔记")
list_parser.add_argument("--limit", type=int, default=5, help="显示数量")

# search 子命令
search_parser = subparsers.add_parser("search", help="搜索笔记")
search_parser.add_argument("keyword", help="搜索关键词")

# 模拟
sys.argv = ["notes.py", "add", "今天学了argparse"]

args = parser.parse_args()

if args.command == "add":
    print(f"📝 添加笔记：{args.text}")
elif args.command == "list":
    print(f"📋 显示最近 {args.limit} 条笔记")
elif args.command == "search":
    print(f"🔍 搜索：{args.keyword}")
```

## 练习

```python thonny title="命令行计算器"
import argparse
import sys

parser = argparse.ArgumentParser(description="简单计算器")
parser.add_argument("x", type=float, help="第一个数")
parser.add_argument("op", choices=["+", "-", "*", "/"], help="运算符")
parser.add_argument("y", type=float, help="第二个数")
parser.add_argument("--verbose", action="store_true", help="显示过程")

# 试试不同的 sys.argv
sys.argv = ["calc.py", "15", "*", "7", "--verbose"]

args = parser.parse_args()

# 请补充运算逻辑
if args.op == "+":
    result = ___
elif args.op == "-":
    result = ___
elif args.op == "*":
    result = ___
elif args.op == "/":
    result = ___

if args.verbose:
    print(f"{args.x} {args.op} {args.y} = {result}")
else:
    print(result)
```
