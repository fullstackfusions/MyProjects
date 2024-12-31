import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_area(shape):
    return shape.area()

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(10, 5)

# Calculate and print areas
print("Circle Area:", calculate_area(circle))      # Outputs area of the circle
print("Rectangle Area:", calculate_area(rectangle)) # Outputs area of the rectangle