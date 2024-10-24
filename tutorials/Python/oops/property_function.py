from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def area(self):
        return self._length * self._width

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Accessing the area property for both shapes
print(f"Circle Area: {circle.area:.2f}")
print(f"Rectangle Area: {rectangle.area:.2f}")