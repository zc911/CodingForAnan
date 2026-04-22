# 第26课练习：AI 创意工坊
# 在 Thonny 里运行！

import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

def create_session(system_prompt):
    messages = [{"role": "system", "content": system_prompt}]
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

# 挑战：AI 成语接龙
print("🐉 AI 成语接龙")
print("你和 AI 轮流说成语，后一个成语的第一个字要和前一个的最后一个字相同（同音也行）")
print("=" * 40)

bot = create_session("我们来玩成语接龙。我说一个成语，你要接一个成语，你的成语的第一个字要和我成语的最后一个字相同（同音也可以）。只输出成语，不要解释。第一个成语我来说。")

current = input("你先说一个成语：")
while True:
    ai_reply = bot(current)
    print(f"AI：{ai_reply}")
    current = input("你：")
    if current.strip() in ["退出", "不玩了"]:
        print("游戏结束！")
        break
    bot(current)  # 把你的也告诉 AI
