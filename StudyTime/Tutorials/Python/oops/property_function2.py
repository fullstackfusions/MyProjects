from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @property
    def area(self):
        return math.pi * self._radius ** 2

    def __init__(self, radius):
        self._radius = radius

class Circle(Shape):
    pass  # No need to define the area property, it's inherited

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(0)  # Circles don't have a length or width

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Accessing the area property for both shapes
print(f"Circle Area: {circle.area:.2f}")
print(f"Rectangle Area: {rectangle.area:.2f}")