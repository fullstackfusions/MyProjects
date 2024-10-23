
# This is used to fix a certain number of arguments of a function and generate a new function.

from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that always multiplies by 2
double = partial(multiply, 2)

print(double(5))  # Output: 10
