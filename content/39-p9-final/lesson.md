# 第39课：🚀 项目九：自选终极大作

## 你的终极项目！

恭喜你走到了最后一课！🎉 现在是时候用你学过的所有技能，完成一个**属于自己的项目**。

下面有三个方向，选一个你最感兴趣的——或者自己想一个！

## 方向一：命令行 RPG 游戏

做一个文字冒险游戏！玩家在命令行里探索世界、打怪升级。

**技术要点：**
- 类与对象：Player、Monster、Item
- 随机事件：random 模块
- 存档系统：JSON 保存/加载游戏进度
- 命令行参数：argparse 选择新游戏/继续

**设计思路：**
```python thonny title="RPG 游戏框架"
import json
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"🧙 {self.name} | HP: {self.hp} | 攻击: {self.attack} | 金币: {self.gold}")
        if self.inventory:
            print(f"   背包：{', '.join(self.inventory)}")

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

def battle(player, monster):
    print(f"\n⚔️ 遭遇了 {monster.name}！")
    while player.is_alive() and monster.is_alive():
        monster.hp -= player.attack
        print(f"  你攻击了 {monster.name}，造成 {player.attack} 伤害")
        if monster.is_alive():
            player.hp -= monster.attack
            print(f"  {monster.name} 攻击了你，造成 {monster.attack} 伤害")

    if player.is_alive():
        reward = random.randint(5, 20)
        player.gold += reward
        print(f"  🎉 你赢了！获得 {reward} 金币")
    else:
        print("  💀 你被击败了...")

# 快速演示
hero = Player("Anan")
hero.show_status()

goblin = Monster("小恶魔", 20, 5)
battle(hero, goblin)
hero.show_status()
```

**扩展方向：**
- 多个地图房间，用字典存储
- 装备系统：武器增加攻击力
- 商店：用金币购买物品
- 用 @log 装饰器记录战斗日志

## 方向二：文件分析工具

做一个分析文本文件的工具——统计字数、找最常用词、生成报告。

**技术要点：**
- 文件读写：os、pathlib
- 正则表达式：提取单词、过滤标点
- 数据可视化：matplotlib 画词频图
- argparse：选择分析模式和文件路径

**设计思路：**
```python thonny title="文件分析框架"
import re
from pathlib import Path
from collections import Counter

def analyze_text(filepath):
    """分析文本文件"""
    content = Path(filepath).read_text(encoding="utf-8")

    # 基本统计
    chars = len(content)
    lines = content.count("\n") + 1

    # 提取中文词和英文词
    chinese_chars = re.findall(r"[一-鿿]", content)
    english_words = re.findall(r"[a-zA-Z]+", content.lower())

    # 词频统计
    cn_freq = Counter(chinese_chars).most_common(10)
    en_freq = Counter(english_words).most_common(10)

    print(f"📄 文件：{filepath}")
    print(f"📏 字符数：{chars}")
    print(f"📝 行数：{lines}")
    print(f"🇨🇳 中文高频字：{cn_freq}")
    print(f"🇺🇸 英文高频词：{en_freq}")

# 创建示例文件并分析
Path("sample.txt").write_text(
    "Python is fun! Python is great!\n学习Python很有趣。\n编程让世界更美好。",
    encoding="utf-8"
)
analyze_text("sample.txt")
```

**扩展方向：**
- 生成 HTML 报告
- 支持批量分析整个文件夹
- 用 matplotlib 画词频柱状图
- 支持导出分析结果为 JSON

## 方向三：网络爬虫 + 数据可视化

做一个从网上获取数据并可视化的工具。

**技术要点：**
- requests：获取网页/API 数据
- JSON 解析：提取有用信息
- matplotlib：数据可视化
- argparse + 自定义异常

**设计思路：**
```python thonny title="API 数据获取框架"
import json
import random
from collections import Counter

# 模拟 API 数据（实际需要 requests 调用真实 API）
mock_weather = {
    "city": "北京",
    "forecast": [
        {"date": "04-20", "temp": 22, "weather": "晴"},
        {"date": "04-21", "temp": 19, "weather": "多云"},
        {"date": "04-22", "temp": 25, "weather": "晴"},
        {"date": "04-23", "temp": 21, "weather": "小雨"},
        {"date": "04-24", "temp": 23, "weather": "晴"},
    ]
}

def analyze_weather(data):
    temps = [day["temp"] for day in data["forecast"]]
    print(f"🌤️ {data['city']} 天气分析：")
    print(f"  平均温度：{sum(temps)/len(temps):.1f}°C")
    print(f"  最高温度：{max(temps)}°C")
    print(f"  最低温度：{min(temps)}°C")

    weather_count = Counter(day["weather"] for day in data["forecast"])
    print(f"  天气分布：{dict(weather_count)}")

analyze_weather(mock_weather)
```

> **注意：** 真实的网络请求需要在 Thonny 中运行，先 `pip install requests`。

**扩展方向：**
- 用 matplotlib 画温度折线图
- 支持多个城市对比
- 数据缓存到本地 JSON 文件
- 添加 @retry 装饰器处理网络错误

## 开工吧！

选定方向后，按这个流程来：

1. 📋 **需求分析**——写下你的程序要做什么（5-8条）
2. 🏗️ **设计**——需要哪些类/函数？数据怎么存？
3. 🔨 **分步实现**——先做最小版本，再慢慢加功能
4. 🧪 **测试**——每个功能都试试，确保没有 bug
5. ✨ **扩展**——加上额外功能，让它更酷

记住：**先让它跑起来，再让它跑得好！** 不用追求完美，第一版能运行就是胜利！🚀