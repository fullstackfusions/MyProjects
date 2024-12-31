class Car:
    def __init__(self):
        self.__fuel_level = 0   # Encapsulated attribute
        self.__speed = 0        # Encapsulated attribute

    def add_fuel(self, amount):
        if amount > 0:
            self.__fuel_level += amount
            print(f"Added {amount} units of fuel. Current fuel level: {self.__fuel_level}")

    def drive(self):
        if self.__fuel_level > 0:
            self.__speed = 60
            self.__fuel_level -= 1
            print(f"Driving. Speed: {self.__speed} km/h, Fuel level: {self.__fuel_level}")
        else:
            print("Cannot drive. No fuel.")

    def stop(self):
        self.__speed = 0
        print(f"Car stopped. Speed: {self.__speed} km/h")

    def get_fuel_level(self):
        return self.__fuel_level

    def get_speed(self):
        return self.__speed

# Using the Car class
my_car = Car()
my_car.add_fuel(10)       # Add fuel to the car
my_car.drive()            # Drive the car
my_car.stop()             # Stop the car
print("Fuel Level:", my_car.get_fuel_level())  # Check fuel level
print("Speed:", my_car.get_speed())            # Check speed