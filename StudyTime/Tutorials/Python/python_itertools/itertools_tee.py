"""

This iterator splits the container into a number of iterators mentioned in the argument.

"""

import itertools
 
# initializing list
li = [2, 4, 6, 7, 8, 10, 20]
 
# storing list in iterator
iti = iter(li)
 
# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)
 
# printing the values of iterators
print("The iterators are : ")
for i in range(0, 3):
    print(list(it[i]))


# The iterators are : 
# [2, 4, 6, 7, 8, 10, 20]
# [2, 4, 6, 7, 8, 10, 20]
# [2, 4, 6, 7, 8, 10, 20]