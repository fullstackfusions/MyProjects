"""

This iterator prints the values of iterables alternatively in sequence. If one of the iterables is printed fully, the remaining values are filled by the values assigned to fillvalue.

"""

import itertools
 
# using zip_longest() to combine two iterables.
print("The combined values of iterables is  : ")
print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))


# The combined values of iterables is  : 
# ('G', 'e') ('e', 'k') ('s', 'f') ('o', 'r') ('G', 'e') ('e', 'k') ('s', '_')