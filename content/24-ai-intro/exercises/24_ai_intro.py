# 第24课练习：AI 初体验
# 在 Thonny 里运行！
# 记得替换 API_KEY

import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

def ask_ai(system_prompt, user_message):
    """调用 AI API 并返回回复"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post(URL, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]

# 试试不同角色
roles = [
    ("你是一个幽默的科学家", "用一句话解释什么是重力"),
    ("你是一个古代诗人", "写一句关于春天的五言诗"),
    ("你是一个宠物猫", "用猫的语气打个招呼"),
]

for system, user in roles:
    print(f"问：{user}")
    print(f"答：{ask_ai(system, user)}")
    print()
