
import math
class shape:
    def area(self):
        return "NotImplementedError"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        area = length * width


class Circle:
    def __init__(self, radius):
        self.radius = radius
        # area = π * radius²
