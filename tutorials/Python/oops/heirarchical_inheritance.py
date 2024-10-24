# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Further derived class from Dog
class Bulldog(Dog):
    def speak(self):
        return f"{self.name} says Woof Woof!"

# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
bulldog = Bulldog("Tank")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
print(bulldog.speak())  # Tank says Woof Woof!