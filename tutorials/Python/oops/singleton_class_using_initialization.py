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


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, value):
        if not self.__initialized:
            self.value = value
            self.__initialized = True

# Usage
singleton1 = Singleton(10)
singleton2 = Singleton(20)

print(singleton1.value)  # Output: 10
print(singleton2.value)  # Output: 10
print(singleton1 is singleton2)  # Output: True