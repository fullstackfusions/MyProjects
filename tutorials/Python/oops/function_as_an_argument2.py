"""

function as an argument

Benefits
- Flexibility: Passing functions as arguments allows for creating more generic and reusable code.
- Functional Programming: This is a key concept in functional programming, enabling operations like map, reduce, and filter.
- Customization: It allows the behavior of a function to be extended or customized without modifying its internal code.

"""

# using built in function and passing as an argument
names = ['Alice', 'Bob', 'Charlie']
# Sort by the length of the name
names.sort(key=len)
print(names)  # Output: ['Bob', 'Alice', 'Charlie']