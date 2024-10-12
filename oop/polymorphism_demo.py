
import math


class Shape:
    def area(self):
        return "NotImplementedError"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        area = length * width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # area = π * radius²
