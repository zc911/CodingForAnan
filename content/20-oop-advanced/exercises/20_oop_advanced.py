# 第20课练习：继承与多态

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def show(self):
        print(f"{self.name}，面积 = {self.area():.2f}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("长方形")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 8)]
for s in shapes:
    s.show()
