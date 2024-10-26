import itertools
 
l = ['Geeks', 'for', 'Geeks']
 
# defining iterator
iterators = itertools.cycle(l)
 
# for in loop
for i in range(6):
 
    # Using next function
    print(next(iterators), end=" ")

# Geeks for Geeks Geeks for Geeks 