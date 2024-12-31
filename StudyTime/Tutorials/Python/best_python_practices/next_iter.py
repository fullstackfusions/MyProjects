# Using iter and next
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2

# Handling StopIteration
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("Reached the end of the iterator.")
