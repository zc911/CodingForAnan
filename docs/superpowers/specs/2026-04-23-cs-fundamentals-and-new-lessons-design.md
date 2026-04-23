# Design: CS Fundamentals Integration + New Lessons 30-39

## Overview

Two changes to Anan's Python course:

1. **CS fundamentals穿插**: Add computer science theory boxes to 16 existing lessons (1-22) where the Python topic naturally connects to a CS concept.
2. **New lessons 30-39**: 10 new lessons covering advanced Python topics with embedded CS fundamentals, including 3 project lessons.

## CS Fundamentals in Existing Lessons (1-29)

Each addition uses a `> 🖥️ **计算机小知识**` blockquote block, placed after "what it is" and before "how to use deeply".

| Lesson | Python Topic | CS Fundamental Added | Placement |
|--------|-------------|---------------------|-----------|
| 1 | 认识Python | 计算机组成：CPU/内存/硬盘/输入输出 | After "what is Python", before first code |
| 2 | 变量和数据类型 | 二进制与数据表示 | After introducing types, before type conversion |
| 3 | 输入与输出 | IPO模型（输入→处理→输出） | After input/print, as a framing summary |
| 4 | 条件判断 | 布尔逻辑与逻辑门 | After boolean operators, before elif chains |
| 5 | while循环 | 指令周期：取指→译码→执行 | After while syntax, before infinite loops |
| 6 | for循环 | 迭代与计数的设计思想 | After for/range, before nested loops |
| 8 | 列表 | 数组和连续内存 | After list indexing, before list methods |
| 9 | 函数 | 调用栈（Call Stack） | After function definition, before return values |
| 10 | 字符串 | 字符编码：ASCII→Unicode→UTF-8 | After string basics, before string methods |
| 11 | 模块 | 编译与解释、标准库概念 | After import syntax, before specific modules |
| 13 | 字典 | 哈希表与哈希函数 | After dict syntax, before dict methods |
| 14 | 文件读写 | 文件系统与磁盘存储 | After open/write, before with statement |
| 15 | 错误处理 | 异常与中断 | After try/except, before specific exceptions |
| 19 | 面向对象基础 | 抽象与封装的设计哲学 | Before class definition, as motivation |
| 21 | JSON与API | 网络基础：IP/TCP/HTTP | Before requests call, explain what happens |
| 22 | 数据可视化 | 数据与信息 | Before matplotlib code, explain why visualize |

### CS Box Format

```markdown
> 🖥️ **计算机小知识**
>
> 你有没有想过……（引出一个问题）
>
> （用通俗语言解释底层原理，2-3段，配合类比和生活例子）
>
> 明白了这个，接下来学 ___ 就知道为什么是这样设计的了！
```

### Writing Guidelines for CS Boxes

- **Target audience**: 9-year-old with ~20 lessons of Python experience (adjust depth per lesson position)
- **Length**: 150-300 Chinese characters per box
- **Tone**: Conversational, curious, uses analogies (not academic)
- **No jargon without explanation**: Every technical term gets a one-line plain-language definition
- **Connect back to Python**: The box must end by linking the CS concept to the Python feature being learned
- **No exercises**: CS boxes are reading-only, no quiz or code challenge

## New Lessons (30-39)

### Lesson Structure

| # | Title | Python Topic | CS Fundamental | Type |
|---|-------|-------------|----------------|------|
| 30 | 正则表达式入门 | re模块：匹配、搜索、替换 | 自动机与模式匹配（有限状态机） | 新知 |
| 31 | 文件与目录操作 | os/pathlib/shutil：批量操作文件 | 操作系统：进程与文件描述符 | 新知 |
| 32 | 🗂️ 项目六：智能日记本 | 文件+正则+日期：可搜索日记 | — | 项目 |
| 33 | 生成器与迭代器 | yield、迭代协议、itertools | 内存层级与栈帧 | 新知 |
| 34 | 装饰器 | @语法、高阶函数、闭包 | 函数式编程范式 | 新知 |
| 35 | ✨ 项目七：魔法计时器 | 装饰器实现计时/重试/日志 | — | 项目 |
| 36 | 异常进阶与自定义异常 | raise、自定义Exception类、异常链 | 调用栈与错误传播深入 | 新知 |
| 37 | 命令行参数与argparse | argparse模块、子命令 | Shell与操作系统接口 | 新知 |
| 38 | 🧪 项目八：单词测验生成器 | argparse+文件+随机：自动出题 | — | 项目 |
| 39 | 🚀 项目九：自选终极大作 | 综合运用所有进阶技能 | — | 项目 |

### Content Format for New Lessons

Same format as existing lessons:
- Directory: `content/<num>-<slug>/`
- Files: `lesson.md` (content), `meta.txt` (title + summary)
- Code blocks: `python demo` (browser runnable), `python thonny` (download for Thonny)
- CS box format: same blockquote style as above

### Lesson 30: 正则表达式入门

- Slug: `30-regex`
- Title: 正则表达式：文字侦探的放大镜
- Summary: 用模式匹配搜索文字——像侦探一样精准找到你要的内容
- Content outline:
  1. 什么是正则？为什么需要比 `in` 更强大的匹配
  2. 🖥️ 计算机小知识：有限状态机——正则引擎的底层原理
  3. 基础语法：`.` `*` `+` `?` `\d` `\w` `\s`
  4. re模块：`re.search()` `re.findall()` `re.sub()`
  5. 分组与 `|` 或操作
  6. 练习：从文本中提取电话号码、邮箱

### Lesson 31: 文件与目录操作

- Slug: `31-file-ops`
- Title: 文件与目录操作：让Python帮你整理文件夹
- Summary: 批量重命名、自动归类文件——Python当你的文件管家
- Content outline:
  1. os模块：`os.listdir()` `os.path.join()` `os.getcwd()`
  2. pathlib：更现代的路径操作
  3. 🖥️ 计算机小知识：文件描述符——程序打开文件时OS做了什么
  4. shutil：复制、移动、删除
  5. 批量操作实战：重命名一组文件
  6. 练习：写一个自动整理下载文件夹的程序

### Lesson 32: 🗂️ 项目六：智能日记本

- Slug: `32-p6-diary`
- Title: 🗂️ 项目六：智能日记本
- Summary: 用文件和正则做一个可搜索、有时间标签的日记程序
- Content outline:
  1. 需求分析：写日记、读日记、搜索日记
  2. 设计：数据结构（字典+列表）、文件格式（日期.txt）
  3. 核心功能：写入、列出、搜索（正则）、统计
  4. 扩展挑战：加密日记、标签系统

### Lesson 33: 生成器与迭代器

- Slug: `33-generators`
- Title: 生成器：要一个给一个的魔法
- Summary: yield 让函数暂停又继续——节省内存的聪明写法
- Content outline:
  1. 回顾：for循环背后发生了什么（`__iter__` `__next__`）
  2. 🖥️ 计算机小知识：内存层级——RAM比硬盘快多少？为什么省内存重要
  3. yield：生成器函数 vs 普通函数
  4. 生成器表达式 vs 列表推导式
  5. itertools简介：count, cycle, chain
  6. 练习：写一个无限斐波那契生成器

### Lesson 34: 装饰器

- Slug: `34-decorators`
- Title: 装饰器：给函数穿新衣服
- Summary: 不改原代码就能加新功能——Python最优雅的高级技巧
- Content outline:
  1. 函数是一等公民：函数当参数、当返回值
  2. 🖥️ 计算机小知识：函数式编程范式——不只是Python有
  3. 手写一个装饰器：`@my_decorator` 背后发生了什么
  4. 带参数的装饰器
  5. functools.wraps：保留原函数信息
  6. 练习：写一个 @debug 装饰器，打印函数调用信息

### Lesson 35: ✨ 项目七：魔法计时器

- Slug: `35-p7-timer`
- Title: ✨ 项目七：魔法计时器
- Summary: 用装饰器实现计时、重试、日志——实用又酷的工具箱
- Content outline:
  1. @timer：测量函数执行时间
  2. @retry：出错自动重试
  3. @log：记录函数调用日志
  4. 组合使用：多个装饰器叠加
  5. 扩展挑战：@rate_limit 限速装饰器

### Lesson 36: 异常进阶与自定义异常

- Slug: `36-custom-exceptions`
- Title: 自定义异常：设计你自己的报错
- Summary: 让程序的专业度上一个台阶——用自定义异常精确描述问题
- Content outline:
  1. 回顾：try/except/else/finally
  2. 🖥️ 计算机小知识：调用栈与错误传播——异常在栈帧间如何传递
  3. raise：主动抛出异常
  4. 自定义Exception类：继承Exception
  5. 异常链：`raise ... from ...`
  6. 练习：为日记本项目写一套自定义异常

### Lesson 37: 命令行参数与argparse

- Slug: `37-argparse`
- Title: 命令行参数：让程序接受指令
- Summary: 像真正的命令行工具一样——用参数控制程序的行为
- Content outline:
  1. sys.argv：最原始的命令行参数
  2. 🖥️ 计算机小知识：Shell与操作系统接口——终端、Shell、环境变量
  3. argparse：参数解析神器
  4. 位置参数、可选参数、默认值
  5. 子命令：像git一样有多个动作
  6. 练习：写一个可以加/减/乘/除的命令行计算器

### Lesson 38: 🧪 项目八：单词测验生成器

- Slug: `38-p8-quiz`
- Title: 🧪 项目八：单词测验生成器
- Summary: argparse+文件+随机——自动从词库出题的测验程序
- Content outline:
  1. 需求：从文件读取词库，随机出题，计分
  2. argparse：选择模式（英译中/中译英/混合）
  3. 文件：词库格式设计（CSV或JSON）
  4. 核心逻辑：出题、答题、判分
  5. 扩展挑战：保存成绩到文件、错题本

### Lesson 39: 🚀 项目九：自选终极大作

- Slug: `39-p9-final`
- Title: 🚀 项目九：自选终极大作
- Summary: 选一个你最感兴趣的终极项目——用所有进阶技能完成它！
- Content outline:
  1. 项目选项：命令行RPG游戏 / 文件分析工具 / 网络爬虫+可视化
  2. 需求分析与设计
  3. 分步实现指引
  4. 扩展方向

## Build System Changes

New lessons follow the exact same structure as existing ones — no build.py changes needed. Just create the content directories with `lesson.md` and `meta.txt`.

## CS Knowledge Progression Map

The CS fundamentals form a coherent arc across all 39 lessons:

```
Hardware & Data           Computation             Systems & Networks
─────────────           ───────────             ──────────────────
L1  计算机组成
L2  二进制与数据表示
L3  IPO模型
L4  布尔逻辑与逻辑门 ──→ L5  指令周期
                         L6  迭代设计
                         L8  数组与连续内存
                         L9  调用栈
L10 字符编码
L11 编译与解释
L13 哈希表
                         L14 文件系统 ──────────→ L14 磁盘存储
                         L15 异常与中断
L19 抽象与封装
                                                L21 网络基础
                         L22 数据与信息
────── New Lessons ──────
L30 有限状态机
L31 文件描述符 ─────────→ L31 OS进程
L33 内存层级
L34 函数式编程
L36 调用栈深入
L37 Shell与OS接口
```

## Implementation Notes

- CS boxes are added inline to existing `lesson.md` files — no template changes
- CS boxes use the existing blockquote format with a `🖥️` emoji prefix
- New lessons (30-39) follow the same markdown + meta.txt pattern
- All new code blocks use `python thonny` type (these advanced topics need real Python, not Pyodide)
