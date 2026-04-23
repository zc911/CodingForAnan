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
