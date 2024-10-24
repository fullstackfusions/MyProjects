from abc import ABC, abstractmethod

# create abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# Implement the class out of abstract class
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

    def drive(self):
        print("Car is moving.")

# In subclass you will call this functions.
my_car = Car()
my_car.start_engine()  # Outputs: Car engine started.
my_car.drive()         # Outputs: Car is moving.
my_car.stop_engine()   # Outputs: Car engine stopped.