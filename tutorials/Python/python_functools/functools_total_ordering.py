# This class decorator makes it easier to define all rich comparison methods.

from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)

print(s1 > s2)  # Output: True
print(s1 >= s2)  # Output: True (derived from total_ordering)
