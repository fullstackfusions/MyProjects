# Using type to create a new class dynamically
MyClass = type('MyClass', (object,), {'x': 5, 'y': 10, 'my_method': lambda self: self.x + self.y})

# Create an instance of this new class
instance = MyClass()

# Accessing attributes and method
print(instance.x)  # 5
print(instance.y)  # 10
print(instance.my_method())  # 15