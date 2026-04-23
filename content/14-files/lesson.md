# 第14课：文件读写

之前程序关闭后，所有数据都消失了。用文件可以把数据**永久保存**。

> **注意：** 文件操作在 Thonny 里运行，会在你的电脑上真正创建文件。

> 🖥️ **计算机小知识**
>
> 你存在电脑里的文件，到底放在哪里了？
>
> 硬盘就像一个巨大的图书馆，文件就是书。**文件系统**就是图书管理员——它维护着一个目录，记录每本书在哪个书架、哪个位置。
>
> 文件和文件夹组成一棵**目录树**：根目录是树干，每个文件夹是树枝，文件是树叶。路径 `C:\Users\Anan\diary.txt` 就是从树根一路找到那片树叶的路线。`open()` 函数就是告诉文件系统："帮我按这个路线找到那片树叶。"

## 写入文件

```python thonny title="写日记"
# 'w' 模式：写入（会覆盖原有内容）
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("今天学了文件读写！\n")
    f.write("Python 越来越好玩了。\n")

print("日记已保存！")
```

## 读取文件

```python thonny title="读日记"
with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("日记内容：")
print(content)
```

## 追加内容

```python thonny title="追加日记"
# 'a' 模式：追加（在末尾添加，不覆盖）
with open("diary.txt", "a", encoding="utf-8") as f:
    new_line = input("今天还想写什么？")
    f.write(new_line + "\n")

print("追加成功！")
```

## 文件模式总结

| 模式 | 说明 |
|------|------|
| `"r"` | 读取（文件必须存在） |
| `"w"` | 写入（覆盖原内容） |
| `"a"` | 追加（在末尾添加） |
