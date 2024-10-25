"""

The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.

Permutations() as the name speaks for itself is used to generate all possible permutations of an iterable. All elements are treated as unique based on their position and not their values. This function takes an iterable and group_size, if the value of group_size is not specified or is equal to None then the value of group_size becomes the length of the iterable.

"""

from itertools import permutations
 
print("All the permutations of the given list is:")
print(list(permutations([1, 'geeks'], 2)))
print()
 
print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()
 
print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))


# Output:
# All the permutations of the given list is:
# [(1, 'geeks'), ('geeks', 1)]

# All the permutations of the given string is:
# [('A', 'B'), ('B', 'A')]

# All the permutations of the given container is:
# [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]