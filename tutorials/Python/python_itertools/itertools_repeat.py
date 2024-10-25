"""

This iterator repeatedly prints the passed value an infinite number of times. If the optional keyword num is mentioned, then it repeatedly prints num number of times.

"""

import itertools
 
# using repeat() to repeatedly print number
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

# Printing the numbers repeatedly : 
# [25, 25, 25, 25]