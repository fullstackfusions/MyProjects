"""

class method with @classmethod

- Class Method: class_method can access and modify class state. It takes cls as the first parameter.
- Factory Methods: Class methods are often used as factory methods, which can create class instances in different ways.
- Accessing Class State: Use class methods when you need to access or modify the class state, which is shared among all instances.
- Alternative Constructors: They are used to provide additional ways to create objects besides the standard __init__ method.

"""

class Person:
    count = 0  # Class variable to count the number of instances

    def __init__(self, name):
        self.name = name  # Instance variable
        Person.count += 1  # Increment the count when a new instance is created

    @classmethod
    def get_instance_count(cls):
        return cls.count

# Creating instances
person1 = Person("Alice")
person2 = Person("Bob")

count = Person.get_instance_count()     # shared among all instances
print(count)  # Output: 2 (retrieved using the class method)