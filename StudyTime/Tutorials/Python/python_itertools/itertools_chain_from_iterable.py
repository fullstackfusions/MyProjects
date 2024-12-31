"""

This function is implemented similarly as a chain() but the argument here is a list of lists or any other iterable container.

"""

import itertools
 
 
# initializing list 1 
li1 = [1, 4, 5, 7] 
   
# initializing list 2 
li2 = [1, 6, 5, 9] 
   
# initializing list 3 
li3 = [8, 10, 5, 4] 
   
# initializing list of list 
li4 = [li1, li2, li3] 
 
# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain.from_iterable(li4)))

# All values in mentioned chain are : [1, 4, 5, 7, 1, 6, 5, 9, 8, 10, 5, 4]