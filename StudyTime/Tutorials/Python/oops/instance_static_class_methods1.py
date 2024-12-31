class MyClass:
    class_variable = "I am a class variable"  # Class variable

    def __init__(self, value):
        self.instance_variable = value  # Instance variable

    def instance_method(self):
        return f"Instance method called, {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"Class method called, {cls.class_variable}"

    @staticmethod
    def static_method():
        return "Static method called"

# Creating an instance of MyClass
obj = MyClass("I am an instance variable")

print(obj.instance_method())  # Accessing instance method
print(MyClass.class_method())  # Accessing class method
print(MyClass.static_method())  # Accessing static method