# 项目五选项A：AI 小助手
# 在 Thonny 里运行！

import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

messages = [
    {"role": "system", "content": "你是一个全能学习助手，可以回答问题、写诗、翻译、讲笑话、解释代码。"}
]

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

# TODO: 加上保存对话记录到文件的功能
# TODO: 加上加载不同人格的功能
# TODO: 加上统计对话次数的功能

print("🤖 AI 小助手")
while True:
    user_input = input("你：")
    if user_input.strip() in ["退出", "exit"]:
        break
    print(f"AI：{chat(user_input)}\n")
