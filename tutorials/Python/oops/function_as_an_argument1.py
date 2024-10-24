"""

function as an argument

Benefits
- Flexibility: Passing functions as arguments allows for creating more generic and reusable code.
- Functional Programming: This is a key concept in functional programming, enabling operations like map, reduce, and filter.
- Customization: It allows the behavior of a function to be extended or customized without modifying its internal code.

"""

def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply(func, x):
    # Call the function passed as an argument
    result = func(x)
    return result

# Pass the square function as an argument
result1 = apply(square, 5)
print(f"Square of 5 is {result1}")

# Pass the cube function as an argument
result2 = apply(cube, 3)
print(f"Cube of 3 is {result2}")