# doc typing - polymorphism
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('도형의 면적을 출력합니다')

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y,radius)
        self.height = height

    def get_area(self):  # get_volume
        # return math.pi * self.radius * self.radius * self.height # 이 공식 중 math.pi * self.radius * self.radius는 이미 있으므로 가져다 쓰면 된다.
        return super().get_area() * self.height

class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f'사각형의 좌표는 x:{self.x}, y:{self.y}이고 넓이는 {self.get_area()}'

    def __add__(self, other):
        # return (self.width * self.length) + (other.width * other.length)  # 두 사각형 넓이의 합
        return Rectangle(0, 0, (self.width + other.width), (self.length + other.length))  # 각 사각형의 가로의 합과 세로의 합의 곱

cy1 = Cylinder(20, 20, 10.0, 2)
c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70, 30, 10, 15)

print(r1.get_area())
print(c1.get_area())
print(c2.get_area())
print(f'사각형의 좌표는 x:{r1.x}, y:{r1.y}이고 넓이는 {r1.get_area()}')
print(cy1.get_area())
print(r1)  # 매직함수 안쪽에 원하는 서식을 넣고 해당 객체가 등장하면 그 포맷대로 출력되게 해줌.
print(r2)
print(r1 + r2)

# 만일 원기둥 만들시는 circle을 상속받는것이 좋다 >> 타고 올라가서 Shape도 상속 받을 수 있고 부피, 면적을 구할 때 circle의 면적을 사용할수도 있기 때문
