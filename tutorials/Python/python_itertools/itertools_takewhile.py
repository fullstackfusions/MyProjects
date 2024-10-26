"""

This iterator is the opposite of dropwhile(), it prints the values till the function returns false for 1st time.

"""

import itertools 
   
# initializing list  
li = [2, 4, 6, 7, 8, 10, 20] 
   
# using takewhile() to print values till condition is false. 
print ("The list values till 1st false value are : ", end ="") 
print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))


# The list values till 1st false value are : [2, 4, 6]