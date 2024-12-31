import itertools
 
# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")

# 5 10 15 20 25 30