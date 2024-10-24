class ExampleClass:
    counter = 0  # Class variable

    def __init__(self, value):
        self._value = value
        ExampleClass.counter += 1

    @property
    def value(self):
        """Property to get the value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Property to set the value."""
        self._value = new_value

    @staticmethod
    def static_method():
        """Static method that does not take instance or class as the first parameter."""
        return "This is a static method"

    @classmethod
    def class_method(cls):
        """Class method that takes the class as the first parameter."""
        return f"This is a class method. {cls.counter} instances have been created."

# Usage
obj = ExampleClass(10)
print(obj.value)              # Accessing property (getter)

obj.value = 20                # Modifying property (setter)
print(obj.value)

print(ExampleClass.static_method())  # Calling static method

obj2 = ExampleClass(30)
print(ExampleClass.class_method())   # Calling class method