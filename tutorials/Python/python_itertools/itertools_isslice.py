"""

This iterator selectively prints the values mentioned in its iterable container passed as argument. This iterator takes 4 arguments, iterable container, starting pos., ending position and step.

"""

import itertools 
   
# initializing list  
li = [2, 4, 5, 7, 8, 10, 20] 
     
# using islice() to slice the list acc. to need 
# starts printing from 2nd index till 6th skipping 2 
print ("The sliced list values are : ", end ="") 
print (list(itertools.islice(li, 1, 6, 2))) 

# The sliced list values are : [4, 7, 10]