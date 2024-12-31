
# A `namedtuple` is a factory function for creating tuple subclasses with named fields.


from collections import namedtuple

# Creating a namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

# Accessing fields
print(p.x, p.y)
print(p[0] + p[1])  # Access like a regular tuple