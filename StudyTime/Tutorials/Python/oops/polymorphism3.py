class Bird:
    def speak(self):
        print("Chirp!")

class Dog:
    def speak(self):
        print("Bark!")

def make_sound(animal):
    animal.speak()

# Create instances of Bird and Dog
bird = Bird()
dog = Dog()

# Call make_sound on both objects
make_sound(bird)  # Outputs: Chirp!
make_sound(dog)   # Outputs: Bark!