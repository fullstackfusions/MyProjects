"""

super().__init__() is required when you have inherited class and you need to access super/parent class's constructor items

"""

# parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)

obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()