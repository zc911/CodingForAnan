# 第25课：AI 对话机器人

## 让 AI 记住上下文

上节课每次调用 API 都是"失忆"的——AI 不知道之前聊了什么。要让 AI **连续对话**，需要把之前的对话记录都发过去：

```python exercise title="多轮对话机器人（在 Thonny 运行）"
import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

# 对话历史——AI 的"记忆"
messages = [
    {"role": "system", "content": "你是一个友好的学习伙伴，说话简单有趣"}
]

def chat(user_input):
    # 把用户的话加到历史里
    messages.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": messages
    }

    response = requests.post(URL, headers=headers, json=data)
    result = response.json()
    ai_reply = result["choices"][0]["message"]["content"]

    # 把 AI 的回复也加到历史里
    messages.append({"role": "assistant", "content": ai_reply})

    return ai_reply

# 聊天循环
print("🤖 AI 对话机器人（输入 '退出' 结束）")
print("=" * 40)

while True:
    user_input = input("你：")
    if user_input.strip() in ["退出", "exit", "quit"]:
        print("再见！👋")
        break

    reply = chat(user_input)
    print(f"AI：{reply}\n")
```

## 用 system 消息控制 AI 人格

`system` 消息就像给 AI 写"人设"：

```python exercise title="不同人格的 AI（在 Thonny 运行）"
import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

def create_bot(personality):
    """创建一个带人设的 AI 机器人"""
    messages = [{"role": "system", "content": personality}]

    def chat(user_input):
        messages.append({"role": "user", "content": user_input})
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {"model": "deepseek-chat", "messages": messages}
        response = requests.post(URL, headers=headers, json=data)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply

    return chat

# 创建不同人格的机器人
teacher = create_bot("你是一位耐心的小学数学老师，总是用生活中的例子来解释概念")
friend = create_bot("你是一个爱讲冷笑话的好朋友，聊天很轻松")

print("老师：", teacher("什么是分数？"))
print()
print("朋友：", friend("我今天好无聊啊"))
```

## 对话历史是关键

```
messages = [
    system:  "你是..."          ← 人设
    user:    "你好"             ← 第1轮
    assistant: "你好！..."      ← 第1轮回复
    user:    "帮我写首诗"       ← 第2轮
    assistant: "好的，..."      ← 第2轮回复
]
```

每次调用 API 都把**完整的 messages 列表**发过去，AI 就能"记住"之前的对话。

## 练习

试试自己设计一个 AI 人格，让它和你进行 5 轮对话：
1. 设定一个有趣的 system 消息
2. 用 while 循环实现连续对话
3. 输入"退出"时显示对话总结
