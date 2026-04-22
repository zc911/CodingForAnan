# 项目四：宠物世界
# 在 Thonny 里运行！
# 在这里完善你的宠物世界——加更多功能和宠物种类！

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
            print(f"  🎉 {self.name}升级了！Lv.{self.level}！")

    def status(self):
        print(f"  [{self.species}] {self.name} Lv.{self.level}")
        print(f"  饥饿:{self.hunger} 心情:{self.happiness}")
        self.speak()

# TODO: 添加更多宠物种类
# TODO: 添加"看病"功能
# TODO: 添加"交朋友"功能
