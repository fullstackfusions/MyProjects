class Animal:
    def __init__(self, species, num_legs):
        self.species = species
        self.num_legs = num_legs

    def clone(self):
        # Creates a new instance of the same class with the same attributes
        return self.__class__(self.species, self.num_legs)

# Usage
dog = Animal("Dog", 4)
new_dog = dog.clone()
