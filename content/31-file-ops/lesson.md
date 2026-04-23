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
