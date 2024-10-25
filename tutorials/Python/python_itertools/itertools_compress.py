"""

This iterator selectively picks the values to print from the passed container according to the boolean list value passed as other arguments. The arguments corresponding to boolean true are printed else all are skipped.

"""


import itertools
 
 
# using compress() selectively print data values
print("The compressed values in string are : ", end="")
print(list(itertools.compress('GEEKSFORGEEKS', [
      1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

# The compressed values in string are : ['G', 'F', 'G']