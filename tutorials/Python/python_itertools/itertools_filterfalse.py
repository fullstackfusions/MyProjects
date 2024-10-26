"""

As the name suggests, this iterator prints only values that return false for the passed function.

"""

import itertools 
   
# initializing list  
li = [2, 4, 5, 7, 8]
 
# using filterfalse() to print false values 
print ("The values that return false to function are : ", end ="") 
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li))) 

# The values that return false to function are : [5, 7]