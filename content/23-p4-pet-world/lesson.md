# 🐾 项目四：宠物世界

恭喜完成阶段五！现在用学过的 **类、继承、列表推导式** 做一个养宠物模拟器。

## 功能设计

1. 可以创建不同种类的宠物（猫、狗、鸟）
2. 每只宠物有名字、心情、饥饿度
3. 可以喂食、玩耍、训练、查看状态
4. 不同宠物叫声不同（多态）

## 先试试基础版

```python demo title="宠物世界基础版"
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50
        self.level = 1

    def speak(self):
        return "..."

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 10)
        print(f"  {self.name}吃饱了！饥饿度{self.hunger}，心情{self.happiness}")

    def play(self):
        self.hunger = min(100, self.hunger + 15)
        self.happiness = min(100, self.happiness + 20)
        print(f"  {self.name}玩得好开心！饥饿度{self.hunger}，心情{self.happiness}")

    def status(self):
        print(f"  [{self.species}] {self.name} | Lv.{self.level} | 饥饿:{self.hunger} 心情:{self.happiness}")
        self.speak()

class Dog(Pet):
    def speak(self):
        print(f"  {self.name}：汪汪！🐕")

class Cat(Pet):
    def speak(self):
        print(f"  {self.name}：喵～🐱")

# 创建宠物
pets = [Dog("旺财", "狗"), Cat("小橘", "猫")]

print("=== 🐾 宠物世界 ===")
for pet in pets:
    pet.status()
    pet.eat()
    pet.play()
    pet.status()
    print()
```

## 完整版（在 Thonny 运行）

```python thonny title="宠物世界完整版"
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50
        self.level = 1
        self.exp = 0

    def speak(self):
        print(f"  {self.name}：...")

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 10)
        self.gain_exp(10)
        print(f"  {self.name}吃饱了！")

    def play(self):
        self.hunger = min(100, self.hunger + 15)
        self.happiness = min(100, self.happiness + 20)
        self.gain_exp(15)
        print(f"  {self.name}玩得好开心！")

    def train(self):
        self.hunger = min(100, self.hunger + 20)
        self.happiness = max(0, self.happiness - 10)
        self.gain_exp(25)
        print(f"  {self.name}努力训练！")

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 50:
            self.exp = 0
            self.level += 1
            print(f"  🎉 {self.name}升级了！现在 Lv.{self.level}！")

    def status(self):
        print(f"  [{self.species}] {self.name} Lv.{self.level} (经验:{self.exp}/{self.level*50})")
        print(f"  饥饿:{self.hunger} 心情:{self.happiness}")
        self.speak()


class Dog(Pet):
    def speak(self):
        print(f"  {self.name}：汪汪！🐕")

class Cat(Pet):
    def speak(self):
        print(f"  {self.name}：喵～🐱")

class Bird(Pet):
    def speak(self):
        print(f"  {self.name}：叽叽！🐦")


# 游戏主循环
print("=" * 30)
print("🐾 欢迎来到宠物世界！")
print("=" * 30)

name = input("给你的宠物起个名字：")
species = input("选一种宠物（狗/猫/鸟）：")

if species == "狗":
    pet = Dog(name, "狗")
elif species == "猫":
    pet = Cat(name, "猫")
else:
    pet = Bird(name, "鸟")

print(f"\n你领养了一只{pet.species}：{pet.name}！\n")

while True:
    pet.status()
    print("\n1.喂食 2.玩耍 3.训练 4.退出")
    choice = input("选择：")
    if choice == "1":
        pet.eat()
    elif choice == "2":
        pet.play()
    elif choice == "3":
        pet.train()
    elif choice == "4":
        print(f"\n再见！{pet.name}会想你的！🐾")
        break
    else:
        print("  无效选择")
    print()
```

## 挑战

- 加一个"看病"功能：饥饿度太高或心情太低时提示生病
- 宠物之间可以"交朋友"
- 加入更多宠物种类（兔子、金鱼、仓鼠）
