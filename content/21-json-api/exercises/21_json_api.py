# 第21课练习：JSON 与 API

import json
import requests

# 练习1：调用 API 获取多条猫知识
print("=== 猫猫知识 × 5 ===")
response = requests.get("https://catfact.ninja/facts?limit=5")
data = response.json()
for i, fact in enumerate(data["data"], 1):
    print(f"{i}. {fact['fact']}\n")

# 练习2：保存到 JSON 文件
with open("cat_facts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("猫猫知识已保存到 cat_facts.json！")
