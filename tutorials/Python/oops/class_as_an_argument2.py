"""

class as an argument

Benefits and Use Cases
- Flexibility: Passing classes as arguments allows for more flexible and reusable code.
- Factory Pattern: Common in implementing factory design patterns where the creation logic of objects is encapsulated.
- Dependency Injection: Useful in scenarios like dependency injection, where objects are created dynamically based on runtime requirements.

"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

def compute_area(ShapeClass, dimension):
    shape = ShapeClass(dimension)
    return shape.area()

# Usage
circle_area = compute_area(Circle, 5)
square_area = compute_area(Square, 4)

print(circle_area)  # Output: 78.5
print(square_area)  # Output: 16
