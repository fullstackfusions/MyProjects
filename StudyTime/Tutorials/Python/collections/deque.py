"""

A `deque` (double-ended queue) is a generalization of stacks and queues. It supports thread-safe, memory-efficient appends and pops from both sides of the deque.

"""

from collections import deque

# Creating a deque
d = deque('ghi')  # make a deque with three items

# Adding items
d.append('j')
d.appendleft('f')

# Popping items
print("Popped from right:", d.pop())
print("Popped from left:", d.popleft())

print("Deque:", d)