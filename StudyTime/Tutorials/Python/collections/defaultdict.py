"""

A `defaultdict` works exactly like a regular dictionary, but it is initialized with a function (`default_factory`) that takes no arguments and provides the default value for a nonexistent key.


"""

from collections import defaultdict

# Creating a defaultdict with default type list
dd = defaultdict(list)

# Adding elements
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['cats'].append('Mr Whiskers')

print("Dogs:", dd['dogs'])
print("Cats:", dd['cats'])