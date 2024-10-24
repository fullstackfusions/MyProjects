"""

A singleton is a design pattern that restricts the instantiation of a class to one single instance. This is useful when exactly one object is needed to coordinate actions across the system. In Python, a singleton can be implemented in various ways.

Example use cases:
- database connections
- configuration settings
- logging purpose to keep track of single logger
- hardware interface access
- caching
- service providers
- kafka

"""


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    def __init__(self, value):
        self.value = value

# Usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
print(singleton1 is singleton2)  # Output: True