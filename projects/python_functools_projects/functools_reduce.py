# This applies a function cumulatively to the items of a sequence, from left to right, to reduce the sequence to a single value.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 15
