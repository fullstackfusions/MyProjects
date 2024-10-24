# Using filter
numbers = range(-5, 5)
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))  # [1, 2, 3, 4]
