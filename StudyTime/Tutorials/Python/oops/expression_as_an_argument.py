"""

function as an argument

Benefits
- Flexibility: Passing functions as arguments allows for creating more generic and reusable code.
- Functional Programming: This is a key concept in functional programming, enabling operations like map, reduce, and filter.
- Customization: It allows the behavior of a function to be extended or customized without modifying its internal code.

"""


def square(x):
    return x * x

numbers = [1,2,3,4,5]

# Using 'map' to apply a function to each item in a list
squared_numbers = list(map(square, numbers))

# Using 'filter' to filter a list based on a function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print(even_numbers)     # Output: [2, 4]