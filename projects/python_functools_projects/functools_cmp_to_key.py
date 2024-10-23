# This converts an old-style comparison function into a key function for sorting.

from functools import cmp_to_key

def compare(a, b):
    return (a > b) - (a < b)

numbers = [5, 3, 2, 4, 1]
sorted_numbers = sorted(numbers, key=cmp_to_key(compare))

print(sorted_numbers)  # Output: [1, 2, 3, 4, 5]
