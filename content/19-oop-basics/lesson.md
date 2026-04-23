# 第19课：面向对象基础：类与对象

## 从字典到类

之前用字典存宠物的信息：

```python demo title="用字典存宠物"
cat = {"name": "小橘", "age": 2, "mood": "开心"}
print(cat["name"], "今年", cat["age"], "岁，心情", cat["mood"])
```

字典只能存数据。如果宠物还能**做事**（吃饭、说话）呢？用**类（class）**！

> 🖥️ **计算机小知识**
>
> 为什么要发明"类"和"对象"？这背后是一个重要的设计思想：**抽象**。
>
> 你不需要知道手机里面怎么工作，只要知道按电源键能开机——这就是抽象，隐藏复杂细节，只暴露简单的接口。
>
> 编程也是一样：早期的程序是一大堆指令堆在一起（**过程式编程**），后来人们发现把相关的数据和操作包在一起会更好管理——这就是**面向对象编程（OOP）**。类把数据"封装"起来，外部只需要调用方法，不需要知道内部怎么实现。

## 设计一个 Pet 类

**类**是设计图纸，**对象**是按图纸造出来的实体：

```python demo title="第一个类：Pet"
class Pet:
    def __init__(self, name, age):
        self.name = name      # 属性：名字
        self.age = age        # 属性：年龄
        self.mood = "开心"    # 属性：心情
        self.hunger = 50      # 属性：饥饿度（0-100）

    def speak(self):
        print(f"{self.name}：你好！我今年{self.age}岁，心情{self.mood}！")

    def eat(self, food):
        self.hunger = max(0, self.hunger - 30)
        self.mood = "满足"
        print(f"{self.name}吃了{food}，好满足！饥饿度：{self.hunger}")

    def play(self):
        self.hunger = min(100, self.hunger + 10)
        self.mood = "兴奋"
        print(f"{self.name}玩得好开心！饥饿度：{self.hunger}")

# 创建宠物对象
my_cat = Pet("小橘", 2)
my_dog = Pet("旺财", 3)

my_cat.speak()
my_cat.eat("小鱼干")
my_cat.play()
print()
my_dog.speak()
my_dog.eat("骨头")
```

## `__init__` 和 `self`

| 概念 | 说明 |
|------|------|
| `class Pet:` | 定义一个类，名字用大驼峰 |
| `__init__` | 创建对象时自动调用的初始化方法 |
| `self` | 指向对象自身，类似"我" |
| `self.name` | 对象的属性，每个对象各有一份 |

## 同一个类，不同的对象

```python demo title="每只宠物都是独立的"
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mood = "开心"

    def speak(self):
        print(f"{self.name}：我{self.age}岁，心情{self.mood}！")

cat1 = Pet("小橘", 2)
cat2 = Pet("花花", 1)

cat1.mood = "困了"
cat1.speak()  # 小橘的状态
cat2.speak()  # 花花的状态不受影响
```

## 练习

```python exercise title="设计你的 Student 类"
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = []

    def add_score(self, subject, score):
        self.scores.append({"subject": subject, "score": score})
        print(f"{self.name}的{subject}成绩{score}分已记录")

    def show_info(self):
        print(f"=== {self.name}（{self.grade}）===")
        for item in self.scores:
            print(f"  {item['subject']}：{item['score']}分")
        if self.scores:
            avg = sum(s['score'] for s in self.scores) / len(self.scores)
            print(f"  平均分：{avg:.1f}")

# 试试看
me = Student("Anan", "三年级")
me.add_score("语文", 95)
me.add_score("数学", 88)
me.add_score("英语", 92)
me.show_info()
```
