# 第21课：JSON 与简单 API

## JSON：程序之间传数据的方式

**JSON** 是一种数据格式，长得很像 Python 的字典和列表：

```python demo title="JSON 长什么样"
import json

# JSON 字符串
json_text = '{"name": "Anan", "age": 9, "hobbies": ["画画", "编程", "读书"]}'

# 解析 JSON → Python 字典
data = json.loads(json_text)
print(data["name"])
print(data["hobbies"])

# Python 字典 → JSON 字符串
person = {"name": "小明", "age": 10, "scores": [95, 88, 92]}
json_str = json.dumps(person, ensure_ascii=False, indent=2)
print(json_str)
```

## JSON 与 Python 类型对照

| JSON | Python |
|------|--------|
| 对象 `{}` | 字典 `dict` |
| 数组 `[]` | 列表 `list` |
| 字符串 `""` | 字符串 `str` |
| 数字 `42` | 整数 `int` |
| `true/false` | `True/False` |
| `null` | `None` |

## JSON 文件读写

```python demo title="读写 JSON 文件"
import json

# 写入 JSON 文件
students = [
    {"name": "Anan", "age": 9, "grade": "三年级"},
    {"name": "小明", "age": 10, "grade": "四年级"},
]

# 在浏览器里模拟（实际文件操作在 Thonny 里）
json_str = json.dumps(students, ensure_ascii=False, indent=2)
print("保存的 JSON：")
print(json_str)

# 读回来
loaded = json.loads(json_str)
for s in loaded:
    print(f"{s['name']}，{s['age']}岁，{s['grade']}")
```

## API：程序的网络接口

**API** 就是程序之间对话的"窗口"。你发一个请求，API 返回数据（通常是 JSON）。

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

> **注意：** API 调用需要在 Thonny 里运行（浏览器有安全限制）。先安装 `requests`：`pip install requests`

```python thonny title="调用免费 API"
import requests
import json

# 随机猫知识（免费，不需要 API key）
response = requests.get("https://catfact.ninja/fact")
data = response.json()
print("🐱 猫猫知识：", data["fact"])

# 随机笑话（免费，不需要 API key）
response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
print("😄 笑话：", data["value"])
```

## 练习

```python thonny title="JSON 数据管理"
import json

# 1. 创建一个通讯录并保存
contacts = [
    {"name": "爸爸", "phone": "138xxxx1234", "relation": "家人"},
    {"name": "小红", "phone": "139xxxx5678", "relation": "同学"},
    {"name": "张老师", "phone": "137xxxx9012", "relation": "老师"},
]

with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)
print("通讯录已保存！")

# 2. 读取并搜索
with open("contacts.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

keyword = input("搜索名字：")
for c in loaded:
    if keyword in c["name"]:
        print(f"  找到：{c['name']} - {c['phone']}（{c['relation']}）")
```
