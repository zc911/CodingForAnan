# 第20课：面向对象进阶：继承与多态

## 猫和狗都是宠物

上节课我们做了 Pet 类。现在想让猫"喵喵"叫、狗"汪汪"叫——它们都是宠物，但叫声不同。

**继承**就是"子类继承父类，然后加上自己的特色"：

```python demo title="继承：Dog 和 Cat 继承 Pet"
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mood = "开心"

    def speak(self):
        print(f"{self.name}发出了声音")

    def show_info(self):
        print(f"{self.name}，{self.age}岁，心情{self.mood}")


class Dog(Pet):          # Dog 继承 Pet
    def speak(self):     # 重写 speak 方法
        print(f"{self.name}：汪汪！🐕")

    def fetch(self):     # Dog 特有方法
        self.mood = "兴奋"
        print(f"{self.name}去捡球了，好开心！")


class Cat(Pet):          # Cat 继承 Pet
    def speak(self):     # 重写 speak 方法
        print(f"{self.name}：喵～🐱")

    def purr(self):      # Cat 特有方法
        self.mood = "满足"
        print(f"{self.name}在咕噜咕噜～")


wangcai = Dog("旺财", 3)
xiaojv = Cat("小橘", 2)

wangcai.speak()      # 汪汪！
wangcai.fetch()
xiaojv.speak()       # 喵～
xiaojv.purr()

# 继承来的方法也能用
wangcai.show_info()
xiaojv.show_info()
```

## 继承的关键概念

| 概念 | 说明 |
|------|------|
| `class Dog(Pet):` | Dog 继承 Pet，拥有 Pet 的所有属性和方法 |
| 重写（override） | 子类重新定义父类的方法，如 `speak()` |
| 特有方法 | 子类可以加父类没有的方法，如 `fetch()` |
| 多态 | 同一个方法名，不同对象有不同的行为 |

## 多态：同一个命令，不同表现

```python demo title="多态：让所有宠物都叫"
class Pet:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}：...")

class Dog(Pet):
    def speak(self):
        print(f"{self.name}：汪汪！🐕")

class Cat(Pet):
    def speak(self):
        print(f"{self.name}：喵～🐱")

class Bird(Pet):
    def speak(self):
        print(f"{self.name}：叽叽！🐦")

# 同一个方法，不同表现——这就是多态
pets = [Dog("旺财"), Cat("小橘"), Bird("皮皮"), Cat("花花")]

print("=== 宠物合唱 ===")
for pet in pets:
    pet.speak()    # 都调 speak()，但各有各的叫声
```

## 练习

```python exercise title="设计一个动物园"
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name}：{self.sound}！")

    def show(self):
        print(f"我是{self.name}，我叫起来{self.sound}")

# 创建你的动物园
animals = [
    Animal("狮子", "吼"),
    Animal("猴子", "吱吱"),
    Animal("青蛙", "呱呱"),
    Animal("小羊", "咩"),
]

print("=== 动物园巡游 ===")
for animal in animals:
    animal.show()
    animal.speak()
    print()
```
