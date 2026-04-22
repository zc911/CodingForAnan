# 第26课：AI 创意工坊

## AI 的超能力

AI 不只是聊天机器人——它能写诗、编故事、翻译、写代码、做数学题……关键在于你怎么**问**它。

## Prompt 技巧：怎么问 AI

**Prompt**（提示词）就是你发给 AI 的文字。问得好，答得妙！

### 技巧 1：给角色

```
普通：写一首诗
好的：你是一位唐代诗人，写一首关于秋天的五言绝句
```

### 技巧 2：给例子

```
普通：编一个谜语
好的：编一个谜语，格式像这样：
      "我有翅膀却不会飞，我在夜里亮闪闪。——答案：萤火虫"
      请编一个关于月亮的谜语
```

### 技巧 3：分步骤

```
普通：解释什么是循环
好的：请分3步解释什么是循环：
      1. 先用生活中的例子说明
      2. 再写一段简单的 Python 代码
      3. 最后出一个小练习题
```

```python exercise title="Prompt 技巧对比（在 Thonny 运行）"
import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

def ask(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(URL, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"]

# 对比：普通 vs 好的 prompt
print("=== 普通问法 ===")
print(ask("写一首诗"))
print()

print("=== 好的问法 ===")
print(ask("你是一位9岁小女孩的爸爸，也是一位诗人。请写一首简短有趣的诗，主题是'学编程'，风格轻松可爱，每行不超过10个字"))
```

## AI 创意应用

```python exercise title="AI 创意工坊（在 Thonny 运行）"
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

# 创意工坊菜单
print("🎨 AI 创意工坊")
print("=" * 30)
print("1. 📝 诗人：让 AI 写诗")
print("2. 📖 故事大王：让 AI 编故事")
print("3. 🌍 翻译官：中英互译")
print("4. 💡 代码助手：解释 Python 代码")

choice = input("\n选择（1-4）：")

if choice == "1":
    bot = create_session("你是一位有趣的现代诗人，擅长写短小精悍的诗，用词简单生动")
    topic = input("诗的主题：")
    print(bot(f"写一首关于'{topic}'的短诗，4行就好"))
elif choice == "2":
    bot = create_session("你是一位儿童故事作家，故事有趣、有教育意义，每次只推进一点点剧情")
    topic = input("故事的主题：")
    print(bot(f"开始讲一个关于'{topic}'的故事开头（50字以内）"))
elif choice == "3":
    bot = create_session("你是翻译官，用户输入中文你翻译成英文，输入英文翻译成中文，只输出翻译")
    text = input("输入要翻译的内容：")
    print(bot(text))
elif choice == "4":
    bot = create_session("你是Python编程老师，用简单易懂的方式解释代码，多用比喻")
    code = input("输入想了解的代码或概念：")
    print(bot(f"请解释：{code}"))
```

## 练习

设计你自己的 AI 应用！选择一个场景：
1. **AI 猜数字**：让 AI 出数字，你来猜
2. **AI 成语接龙**：和 AI 玩成语接龙
3. **AI 作文助手**：帮你写作文提纲
