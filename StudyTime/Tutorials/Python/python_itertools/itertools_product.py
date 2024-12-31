"""

The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.


This tool computes the cartesian product of input iterables. To compute the product of an iterable with itself, we use the optional repeat keyword argument to specify the number of repetitions. The output of this function is tuples in sorted order.

"""


from itertools import product
 
print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()
 
print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()
 
print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# Output:
# The cartesian product using repeat:
# [(1, 1), (1, 2), (2, 1), (2, 2)]

# The cartesian product of the containers:
# [('geeks', '2'), ('for', '2'), ('geeks', '2')]

# The cartesian product of the containers:
# [('A', 3), ('A', 4), ('B', 3), ('B', 4)]