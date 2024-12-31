
from collections import UserString

class MyString(UserString):
    def reverse(self):
        return self.data[::-1]

# Example usage
my_string = MyString("Hello")
print("Original:", my_string)
print("Reversed:", my_string.reverse())