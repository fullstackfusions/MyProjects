"""

A `Counter` is a subclass of `dict` used for counting hashable objects. It’s a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

"""

from collections import Counter

# Creating a Counter from a list
counter = Counter(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])

# Count of individual element
print("Count of apples:", counter['apple'])

# Most common elements
print("Two most common fruits:", counter.most_common(2))