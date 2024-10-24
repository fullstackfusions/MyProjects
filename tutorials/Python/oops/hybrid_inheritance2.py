# Base class
class Animal:
    def eat(self):
        return "Eating..."

# Intermediate class
class Mammal(Animal):
    def walk(self):
        return "Walking..."

# Another base class
class Bird(Animal):
    def fly(self):
        return "Flying..."

# Child class derived from Mammal and Bird (Multiple Inheritance)
class Bat(Mammal, Bird):
    def use_sonar(self):
        return "Using sonar..."

# Example usage
bat = Bat()
print(bat.eat())        # Inherited from Animal
print(bat.walk())       # Inherited from Mammal
print(bat.fly())        # Inherited from Bird
print(bat.use_sonar())  # Defined in Bat