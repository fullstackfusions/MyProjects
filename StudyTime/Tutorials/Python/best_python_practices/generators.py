# Processing a Large Range of Numbers
def large_number_range(limit):
    """A generator that yields a large range of numbers.
    It's a substitute for a large dataset."""
    for i in range(limit):
        yield i

def squared_numbers(numbers):
    """A generator pipeline stage that yields squared numbers."""
    for n in numbers:
        yield n ** 2

def even_numbers(numbers):
    """A generator pipeline stage that yields even numbers."""
    for n in numbers:
        if n % 2 == 0:
            yield n

# Usage
limit = 1000000  # Can be a very large number
numbers = large_number_range(limit)
squared = squared_numbers(numbers)
evens = even_numbers(squared)

for i, number in enumerate(evens):
    if i >= 10:  # Limit output for demonstration
        break
    print(number)

# Note: The entire dataset is never fully loaded into memory.
