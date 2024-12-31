"""

This iterator takes a function and tuple list as argument and returns the value according to the function from each tuple of the list.

"""

import itertools 
   
   
# initializing tuple list 
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ] 
   
# using starmap() for selection value acc. to function 
# selects min of all tuple values 
print ("The values acc. to function are : ", end ="") 
print (list(itertools.starmap(min, li))) 


# The values acc. to function are : [1, 1, 4, 1]