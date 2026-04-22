# 项目三：个人日记本
import datetime

FILE = "my_diary.txt"

def write():
    date = datetime.date.today()
    content = input("今天想写什么？\n> ")
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"\n【{date}】\n{content}\n")
    print("✅ 已保存！")

def read_all():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("还没有日记！")

while True:
    print("\n1-写日记  2-查看  3-退出")
    c = input("选择：")
    if c == "1": write()
    elif c == "2": read_all()
    elif c == "3": break
