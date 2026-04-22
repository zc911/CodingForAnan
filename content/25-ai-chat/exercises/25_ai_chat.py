# 第25课练习：AI 对话机器人
# 在 Thonny 里运行！

import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

# 挑战：做一个"AI 翻译官"
messages = [
    {"role": "system", "content": "你是一个翻译官。用户输入中文，你翻译成英文；用户输入英文，你翻译成中文。只输出翻译结果，不要解释。"}
]

print("🌍 AI 翻译官（输入 '退出' 结束）")
print("=" * 40)

while True:
    text = input("输入：")
    if text.strip() in ["退出", "exit"]:
        break

    messages.append({"role": "user", "content": text})
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"model": "deepseek-chat", "messages": messages}
    response = requests.post(URL, headers=headers, json=data)
    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print(f"翻译：{reply}\n")
