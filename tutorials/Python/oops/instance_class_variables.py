class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Daisy", "Golden Retriever")

print(f"{dog1.name} is a {dog1.breed} ({dog1.species})")
print(f"{dog2.name} is a {dog2.breed} ({dog2.species})")