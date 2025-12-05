# polymorphism_demo.py
import math


class Shape:
    def area(self):
        raise NotImplementedError("override subclasses")


class Rectangle(Shape):
    def __init__(self, length=0, width=0):  # default values added
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius=0):  # default value added
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
