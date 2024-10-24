from abc import ABC, abstractmethod
from typing import Any

class Shape(ABC):
    """
    Abstract base class for different geometric shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.
        """
        pass


class Rectangle(Shape):
    """
    Represents a rectangle, a subclass of Shape.
    """

    def __init__(self, length: float, width: float) -> None:
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)


# Example usage
try:
    rect = Rectangle(4, 5)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}")
except ValueError as e:
    print(f"Error: {e}")