# 第24课：AI 是什么？大模型初体验

## 人工智能就在身边

你用过这些吗？
- 手机语音助手（Siri、小爱同学）
- 翻译软件
- 推荐你看什么视频的算法

这些都是**人工智能（AI）** 的应用！

## 大语言模型是什么？

**大语言模型（LLM）** 是一种 AI，它读过互联网上几乎所有的文字，学会了"猜下一个字"。

就像你写作文时，写了"今天天气很"，下一个字大概率是"好"或"差"。大模型就是把这个"猜下一个字"做到极致。

## 和 AI 说第一句话

> **准备工作：**
> 1. 在 Thonny 里安装 requests：`pip install requests`
> 2. 获取一个免费的 API key：
>    - 打开 https://platform.deepseek.com 注册账号
>    - 进入"API Keys"页面，创建一个 key
>    - 把 key 复制下来（只显示一次！）
> 3. 在代码里把 `你的API_KEY` 替换成你的 key

```python thonny title="第一次和 AI 对话"
import requests
import json

API_KEY = "你的API_KEY"    # ← 替换成你的 key
URL = "https://api.deepseek.com/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "你好！请用一句话介绍你自己"}
    ]
}

response = requests.post(URL, headers=headers, json=data)
result = response.json()

print("AI 说：")
print(result["choices"][0]["message"]["content"])
```

## API 调用是怎么回事？

调用 AI 的 API 就像发微信消息：

1. **你（客户端）**：发一条消息给 AI
2. **AI 服务器**：读完消息，思考，写回复
3. **AI 服务器**：把回复发回给你
4. **你**：收到回复，显示出来

```
你 → "你好" → AI 服务器 → "你好！有什么可以帮你的？" → 你
```

## 消息格式

AI 的对话用 JSON 格式传递，每条消息有**角色**：

| 角色 | 说明 |
|------|------|
| `system` | 系统提示，告诉 AI 怎么表现（可选） |
| `user` | 用户说的话 |
| `assistant` | AI 说的话 |

```python thonny title="给 AI 设定角色"
import requests
import json

API_KEY = "你的API_KEY"
URL = "https://api.deepseek.com/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是一个友好的小学老师，说话简单有趣，喜欢用emoji"},
        {"role": "user", "content": "什么是变量？"}
    ]
}

response = requests.post(URL, headers=headers, json=data)
result = response.json()

print("AI 老师说：")
print(result["choices"][0]["message"]["content"])
```

## 练习

试着修改 system 消息，让 AI 变成不同的角色：
- 一个严厉的老师
- 一个爱讲冷笑话的朋友
- 一个古代诗人
