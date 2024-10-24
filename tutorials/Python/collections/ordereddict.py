"""

An `OrderedDict` is a dictionary subclass that remembers the order in which its contents are added. (Note: From Python 3.7, regular `dict` types also maintain insertion order by default.)

"""

from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['banana'] = 3
ordered_dict['apple'] = 4
ordered_dict['pear'] = 1

# Iterating in order of insertion
for key, value in ordered_dict.items():
    print(key, value)