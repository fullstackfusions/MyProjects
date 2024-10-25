"""

This function is used to print all the values in iterable targets one after another mentioned in its arguments.

"""
import itertools
 
# initializing list 1
li1 = [1, 4, 5, 7]
 
# initializing list 2
li2 = [1, 6, 5, 9]
 
# initializing list 3
li3 = [8, 10, 5, 4]
 
# using chain() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain(li1, li2, li3)))


# All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]