"""

This iterator starts printing the characters only after the func. in argument returns false for the first time.

"""

import itertools
 
 
# initializing list  
li = [2, 4, 5, 7, 8] 
   
# using dropwhile() to start displaying after condition is false 
print ("The values after condition returns false : ", end ="") 
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li))) 

# The values after condition returns false : [5, 7, 8]