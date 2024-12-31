"""

class as an argument

Benefits and Use Cases
- Flexibility: Passing classes as arguments allows for more flexible and reusable code.
- Factory Pattern: Common in implementing factory design patterns where the creation logic of objects is encapsulated.
- Dependency Injection: Useful in scenarios like dependency injection, where objects are created dynamically based on runtime requirements.

"""

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(AnimalClass):
    return AnimalClass()

# Usage
dog = animal_factory(Dog)
cat = animal_factory(Cat)

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!