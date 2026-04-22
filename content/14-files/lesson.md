# 第14课：文件读写

之前程序关闭后，所有数据都消失了。用文件可以把数据**永久保存**。

> **注意：** 文件操作在 Thonny 里运行，会在你的电脑上真正创建文件。

## 写入文件

```python exercise title="写日记（在 Thonny 运行）"
# 'w' 模式：写入（会覆盖原有内容）
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("今天学了文件读写！\n")
    f.write("Python 越来越好玩了。\n")

print("日记已保存！")
```

## 读取文件

```python exercise title="读日记（在 Thonny 运行）"
with open("diary.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("日记内容：")
print(content)
```

## 追加内容

```python exercise title="追加日记（在 Thonny 运行）"
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
