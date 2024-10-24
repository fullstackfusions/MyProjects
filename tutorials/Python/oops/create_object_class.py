# without type, or normally define class from object
class MyClass(object):
    x = 5
    y = 10

    def my_method(self):
        return self.x + self.y

# Create an instance of this class
instance = MyClass()

# Accessing attributes and method
print(instance.x)  # 5
print(instance.y)  # 10
print(instance.my_method())  # 15

# Note: Here MyClass(object) is same as MyClass