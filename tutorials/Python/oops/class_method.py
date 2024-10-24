"""

class method with @classmethod

- Class Method: class_method can access and modify class state. It takes cls as the first parameter.
- Factory Methods: Class methods are often used as factory methods, which can create class instances in different ways.
- Accessing Class State: Use class methods when you need to access or modify the class state, which is shared among all instances.
- Alternative Constructors: They are used to provide additional ways to create objects besides the standard __init__ method.

"""

class Employee:
    raise_amount = 1.04  # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        """Class method to set the raise amount for all instances."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Class method to create an instance from a string."""
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

# Usage
Employee.set_raise_amount(1.05)

emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee.from_string('Jane-Doe-60000')

emp1.apply_raise()
emp2.apply_raise()

print(emp1.pay)  # 52500
print(emp2.pay)  # 63000