"""

The recursive generators that are used to simplify combinatorial constructs such as permutations, combinations, and Cartesian products are called combinatoric iterators.

This iterator prints all the possible combinations(without replacement) of the container passed in arguments in the specified group size in sorted order.

"""


from itertools import combinations 

print ("All the combination of list in sorted order(without replacement) is:") 
print(list(combinations(['A', 2], 2))) 
print() 

print ("All the combination of string in sorted order(without replacement) is:") 
print(list(combinations('AB', 2))) 
print() 

print ("All the combination of list in sorted order(without replacement) is:") 
print(list(combinations(range(2), 1))) 


# Output:
# All the combination of list in sorted order(without replacement) is:
# [('A', 2)]

# All the combination of string in sorted order(without replacement) is:
# [('A', 'B')]

# All the combination of list in sorted order(without replacement) is:
# [(0, ), (1, )]