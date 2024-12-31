"""

static method with @staticmethod

- Static Method: static_method doesn't take a specific instance (self) or class (cls) parameter. It's like a regular function but belongs to the class's namespace.
- Utility Functions: Use static methods for utility or helper functions that could logically belong to the class but don't need access to any class or instance-specific data.
- Namespacing: Static methods provide a way to namespace our methods. They help in organizing code by keeping related methods within a class.
- Independence from Instances: Since static methods don't rely on class instances, they can be called directly on the class without creating an instance.

"""

class MathOperations:
    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers."""
        return a * b

# Usage
# Call static methods directly on the class without creating an instance
result_add = MathOperations.add(10, 5)       # 15
result_multiply = MathOperations.multiply(4, 5)  # 20

print(f"Addition: {result_add}, Multiplication: {result_multiply}")
