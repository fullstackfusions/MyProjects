# add, subtract, multiply, and divide are instance methods.
# They modify the state of the instance (self.value).
class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, amount):
        """Add amount to the value."""
        self.value += amount
        return self.value

    def subtract(self, amount):
        """Subtract amount from the value."""
        self.value -= amount
        return self.value

    def multiply(self, amount):
        """Multiply the value by the amount."""
        self.value *= amount
        return self.value

    def divide(self, amount):
        """Divide the value by the amount."""
        if amount != 0:
            self.value /= amount
            return self.value
        else:
            return "Division by zero error"

# Example Usage
calc = Calculator(10)
print(calc.add(5))      # 15
print(calc.subtract(3)) # 12
print(calc.multiply(2)) # 24
print(calc.divide(4))   # 6.0
print(calc.divide(0))   # Division by zero error