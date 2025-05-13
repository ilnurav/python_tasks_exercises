'''
Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. Дополнительно к работоспособности оценим:

Юнит-тесты
Легкость добавления других фигур
Вычисление площади фигуры без знания типа фигуры в compile-time
Проверку на то, является ли треугольник прямоугольным
'''

import math
from abc import ABC, abstractmethod
from typing import Union, Tuple

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        sides.sort()
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Triangle inequality violated")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self, tolerance: float = 1e-6) -> bool:
        sides = [self.a, self.b, self.c]
        sides.sort()
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance

def calculate_area(shape: Shape) -> float:
    return shape.area()

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
