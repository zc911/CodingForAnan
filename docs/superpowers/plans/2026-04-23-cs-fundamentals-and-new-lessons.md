# CS Fundamentals Integration + Lessons 30-39 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add computer science theory boxes to 16 existing lessons and create 10 new advanced Python lessons (30-39), all with embedded CS fundamentals.

**Architecture:** CS boxes are markdown blockquotes added inline to existing `lesson.md` files. New lessons follow the established directory structure (`content/<num>-<slug>/lesson.md` + `meta.txt`). No build system changes needed.

**Tech Stack:** Markdown content files, existing Jinja2/Python build pipeline.

---

## File Structure

### Modified files (CS box insertions)
- `content/01-hello/lesson.md` — 计算机组成
- `content/02-variables/lesson.md` — 二进制与数据表示
- `content/03-input-output/lesson.md` — IPO模型
- `content/04-conditionals/lesson.md` — 布尔逻辑与逻辑门
- `content/05-while/lesson.md` — 指令周期
- `content/06-for/lesson.md` — 迭代与计数的设计思想
- `content/08-lists/lesson.md` — 数组和连续内存
- `content/09-functions/lesson.md` — 调用栈
- `content/10-strings/lesson.md` — 字符编码
- `content/11-modules/lesson.md` — 编译与解释
- `content/13-dicts/lesson.md` — 哈希表
- `content/14-files/lesson.md` — 文件系统
- `content/15-errors/lesson.md` — 异常与中断
- `content/19-oop-basics/lesson.md` — 抽象与封装
- `content/21-json-api/lesson.md` — 网络基础
- `content/22-matplotlib/lesson.md` — 数据与信息

### New files (lessons 30-39)
- `content/30-regex/meta.txt`
- `content/30-regex/lesson.md`
- `content/31-file-ops/meta.txt`
- `content/31-file-ops/lesson.md`
- `content/32-p6-diary/meta.txt`
- `content/32-p6-diary/lesson.md`
- `content/33-generators/meta.txt`
- `content/33-generators/lesson.md`
- `content/34-decorators/meta.txt`
- `content/34-decorators/lesson.md`
- `content/35-p7-timer/meta.txt`
- `content/35-p7-timer/lesson.md`
- `content/36-custom-exceptions/meta.txt`
- `content/36-custom-exceptions/lesson.md`
- `content/37-argparse/meta.txt`
- `content/37-argparse/lesson.md`
- `content/38-p8-quiz/meta.txt`
- `content/38-p8-quiz/lesson.md`
- `content/39-p9-final/meta.txt`
- `content/39-p9-final/lesson.md`

---

### Task 1: Add CS box to Lesson 1 — 计算机组成

**Files:**
- Modify: `content/01-hello/lesson.md`

**Insertion point:** After the paragraph `Python 用文字代码，更像真正的程序员写的代码。` (line 13), before `## 你的第一行 Python 代码`

- [ ] **Step 1: Insert CS box**

Insert this blockquote between the "Python 是什么" section and "你的第一行 Python 代码" section:

```markdown
> 🖥️ **计算机小知识**
>
> 你每天用的电脑，肚子里到底有什么？主要有四个部件：
>
> - **CPU（处理器）**——电脑的大脑，负责思考和计算，就像你的脑子
> - **内存（RAM）**——CPU 的工作台，正在处理的数据放在这里，断电就没了
> - **硬盘**——长期仓库，你的照片、游戏都存在这里，断电也不丢
> - **输入输出设备**——键盘、屏幕、音箱，让你和电脑交流
>
> 你写的 Python 代码，最终会被 CPU 一条一条执行，数据在内存里来回搬运。明白这些，你就知道程序到底在"哪里跑"了！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: `Built 29 lessons → dist/` (no errors)

- [ ] **Step 3: Commit**

```bash
git add content/01-hello/lesson.md
git commit -m "content: add CS box - computer components (lesson 1)"
```

---

### Task 2: Add CS box to Lesson 2 — 二进制与数据表示

**Files:**
- Modify: `content/02-variables/lesson.md`

**Insertion point:** After the four data types table (under `## 四种基本数据类型`), before the next section about variable calculations or type operations.

- [ ] **Step 1: Insert CS box**

Insert after the types table:

```markdown
> 🖥️ **计算机小知识**
>
> 你知道吗？计算机里所有的数据——数字、文字、图片、视频——最终都变成了 **0 和 1**！这叫**二进制**。
>
> 为什么是 0 和 1？因为 CPU 里有几十亿个微小的开关，每个开关只有"开"（1）和"关"（0）两种状态。整数 `9` 在二进制里写成 `1001`，小数 `3.14` 也被转换成了一大串 0 和 1。
>
> 所以 `int` 和 `float` 不一样，不只是因为有没有小数点——它们在内存里存的 0 和 1 的排列方式完全不同！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/02-variables/lesson.md
git commit -m "content: add CS box - binary & data representation (lesson 2)"
```

---

### Task 3: Add CS box to Lesson 3 — IPO模型

**Files:**
- Modify: `content/03-input-output/lesson.md`

**Insertion point:** After the input/print basics and type conversion explanation, before `## 自我介绍生成器`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 所有的程序，不管多复杂，都在做同一件事：**输入 → 处理 → 输出**，这叫 **IPO 模型**。
>
> - 微信：你打字（输入）→ 服务器转发（处理）→ 朋友看到消息（输出）
> - 计算器：你按数字（输入）→ CPU 算结果（处理）→ 屏幕显示答案（输出）
> - 游戏：你按手柄（输入）→ 游戏引擎算画面（处理）→ 电视显示画面（输出）
>
> `input()` 就是输入，`print()` 就是输出，中间的代码就是处理。你已经掌握了所有程序的核心套路！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/03-input-output/lesson.md
git commit -m "content: add CS box - IPO model (lesson 3)"
```

---

### Task 4: Add CS box to Lesson 4 — 布尔逻辑与逻辑门

**Files:**
- Modify: `content/04-conditionals/lesson.md`

**Insertion point:** After the boolean operators explanation (`==`, `!=`, `>`, `<`, `and`, `or`, `not`) and the note about `==` vs `=`, before `## if 语句结构`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> `True` 和 `False` 看起来很简单，但 CPU 里真的有对应的零件——**逻辑门**！
>
> - **与门（AND）**：两个输入都是 1，输出才是 1——和 `and` 一模一样
> - **或门（OR）**：只要有一个输入是 1，输出就是 1——和 `or` 一模一样
> - **非门（NOT）**：输入 1 输出 0，输入 0 输出 1——和 `not` 一模一样
>
> CPU 里几十亿个晶体管，其实就是无数个逻辑门连在一起。你写的 `if a and b`，在硬件层面真的有对应的电路在闪烁！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/04-conditionals/lesson.md
git commit -m "content: add CS box - boolean logic & logic gates (lesson 4)"
```

---

### Task 5: Add CS box to Lesson 5 — 指令周期

**Files:**
- Modify: `content/05-while/lesson.md`

**Insertion point:** After the while syntax explanation and the note about checking conditions, before the section about infinite loops.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> CPU 也在"循环"！它每秒重复做三件事，这叫**指令周期**：
>
> 1. **取指（Fetch）**——从内存里取出下一条指令
> 2. **译码（Decode）**——弄清楚这条指令要干什么
> 3. **执行（Execute）**——真正做这件事（计算、搬运数据……）
>
> 你的 CPU 每秒能做几十亿次这样的循环！所以 `while` 循环不是什么特殊的东西——它就是让 CPU 在某些指令之间来回跑，而不是一直往前走。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/05-while/lesson.md
git commit -m "content: add CS box - instruction cycle (lesson 5)"
```

---

### Task 6: Add CS box to Lesson 6 — 迭代与计数的设计思想

**Files:**
- Modify: `content/06-for/lesson.md`

**Insertion point:** After the range examples (including `range(start, stop, step)`), before nested loops section.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 如果没有循环，编程会是什么样子？假设你要打印 1 到 100，就得写 100 行 `print()`！
>
> 早期的程序员真的这么干过。后来人们发明了**循环**这个概念，才让编程变得高效。几乎所有的编程语言都有循环——`for`、`while`、`do-while`……虽然写法不同，但核心思想一样：**告诉计算机"重复做这件事"**。
>
> 这就是**迭代**的思想——把一个大任务拆成重复的小步骤。不只在编程里，生活中也一样：读书是一页一页翻的，扫地是一块一块擦的。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/06-for/lesson.md
git commit -m "content: add CS box - iteration design (lesson 6)"
```

---

### Task 7: Add CS box to Lesson 8 — 数组和连续内存

**Files:**
- Modify: `content/08-lists/lesson.md`

**Insertion point:** After list indexing explanation and the note about 0-based indexing, before `## 常用操作`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 列表在内存里是怎么存的？想象一排连续的储物柜：
>
> ```
> 柜子编号:  0号   1号   2号   3号
> 里面存着: "苹果" "香蕉" "橘子" "葡萄"
> 内存地址: 100   101   102   103
> ```
>
> 这就是**数组**——数据一个挨一个排在连续的内存位置上。为什么 `fruits[0]` 这么快？因为 CPU 只要用"起始地址 + 下标"就能直接算出数据在哪，一步到位！
>
> 不过 Python 的列表比普通数组更聪明——它允许放不同类型的数据，但速度会稍慢一点点。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/08-lists/lesson.md
git commit -m "content: add CS box - arrays & contiguous memory (lesson 8)"
```

---

### Task 8: Add CS box to Lesson 9 — 调用栈

**Files:**
- Modify: `content/09-functions/lesson.md`

**Insertion point:** After the function definition explanation and the note about parameters, before `## 有返回值的函数`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 当你调用一个函数时，内存里发生了什么？想象一叠盘子：
>
> - 每调用一个函数，就在上面放一个新盘子（叫**栈帧**），里面存着这个函数的参数和变量
> - 函数执行完，就把这个盘子拿走，回到下面那个盘子继续
> - 这叠盘子就叫**调用栈（Call Stack）**
>
> 如果函数 A 调用函数 B，函数 B 调用函数 C，栈就有三个盘子。C 执行完 → B 执行完 → 回到 A。层层返回，一个都不会乱！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/09-functions/lesson.md
git commit -m "content: add CS box - call stack (lesson 9)"
```

---

### Task 9: Add CS box to Lesson 10 — 字符编码

**Files:**
- Modify: `content/10-strings/lesson.md`

**Insertion point:** After string basics (indexing, slicing, len), before `## 常用字符串方法`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> `len("你好")` 是 2，但你知道文件里存"你好"占了几个字节吗？答案是 6！
>
> 最早只有英文字符的编码叫 **ASCII**，每个字符 1 个字节，只能表示 256 种字符。但全世界有中文、日文、阿拉伯文……ASCII 完全不够用！
>
> 于是有了 **Unicode**——给全世界每个字符一个唯一的编号。"你"的编号是 20320，"好"是 22909。**UTF-8** 是 Unicode 最常用的存储方式：英文 1 字节，中文 3 字节，emoji 4 字节。所以 🎉 占的空间比 A 多四倍！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/10-strings/lesson.md
git commit -m "content: add CS box - character encoding (lesson 10)"
```

---

### Task 10: Add CS box to Lesson 11 — 编译与解释

**Files:**
- Modify: `content/11-modules/lesson.md`

**Insertion point:** After explaining what modules are and `import` syntax, before `## random 模块`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> Python 代码是怎么变成 CPU 能执行的指令的？有两种方式：
>
> - **编译型语言**（C、C++）：一次性把所有代码翻译成机器码，生成一个 `.exe` 文件，直接运行。像把整本书翻译成另一种语言，然后只看翻译版。
> - **解释型语言**（Python）：一行一行翻译、一行一行执行。像有个翻译官坐在旁边，你说一句他翻一句。
>
> Python 自带的模块（标准库）是已经写好的代码，`import` 就是告诉解释器："把这些代码也加载进来，我要用！"这比你自己从头写要快得多。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/11-modules/lesson.md
git commit -m "content: add CS box - compilation vs interpretation (lesson 11)"
```

---

### Task 11: Add CS box to Lesson 13 — 哈希表

**Files:**
- Modify: `content/13-dicts/lesson.md`

**Insertion point:** After the first dict demo (creating and accessing by key), before `## 增加、修改、删除`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 字典查找为什么这么快？因为底层用了**哈希表**！
>
> 哈希表的核心是一个神奇的函数叫**哈希函数**：给它一个键，它就能算出一个"地址"。比如 `hash("name")` 可能算出 42，那 `"name"` 对应的值就放在第 42 号位置。
>
> 所以查找时不需要从头到尾翻找——只要算一下哈希值，一步到位！这就像你知道书在第几个书架第几层，直接走过去拿，而不是一个书架一个书架地找。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/13-dicts/lesson.md
git commit -m "content: add CS box - hash tables (lesson 13)"
```

---

### Task 12: Add CS box to Lesson 14 — 文件系统

**Files:**
- Modify: `content/14-files/lesson.md`

**Insertion point:** After the file basics and the Thonny note, before `## 写入文件`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 你存在电脑里的文件，到底放在哪里了？
>
> 硬盘就像一个巨大的图书馆，文件就是书。**文件系统**就是图书管理员——它维护着一个目录，记录每本书在哪个书架、哪个位置。
>
> 文件和文件夹组成一棵**目录树**：根目录是树干，每个文件夹是树枝，文件是树叶。路径 `C:\Users\Anan\diary.txt` 就是从树根一路找到那片树叶的路线。`open()` 函数就是告诉文件系统："帮我按这个路线找到那片树叶。"
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/14-files/lesson.md
git commit -m "content: add CS box - filesystem & disk storage (lesson 14)"
```

---

### Task 13: Add CS box to Lesson 15 — 异常与中断

**Files:**
- Modify: `content/15-errors/lesson.md`

**Insertion point:** After the try/except explanation, before `## 常见错误类型`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 程序出错时，CPU 做的事叫**中断**——就像上课时突然有人敲门，老师暂停讲课去处理。
>
> CPU 每秒都会收到各种中断：键盘按下了、网卡有数据了、定时器响了……CPU 会暂停当前任务，保存现场，处理完中断再回来继续。
>
> Python 的 `try/except` 做的事情很像：提前说好"如果出错了就执行这段应急代码"，不让程序直接崩溃。这就是从硬件中断到软件异常的思路传承！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/15-errors/lesson.md
git commit -m "content: add CS box - exceptions & interrupts (lesson 15)"
```

---

### Task 14: Add CS box to Lesson 19 — 抽象与封装

**Files:**
- Modify: `content/19-oop-basics/lesson.md`

**Insertion point:** Before `## 设计一个 Pet 类`, after the motivation about "字典只能存数据……用类！".

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 为什么要发明"类"和"对象"？这背后是一个重要的设计思想：**抽象**。
>
> 你不需要知道手机里面怎么工作，只要知道按电源键能开机——这就是抽象，隐藏复杂细节，只暴露简单的接口。
>
> 编程也是一样：早期的程序是一大堆指令堆在一起（**过程式编程**），后来人们发现把相关的数据和操作包在一起会更好管理——这就是**面向对象编程（OOP）**。类把数据"封装"起来，外部只需要调用方法，不需要知道内部怎么实现。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/19-oop-basics/lesson.md
git commit -m "content: add CS box - abstraction & encapsulation (lesson 19)"
```

---

### Task 15: Add CS box to Lesson 21 — 网络基础

**Files:**
- Modify: `content/21-json-api/lesson.md`

**Insertion point:** After the API/Thonny note (before the `pip install requests` note), where the lesson starts to talk about calling an API.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> 当你在浏览器输入一个网址，到页面显示出来，中间发生了什么？
>
> 1. 你的电脑先找到那台服务器的**IP 地址**（像门牌号，比如 `93.184.216.34`）
> 2. 跟服务器建立**TCP 连接**（像打电话，确保双方能听到对方）
> 3. 发送 **HTTP 请求**（"请把首页给我"）
> 4. 服务器返回 **HTTP 响应**（HTML、JSON 等数据）
>
> API 就是步骤3和4的简化版：你发请求问一个问题，服务器返回一段 JSON 数据。`requests.get()` 帮你完成了所有这些步骤！
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/21-json-api/lesson.md
git commit -m "content: add CS box - networking basics (lesson 21)"
```

---

### Task 16: Add CS box to Lesson 22 — 数据与信息

**Files:**
- Modify: `content/22-matplotlib/lesson.md`

**Insertion point:** After the matplotlib installation note, before the first code block `第一个柱状图`.

- [ ] **Step 1: Insert CS box**

```markdown
> 🖥️ **计算机小知识**
>
> **数据**和**信息**是一回事吗？不是！
>
> - **数据**是原始的数字和文字：`37.2, 36.8, 38.5, 37.0`
> - **信息**是数据经过整理后，你能读懂的东西："第3天体温偏高，可能发烧了"
>
> 一堆数字本身没有意义，但画成折线图，你一眼就能看出趋势。**数据可视化**就是把数据变成信息的魔法——用图表代替数字，让人脑（而不是电脑）更快地理解。
```

- [ ] **Step 2: Build and verify**

Run: `python build.py`
Expected: no errors

- [ ] **Step 3: Commit**

```bash
git add content/22-matplotlib/lesson.md
git commit -m "content: add CS box - data vs information (lesson 22)"
```

---

### Task 17: Create Lesson 30 — 正则表达式

**Files:**
- Create: `content/30-regex/meta.txt`
- Create: `content/30-regex/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
正则表达式：文字侦探的放大镜
用模式匹配搜索文字——像侦探一样精准找到你要的内容
```

- [ ] **Step 2: Create lesson.md**

```markdown
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
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 30 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/30-regex/
git commit -m "content: lesson 30 - regex basics"
```

---

### Task 18: Create Lesson 31 — 文件与目录操作

**Files:**
- Create: `content/31-file-ops/meta.txt`
- Create: `content/31-file-ops/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
文件与目录操作：让Python帮你整理文件夹
批量重命名、自动归类文件——Python当你的文件管家
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第31课：文件与目录操作：让Python帮你整理文件夹

## 用 Python 管理文件

之前你学过读写文件内容，这次我们来操作文件本身——重命名、移动、复制、删除。

```python thonny title="看看当前目录有什么"
import os

# 当前工作目录
print("我在：", os.getcwd())

# 列出当前目录的文件
for item in os.listdir("."):
    print(item)
```

## os 模块：路径操作

```python thonny title="路径拼接与判断"
import os

# 拼接路径（自动处理斜杠方向）
path = os.path.join("homework", "lesson1.txt")
print("拼接路径：", path)

# 判断文件/文件夹是否存在
print("存在吗？", os.path.exists(path))

# 判断是文件还是文件夹
if os.path.exists("homework"):
    print("是文件夹？", os.path.isdir("homework"))
    print("是文件？", os.path.isfile("homework"))
```

## pathlib：更现代的方式

```python thonny title="pathlib 路径操作"
from pathlib import Path

# 创建 Path 对象
p = Path("homework")

# 创建文件夹（如果不存在）
p.mkdir(exist_ok=True)

# 列出文件夹内容
for f in p.iterdir():
    print(f.name, f.suffix)

# 找特定类型的文件
for txt in p.glob("*.txt"):
    print("找到文本文件：", txt.name)
```

> 🖥️ **计算机小知识**
>
> 当你用 `open()` 打开文件时，操作系统做了一件事：给你分配一个**文件描述符**（一个编号）。
>
> 操作系统内部维护着一张表，记录每个程序打开了哪些文件。文件描述符就是这张表的编号——程序说"读3号文件"，操作系统就知道你要读哪个。
>
> 每个程序默认有3个文件描述符：0号是键盘输入，1号是屏幕输出，2号是错误输出。所以 `print()` 其实就是往1号文件写东西！

## shutil：复制、移动、删除

```python thonny title="shutil 文件操作"
import shutil
from pathlib import Path

# 创建测试文件
Path("test_dir").mkdir(exist_ok=True)
Path("test_dir/hello.txt").write_text("你好！", encoding="utf-8")

# 复制文件
shutil.copy("test_dir/hello.txt", "test_dir/hello_backup.txt")

# 移动/重命名文件
shutil.move("test_dir/hello_backup.txt", "test_dir/greeting.txt")

# 复制整个文件夹
shutil.copytree("test_dir", "test_dir_copy")

# 删除整个文件夹
shutil.rmtree("test_dir_copy")

# 看看剩下的文件
for f in Path("test_dir").iterdir():
    print(f.name)
```

## 实战：批量重命名文件

```python thonny title="批量重命名"
import os
from pathlib import Path

# 模拟：创建一些测试文件
for i in range(1, 6):
    Path(f"photo_{i}.jpg").touch()

# 批量重命名：photo_1.jpg → 001-照片.jpg
for f in Path(".").glob("photo_*.jpg"):
    num = f.stem.split("_")[1]       # 提取数字
    new_name = f"{int(num):03d}-照片.jpg"
    f.rename(new_name)
    print(f"重命名：{f.name} → {new_name}")
```

## 练习

```python thonny title="自动整理下载文件夹"
from pathlib import Path
import shutil

# 模拟一个下载文件夹
download = Path("downloads")
download.mkdir(exist_ok=True)
(download / "报告.docx").touch()
(download / "照片.jpg").touch()
(download / "歌曲.mp3").touch()
(download / "笔记.txt").touch()
(download / "视频.mp4").touch()

# 按扩展名归类到子文件夹
categories = {
    ".jpg": "图片",
    ".png": "图片",
    ".mp3": "音乐",
    ".mp4": "视频",
    ".docx": "文档",
    ".txt": "文档",
}

for f in download.iterdir():
    if f.is_file():
        folder = categories.get(f.suffix, "其他")
        target = download / folder
        target.mkdir(exist_ok=True)
        shutil.move(str(f), target / f.name)
        print(f"移动 {f.name} → {folder}/")

# 看看整理结果
for folder in sorted(download.iterdir()):
    if folder.is_dir():
        print(f"\n{folder.name}/")
        for f in folder.iterdir():
            print(f"  {f.name}")
```
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 31 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/31-file-ops/
git commit -m "content: lesson 31 - file & directory operations"
```

---

### Task 19: Create Lesson 32 — 项目六：智能日记本

**Files:**
- Create: `content/32-p6-diary/meta.txt`
- Create: `content/32-p6-diary/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
🗂️ 项目六：智能日记本
用文件和正则做一个可搜索、有时间标签的日记程序
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第32课：🗂️ 项目六：智能日记本

## 这个项目做什么？

我们要做一个**智能日记本**程序！它能：

- ✍️ 写日记——输入内容，自动保存
- 📖 读日记——查看某天的日记
- 🔍 搜索日记——用正则表达式搜索关键词
- 📊 统计——一共写了多少篇，哪些词出现最多

## 需求分析

先想清楚程序要做什么：

1. **写入**：用户输入内容，程序自动加上日期保存
2. **列出**：显示所有日记的日期列表
3. **搜索**：输入关键词，找到包含它的所有日记
4. **统计**：统计日记数量和字数

## 设计：数据怎么存？

每篇日记保存成一个独立的文件，文件名用日期：

```
diary/
├── 2026-04-20.txt
├── 2026-04-21.txt
└── 2026-04-23.txt
```

这样最简单——不需要数据库，用文件就够了！

## 第一步：创建和写入日记

```python thonny title="创建日记本 - 写入功能"
from pathlib import Path
from datetime import datetime

DIARY_DIR = Path("my_diary")
DIARY_DIR.mkdir(exist_ok=True)

def write_diary(content):
    """写一篇日记，文件名用今天的日期"""
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = DIARY_DIR / f"{today}.txt"

    # 如果今天已经写过，就追加；否则新建
    mode = "a" if filepath.exists() else "w"
    with open(filepath, mode, encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M")
        f.write(f"\n[{timestamp}]\n{content}\n")

    print(f"✅ 日记已保存到 {filepath.name}")

# 试试写入
write_diary("今天学了正则表达式，好酷！")
write_diary("晚上吃了冰淇淋 🍦")
```

## 第二步：列出所有日记

```python thonny title="列出所有日记"
from pathlib import Path

DIARY_DIR = Path("my_diary")

def list_diaries():
    """列出所有日记，按日期排序"""
    files = sorted(DIARY_DIR.glob("*.txt"))
    if not files:
        print("还没有日记哦，快写一篇吧！")
        return

    print(f"📓 一共 {len(files)} 篇日记：")
    for f in files:
        # 读取第一行作为预览
        with open(f, encoding="utf-8") as file:
            preview = file.read(50).replace("\n", " ")
        print(f"  {f.stem}  {preview}...")

list_diaries()
```

## 第三步：搜索日记

```python thonny title="用正则搜索日记"
import re
from pathlib import Path

DIARY_DIR = Path("my_diary")

def search_diary(keyword):
    """搜索包含关键词的日记（支持正则！）"""
    pattern = re.compile(keyword, re.IGNORECASE)
    results = []

    for f in sorted(DIARY_DIR.glob("*.txt")):
        content = f.read_text(encoding="utf-8")
        matches = pattern.findall(content)
        if matches:
            results.append((f.stem, len(matches), matches))

    if not results:
        print(f"没有找到包含 '{keyword}' 的日记")
        return

    print(f"🔍 搜索 '{keyword}' 的结果：")
    for date, count, matches in results:
        print(f"  📅 {date} — 出现 {count} 次：{matches[:5]}")

search_diary("日记|冰淇淋|正则")
```

## 第四步：统计

```python thonny title="日记统计"
from pathlib import Path
from collections import Counter
import re

DIARY_DIR = Path("my_diary")

def diary_stats():
    """统计日记本的数据"""
    files = list(DIARY_DIR.glob("*.txt"))
    if not files:
        print("还没有日记哦！")
        return

    total_chars = 0
    all_words = []

    for f in files:
        content = f.read_text(encoding="utf-8")
        total_chars += len(content)
        # 提取中文词（简单方式：连续中文字符）
        words = re.findall(r"[一-鿿]+", content)
        all_words.extend(words)

    print(f"📊 日记统计：")
    print(f"  📝 共 {len(files)} 篇日记")
    print(f"  📏 共 {total_chars} 个字符")
    print(f"  🏆 最常用词：")
    for word, count in Counter(all_words).most_common(10):
        if len(word) > 1:  # 只显示两个字以上的词
            print(f"     {word} ({count}次)")

diary_stats()
```

## 扩展挑战

- 🔐 **加密日记**：写入时用简单的加密（比如每个字符偏移3位），读取时解密
- 🏷️ **标签系统**：用 `#学习` `#开心` 这样的标签，搜索时可以按标签筛选
- 📅 **日历视图**：打印一个月的日历，有日记的日期标上 ⭐
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 32 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/32-p6-diary/
git commit -m "content: lesson 32 - project 6: smart diary"
```

---

### Task 20: Create Lesson 33 — 生成器与迭代器

**Files:**
- Create: `content/33-generators/meta.txt`
- Create: `content/33-generators/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
生成器：要一个给一个的魔法
yield 让函数暂停又继续——节省内存的聪明写法
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第33课：生成器：要一个给一个的魔法

## for 循环背后发生了什么？

`for x in [1, 2, 3]` 看起来简单，但 Python 在背后做了什么？

```python thonny title="手动迭代"
nums = [1, 2, 3]
it = iter(nums)          # 获取迭代器
print(next(it))          # 1
print(next(it))          # 2
print(next(it))          # 3
# print(next(it))        # ❌ StopIteration！
```

`iter()` 把列表变成**迭代器**，`next()` 每次取一个值。`for` 循环其实就是不断调用 `next()`，直到 `StopIteration`。

## yield：让函数暂停的魔法

普通函数 `return` 一次就结束了。`yield` 让函数**暂停**，下次调用时**继续**：

```python thonny title="第一个生成器"
def count_up(max_num):
    n = 1
    while n <= max_num:
        yield n        # 暂停，把 n 交出去
        n += 1         # 下次从这里继续

for num in count_up(5):
    print(num, end=" ")
print()

# 生成器是一个迭代器
g = count_up(3)
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```

> 🖥️ **计算机小知识**
>
> 内存就像一张书桌，空间有限。如果你要处理 1 亿个数字，全部放进列表，电脑可能直接卡死！
>
> 生成器的聪明之处：不把所有数据一次性放进内存，而是**要一个算一个**。就像你吃自助餐，不用把所有菜端到桌上——吃完一盘再去拿下一盘。
>
> 这就是**内存层级**的重要性：CPU 缓存最快（但最小）→ 内存很快 → 硬盘最慢（但最大）。省内存 = 让程序跑得更快更稳！

## 生成器表达式

列表推导式用 `[]`，生成器表达式用 `()`——同样的事，但不占内存：

```python thonny title="生成器表达式 vs 列表推导式"
import sys

# 列表推导式：一次性生成所有数据
nums_list = [x * x for x in range(1000)]
print("列表大小：", sys.getsizeof(nums_list), "字节")

# 生成器表达式：按需生成
nums_gen = (x * x for x in range(1000))
print("生成器大小：", sys.getsizeof(nums_gen), "字节")

# 生成器用起来和列表一样
for i, val in enumerate(nums_gen):
    if i >= 5:
        break
    print(val, end=" ")
print("... (只算了需要的几个)")
```

## itertools：生成器的好帮手

```python thonny title="itertools 常用工具"
from itertools import count, cycle, chain, islice

# count：无限计数器
for i in islice(count(1), 5):    # 取前5个
    print(i, end=" ")
print()

# cycle：无限循环
colors = cycle(["🔴", "🔵", "🟢"])
for _ in range(6):
    print(next(colors), end=" ")
print()

# chain：把多个可迭代对象连起来
a = [1, 2, 3]
b = ["x", "y"]
print(list(chain(a, b)))
```

## 练习

```python thonny title="无限斐波那契生成器"
def fibonacci():
    """无限斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 打印前 15 个斐波那契数
for i, num in enumerate(fibonacci()):
    if i >= 15:
        break
    print(f"F({i}) = {num}")
```
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 33 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/33-generators/
git commit -m "content: lesson 33 - generators & iterators"
```

---

### Task 21: Create Lesson 34 — 装饰器

**Files:**
- Create: `content/34-decorators/meta.txt`
- Create: `content/34-decorators/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
装饰器：给函数穿新衣服
不改原代码就能加新功能——Python最优雅的高级技巧
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第34课：装饰器：给函数穿新衣服

## 函数是一等公民

在 Python 里，函数和数字、字符串一样，可以**当参数传递**，也可以**当返回值**：

```python thonny title="函数当参数"
def say_hello(name):
    return f"你好，{name}！"

def say_bye(name):
    return f"再见，{name}！"

def greet(func, name):
    """接收一个函数作为参数"""
    print(func(name))

greet(say_hello, "Anan")
greet(say_bye, "Anan")
```

```python thonny title="函数当返回值"
def make_multiplier(n):
    """返回一个新函数"""
    def multiply(x):
        return x * n
    return multiply

times_3 = make_multiplier(3)
times_5 = make_multiplier(5)

print(times_3(10))   # 30
print(times_5(10))   # 50
```

> 🖥️ **计算机小知识**
>
> 把函数当变量传来传去，这不只是 Python 的花招——这是一种编程思想，叫**函数式编程**。
>
> 函数式编程的核心：函数像数据一样可以被创建、传递、组合。LISP（1958年）是第一个函数式语言，比 Python 早了30多年！Python 从函数式编程借鉴了很多好东西：`map()`、`filter()`、`lambda`、装饰器……
>
> 不同的编程思想像不同的工具：过程式 = 按步骤来，面向对象 = 分角色来，函数式 = 组合小函数来。高手会根据问题选择最合适的工具。

## 手写第一个装饰器

装饰器 = 接收一个函数，返回一个**增强版**函数：

```python thonny title="第一个装饰器"
def my_decorator(func):
    def wrapper():
        print("✨ 函数执行前")
        func()
        print("✨ 函数执行后")
    return wrapper

def say_hi():
    print("你好！")

# 手动装饰
say_hi = my_decorator(say_hi)
say_hi()
```

用 `@` 语法更优雅——效果完全一样：

```python thonny title="@ 语法糖"
def my_decorator(func):
    def wrapper():
        print("✨ 函数执行前")
        func()
        print("✨ 函数执行后")
    return wrapper

@my_decorator       # 等于 say_hi = my_decorator(say_hi)
def say_hi():
    print("你好！")

say_hi()
```

## 装饰带参数的函数

```python thonny title="装饰带参数的函数"
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} 耗时 {end-start:.4f} 秒")
        return result
    return wrapper

@timer
def slow_add(a, b):
    import time
    time.sleep(0.1)
    return a + b

result = slow_add(3, 7)
print(f"结果：{result}")
```

## 带参数的装饰器

如果装饰器自己也要接收参数，就多包一层：

```python thonny title="带参数的装饰器"
def repeat(n):
    """让函数执行 n 次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)
    return msg

say("你好！")
```

## functools.wraps

装饰器会把原函数的名字和文档覆盖掉。用 `@wraps` 修复：

```python thonny title="用 wraps 保留原函数信息"
from functools import wraps

def my_decorator(func):
    @wraps(func)           # 保留 func 的名字和文档
    def wrapper(*args, **kwargs):
        """我是 wrapper"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """打招呼的函数"""
    return f"你好，{name}！"

print(greet("Anan"))
print("函数名：", greet.__name__)       # greet（不是 wrapper）
print("文档：", greet.__doc__)           # 打招呼的函数
```

## 练习

```python thonny title="写一个 @debug 装饰器"
from functools import wraps

def debug(func):
    """打印函数调用的参数和返回值"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        print(f"🔍 调用 {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"🔍 返回 {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

@debug
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

add(3, 7)
print("---")
factorial(5)
```
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 34 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/34-decorators/
git commit -m "content: lesson 34 - decorators"
```

---

### Task 22: Create Lesson 35 — 项目七：魔法计时器

**Files:**
- Create: `content/35-p7-timer/meta.txt`
- Create: `content/35-p7-timer/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
✨ 项目七：魔法计时器
用装饰器实现计时、重试、日志——实用又酷的工具箱
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第35课：✨ 项目七：魔法计时器

## 这个项目做什么？

上节课学了装饰器，现在用装饰器做一个**实用工具箱**！每个装饰器给函数加一种超能力：

- ⏱️ @timer — 测量函数执行时间
- 🔄 @retry — 出错自动重试
- 📝 @log — 记录函数调用日志

## @timer：测量执行时间

```python thonny title="@timer 装饰器"
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱️ {func.__name__} 用了 {elapsed:.4f} 秒")
        return result
    return wrapper

@timer
def slow_count(n):
    """数到 n，每数一个稍等一下"""
    for i in range(n):
        time.sleep(0.01)
    return f"数完了 {n}！"

result = slow_count(10)
print(result)

@timer
def fast_math():
    return sum(range(1000000))

fast_math()
```

## @retry：出错自动重试

```python thonny title="@retry 装饰器"
import time
import random
from functools import wraps

def retry(max_attempts=3, delay=0.5):
    """出错时自动重试"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"❌ 第{attempt}次失败：{e}")
                    if attempt < max_attempts:
                        print(f"   ⏳ {delay}秒后重试...")
                        time.sleep(delay)
                    else:
                        print(f"💥 全部 {max_attempts} 次都失败了！")
                        raise
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.2)
def unstable_network():
    """模拟不稳定的网络请求（50%概率失败）"""
    if random.random() < 0.5:
        raise ConnectionError("网络连接失败")
    return "✅ 数据获取成功！"

# 试试看好不好运
try:
    result = unstable_network()
    print(result)
except ConnectionError:
    print("最终失败")
```

## @log：记录调用日志

```python thonny title="@log 装饰器"
from datetime import datetime
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%H:%M:%S")
        args_str = ", ".join(str(a) for a in args)
        print(f"[{timestamp}] 📞 调用 {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] 📤 返回 {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def greet(name, greeting="你好"):
    return f"{greeting}，{name}！"

add(3, 7)
print()
greet("Anan")
print()
greet("Anan", greeting="早上好")
```

## 组合使用：装饰器叠叠乐

多个装饰器可以叠在一起，**从下往上**执行：

```python thonny title="装饰器叠加"
@timer
@log
@retry(max_attempts=3, delay=0.1)
def dice_game():
    """掷骰子，掷到6才算赢"""
    import random
    result = random.randint(1, 6)
    if result != 6:
        raise ValueError(f"掷到了 {result}，不是6！")
    return f"🎉 掷到了 {result}！"

try:
    print(dice_game())
except ValueError as e:
    print(f"最终结果：{e}")
```

## 扩展挑战

- 🚦 **@rate_limit(seconds)**：限制函数每 N 秒只能调用一次
- 📊 **@count_calls**：统计函数被调用了多少次
- 🔒 **@require_auth**：模拟权限检查，只有管理员才能调用

```python thonny title="扩展挑战提示"
from functools import wraps

def count_calls(func):
    """统计函数被调用了多少次"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"📊 {func.__name__} 已被调用 {wrapper.calls} 次")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def hello():
    print("你好！")

hello()
hello()
hello()
print(f"总共调用了 {hello.calls} 次")
```
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 35 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/35-p7-timer/
git commit -m "content: lesson 35 - project 7: magic timer with decorators"
```

---

### Task 23: Create Lesson 36 — 异常进阶与自定义异常

**Files:**
- Create: `content/36-custom-exceptions/meta.txt`
- Create: `content/36-custom-exceptions/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
自定义异常：设计你自己的报错
让程序的专业度上一个台阶——用自定义异常精确描述问题
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第36课：自定义异常：设计你自己的报错

## 回顾：try/except 完整语法

```python thonny title="try/except/else/finally"
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ 不能除以0！")
        return None
    else:
        print("✅ 计算成功！")
        return result
    finally:
        print("📌 无论如何都会执行")

print(divide(10, 3))
print("---")
print(divide(10, 0))
```

> 🖥️ **计算机小知识**
>
> 当程序出错时，Python 会从出错的那个函数开始，沿着**调用栈**一层层往上抛异常。
>
> 想象你请朋友A帮忙，A又请B帮忙，B又请C帮忙。如果C出了问题，C会告诉B，B告诉A，A告诉你。每个人都可以选择"处理"或者"继续往上抛"。
>
> `traceback` 那一长串错误信息，就是异常在调用栈中旅行的路径！`except` 就像在某一层放了个"拦截网"，把异常拦住处理掉。

## raise：主动抛出异常

```python thonny title="raise 主动报错"
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数！")
    if age < 0 or age > 150:
        raise ValueError(f"年龄 {age} 不合理！应该在 0-150 之间")
    print(f"✅ 年龄设置为 {age}")

set_age(9)
try:
    set_age(-5)
except ValueError as e:
    print(f"捕获到错误：{e}")

try:
    set_age("九")
except TypeError as e:
    print(f"捕获到错误：{e}")
```

## 自定义异常类

Python 内置的异常类型不够用时，自己定义！只需继承 `Exception`：

```python thonny title="自定义异常"
class DiaryError(Exception):
    """日记本相关的所有错误"""
    pass

class DiaryNotFoundError(DiaryError):
    """日记不存在"""
    def __init__(self, date):
        self.date = date
        super().__init__(f"📅 {date} 的日记不存在")

class DiaryEmptyError(DiaryError):
    """日记内容为空"""
    def __init__(self, date):
        self.date = date
        super().__init__(f"📝 {date} 的日记是空的")

# 使用自定义异常
def read_diary(date, content):
    if content is None:
        raise DiaryNotFoundError(date)
    if len(content.strip()) == 0:
        raise DiaryEmptyError(date)
    print(f"📖 {date}：{content}")

try:
    read_diary("2026-04-20", None)
except DiaryNotFoundError as e:
    print(f"错误：{e}")

try:
    read_diary("2026-04-21", "   ")
except DiaryError as e:
    print(f"日记错误：{e}")
```

## 异常链：raise ... from ...

有时候你捕获了一个异常，想换成自己的类型，但保留原始原因：

```python thonny title="异常链"
class ConfigError(Exception):
    """配置文件错误"""
    pass

def load_config():
    try:
        with open("不存在的文件.txt") as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigError("配置文件找不到") from e

try:
    load_config()
except ConfigError as e:
    print(f"自定义错误：{e}")
    print(f"原始原因：{e.__cause__}")
```

## 练习

```python thonny title="为日记本设计异常体系"
class DiaryError(Exception):
    """日记本基础异常"""
    pass

class DiaryNotFoundError(DiaryError):
    def __init__(self, date):
        super().__init__(f"📅 {date} 的日记不存在")

class DiaryEmptyError(DiaryError):
    def __init__(self, date):
        super().__init__(f"📝 {date} 的日记是空的")

class DiaryWriteError(DiaryError):
    def __init__(self, date, reason):
        super().__init__(f"✍️ 无法写入 {date} 的日记：{reason}")

def safe_write_diary(date, content):
    """安全的日记写入函数"""
    if not content or len(content.strip()) == 0:
        raise DiaryEmptyError(date)
    try:
        with open(f"diary_{date}.txt", "w") as f:
            f.write(content)
    except OSError as e:
        raise DiaryWriteError(date, str(e)) from e
    print(f"✅ {date} 的日记已保存")

# 测试
try:
    safe_write_diary("2026-04-23", "")
except DiaryError as e:
    print(f"操作失败：{e}")
```
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 36 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/36-custom-exceptions/
git commit -m "content: lesson 36 - custom exceptions"
```

---

### Task 24: Create Lesson 37 — 命令行参数与argparse

**Files:**
- Create: `content/37-argparse/meta.txt`
- Create: `content/37-argparse/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
命令行参数：让程序接受指令
像真正的命令行工具一样——用参数控制程序的行为
```

- [ ] **Step 2: Create lesson.md**

```markdown
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
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 37 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/37-argparse/
git commit -m "content: lesson 37 - argparse & command line arguments"
```

---

### Task 25: Create Lesson 38 — 项目八：单词测验生成器

**Files:**
- Create: `content/38-p8-quiz/meta.txt`
- Create: `content/38-p8-quiz/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
🧪 项目八：单词测验生成器
argparse+文件+随机——自动从词库出题的测验程序
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第38课：🧪 项目八：单词测验生成器

## 这个项目做什么？

做一个**单词测验生成器**！它能：

- 📚 从文件读取词库
- 🎲 随机出题
- 🎯 自动判分
- ⚙️ 用命令行参数控制模式

## 需求分析

程序要实现：

1. 从 JSON 文件读取词库
2. 支持3种模式：英译中、中译英、混合
3. 用 argparse 选择模式和题目数量
4. 答完后显示得分和错题

## 第一步：设计词库格式

创建 `words.json` 文件（先在代码里创建一个示例）：

```python thonny title="创建词库文件"
import json
from pathlib import Path

# 示例词库
word_bank = [
    {"en": "apple", "cn": "苹果"},
    {"en": "cat", "cn": "猫"},
    {"en": "book", "cn": "书"},
    {"en": "water", "cn": "水"},
    {"en": "sun", "cn": "太阳"},
    {"en": "moon", "cn": "月亮"},
    {"en": "flower", "cn": "花"},
    {"en": "fish", "cn": "鱼"},
    {"en": "happy", "cn": "开心的"},
    {"en": "friend", "cn": "朋友"},
    {"en": "school", "cn": "学校"},
    {"en": "music", "cn": "音乐"},
    {"en": "computer", "cn": "电脑"},
    {"en": "dream", "cn": "梦想"},
    {"en": "animal", "cn": "动物"},
]

# 保存词库
Path("words.json").write_text(
    json.dumps(word_bank, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
print(f"✅ 词库已保存，共 {len(word_bank)} 个单词")
```

## 第二步：核心出题逻辑

```python thonny title="出题与判分"
import json
import random

def load_words(filepath="words.json"):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

def run_quiz(words, mode="en2cn", count=5):
    """运行测验"""
    score = 0
    wrong = []
    questions = random.sample(words, min(count, len(words)))

    print(f"\n📝 单词测验开始！模式：{mode}，共 {len(questions)} 题\n")

    for i, word in enumerate(questions, 1):
        if mode == "en2cn":
            question = word["en"]
            answer = word["cn"]
        else:
            question = word["cn"]
            answer = word["en"]

        user_answer = input(f"第{i}题：{question} = ")

        if user_answer.strip() == answer:
            print("  ✅ 正确！")
            score += 1
        else:
            print(f"  ❌ 错误！正确答案：{answer}")
            wrong.append({"question": question, "correct": answer,
                          "yours": user_answer})

    print(f"\n📊 得分：{score}/{len(questions)}")
    if wrong:
        print("\n❌ 错题回顾：")
        for w in wrong:
            print(f"  {w['question']} = {w['correct']}（你答了：{w['yours']}）")

    return score, wrong

# 测试（用固定数据，不用 input）
words = load_words()
print(f"词库有 {len(words)} 个单词")
sample = random.sample(words, 3)
print("随机3个词：", [(w["en"], w["cn"]) for w in sample])
```

## 第三步：加上 argparse

```python thonny title="完整程序 + argparse"
import argparse
import json
import random
import sys

def main():
    parser = argparse.ArgumentParser(description="📝 单词测验生成器")
    parser.add_argument("--mode", choices=["en2cn", "cn2en", "mix"],
                        default="en2cn", help="测验模式")
    parser.add_argument("--count", type=int, default=5, help="题目数量")
    parser.add_argument("--file", default="words.json", help="词库文件")

    # 模拟命令行（在 Thonny 中运行）
    sys.argv = ["quiz.py", "--mode", "en2cn", "--count", "3"]

    args = parser.parse_args()

    words = load_words(args.file)
    print(f"📚 词库：{len(words)} 个单词")
    print(f"📝 模式：{args.mode}，题数：{args.count}")

    if args.mode == "mix":
        # 混合模式：每题随机选方向
        for word in random.sample(words, min(args.count, len(words))):
            if random.random() < 0.5:
                print(f"  英→中：{word['en']} = ?")
            else:
                print(f"  中→英：{word['cn']} = ?")
    else:
        # 实际运行测验（需要输入，这里只展示框架）
        print("  （运行测验需要真实输入，请在终端中运行）")

if __name__ == "__main__":
    main()
```

## 扩展挑战

- 💾 **保存成绩**：把每次得分写入 `scores.json`，可以查看历史成绩
- 📓 **错题本**：把错题单独保存，下次可以专门复习错题
- 📈 **成绩趋势**：用 matplotlib 画出历次得分折线图
- 🔄 **间隔重复**：答错的词下次出现概率更高（类似 Anki）
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 38 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/38-p8-quiz/
git commit -m "content: lesson 38 - project 8: word quiz generator"
```

---

### Task 26: Create Lesson 39 — 项目九：自选终极大作

**Files:**
- Create: `content/39-p9-final/meta.txt`
- Create: `content/39-p9-final/lesson.md`

- [ ] **Step 1: Create meta.txt**

```plain
🚀 项目九：自选终极大作
选一个你最感兴趣的终极项目——用所有进阶技能完成它！
```

- [ ] **Step 2: Create lesson.md**

```markdown
# 第39课：🚀 项目九：自选终极大作

## 你的终极项目！

恭喜你走到了最后一课！🎉 现在是时候用你学过的所有技能，完成一个**属于自己的项目**。

下面有三个方向，选一个你最感兴趣的——或者自己想一个！

## 方向一：命令行 RPG 游戏

做一个文字冒险游戏！玩家在命令行里探索世界、打怪升级。

**技术要点：**
- 类与对象：Player、Monster、Item
- 随机事件：random 模块
- 存档系统：JSON 保存/加载游戏进度
- 命令行参数：argparse 选择新游戏/继续

**设计思路：**
```python thonny title="RPG 游戏框架"
import json
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"🧙 {self.name} | HP: {self.hp} | 攻击: {self.attack} | 金币: {self.gold}")
        if self.inventory:
            print(f"   背包：{', '.join(self.inventory)}")

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

def battle(player, monster):
    print(f"\n⚔️ 遭遇了 {monster.name}！")
    while player.is_alive() and monster.is_alive():
        monster.hp -= player.attack
        print(f"  你攻击了 {monster.name}，造成 {player.attack} 伤害")
        if monster.is_alive():
            player.hp -= monster.attack
            print(f"  {monster.name} 攻击了你，造成 {monster.attack} 伤害")

    if player.is_alive():
        reward = random.randint(5, 20)
        player.gold += reward
        print(f"  🎉 你赢了！获得 {reward} 金币")
    else:
        print("  💀 你被击败了...")

# 快速演示
hero = Player("Anan")
hero.show_status()

goblin = Monster("小恶魔", 20, 5)
battle(hero, goblin)
hero.show_status()
```

**扩展方向：**
- 多个地图房间，用字典存储
- 装备系统：武器增加攻击力
- 商店：用金币购买物品
- 用 @log 装饰器记录战斗日志

## 方向二：文件分析工具

做一个分析文本文件的工具——统计字数、找最常用词、生成报告。

**技术要点：**
- 文件读写：os、pathlib
- 正则表达式：提取单词、过滤标点
- 数据可视化：matplotlib 画词频图
- argparse：选择分析模式和文件路径

**设计思路：**
```python thonny title="文件分析框架"
import re
from pathlib import Path
from collections import Counter

def analyze_text(filepath):
    """分析文本文件"""
    content = Path(filepath).read_text(encoding="utf-8")

    # 基本统计
    chars = len(content)
    lines = content.count("\n") + 1

    # 提取中文词和英文词
    chinese_chars = re.findall(r"[一-鿿]", content)
    english_words = re.findall(r"[a-zA-Z]+", content.lower())

    # 词频统计
    cn_freq = Counter(chinese_chars).most_common(10)
    en_freq = Counter(english_words).most_common(10)

    print(f"📄 文件：{filepath}")
    print(f"📏 字符数：{chars}")
    print(f"📝 行数：{lines}")
    print(f"🇨🇳 中文高频字：{cn_freq}")
    print(f"🇺🇸 英文高频词：{en_freq}")

# 创建示例文件并分析
Path("sample.txt").write_text(
    "Python is fun! Python is great!\n学习Python很有趣。\n编程让世界更美好。",
    encoding="utf-8"
)
analyze_text("sample.txt")
```

**扩展方向：**
- 生成 HTML 报告
- 支持批量分析整个文件夹
- 用 matplotlib 画词频柱状图
- 支持导出分析结果为 JSON

## 方向三：网络爬虫 + 数据可视化

做一个从网上获取数据并可视化的工具。

**技术要点：**
- requests：获取网页/API 数据
- JSON 解析：提取有用信息
- matplotlib：数据可视化
- argparse + 自定义异常

**设计思路：**
```python thonny title="API 数据获取框架"
import json
import random
from collections import Counter

# 模拟 API 数据（实际需要 requests 调用真实 API）
mock_weather = {
    "city": "北京",
    "forecast": [
        {"date": "04-20", "temp": 22, "weather": "晴"},
        {"date": "04-21", "temp": 19, "weather": "多云"},
        {"date": "04-22", "temp": 25, "weather": "晴"},
        {"date": "04-23", "temp": 21, "weather": "小雨"},
        {"date": "04-24", "temp": 23, "weather": "晴"},
    ]
}

def analyze_weather(data):
    temps = [day["temp"] for day in data["forecast"]]
    print(f"🌤️ {data['city']} 天气分析：")
    print(f"  平均温度：{sum(temps)/len(temps):.1f}°C")
    print(f"  最高温度：{max(temps)}°C")
    print(f"  最低温度：{min(temps)}°C")

    weather_count = Counter(day["weather"] for day in data["forecast"])
    print(f"  天气分布：{dict(weather_count)}")

analyze_weather(mock_weather)
```

> **注意：** 真实的网络请求需要在 Thonny 中运行，先 `pip install requests`。

**扩展方向：**
- 用 matplotlib 画温度折线图
- 支持多个城市对比
- 数据缓存到本地 JSON 文件
- 添加 @retry 装饰器处理网络错误

## 开工吧！

选定方向后，按这个流程来：

1. 📋 **需求分析**——写下你的程序要做什么（5-8条）
2. 🏗️ **设计**——需要哪些类/函数？数据怎么存？
3. 🔨 **分步实现**——先做最小版本，再慢慢加功能
4. 🧪 **测试**——每个功能都试试，确保没有 bug
5. ✨ **扩展**——加上额外功能，让它更酷

记住：**先让它跑起来，再让它跑得好！** 不用追求完美，第一版能运行就是胜利！🚀
```

- [ ] **Step 3: Build and verify**

Run: `python build.py`
Expected: `Built 39 lessons → dist/`

- [ ] **Step 4: Commit**

```bash
git add content/39-p9-final/
git commit -m "content: lesson 39 - project 9: final project"
```

---

### Task 27: Final build verification

- [ ] **Step 1: Full build**

Run: `python build.py`
Expected: `Built 39 lessons → dist/`

- [ ] **Step 2: Verify all lesson counts**

Run: `ls content/ | wc -l`
Expected: 39

- [ ] **Step 3: Verify all meta.txt files exist**

Run: `find content -name meta.txt | wc -l`
Expected: 39

- [ ] **Step 4: Verify dist output**

Run: `ls dist/ | grep -v static | wc -l`
Expected: 39 (lesson directories) + 1 (index.html) = at least 39 directories

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "content: complete CS fundamentals integration + lessons 30-39"
```
```

Now let me do the self-review.

**Spec coverage check:**
- 16 CS boxes in existing lessons → Tasks 1-16 ✓
- 10 new lessons (30-39) → Tasks 17-26 ✓
- Build verification → Task 27 ✓

**Placeholder scan:** Tasks 19-26 (project lessons and some new concept lessons) say "Write full lesson content covering..." without the actual markdown. These are content-writing tasks where the full text would be 80-120 lines each — too large to inline in a plan. However, per the "No Placeholders" rule, I should provide the actual content. Let me update Tasks 17-18 (which I did provide full content for) as the template, and note that Tasks 19-26 need the same treatment.

Actually, looking at this more carefully — the plan for Tasks 17-18 has complete lesson.md content inline. Tasks 19-26 describe what to write but don't include the actual content. This violates the "No Placeholders" rule. However, writing 8 full lessons (each 80-120 lines of Chinese markdown) inline in the plan would make it enormously long. The practical approach is to provide the full content for the first 2 new lessons as templates (Tasks 17-18 already done), then let the implementer follow the same pattern. But the skill says "never write them" for these patterns...

Let me provide full content for all 10 new lessons. I'll write them out.<tool_call>Read<arg_key>file_path</arg_key><arg_value>/Users/chenzhen48/Workspace/CodingForAnan/docs/superpowers/plans/2026-04-23-cs-fundamentals-and-new-lessons.md