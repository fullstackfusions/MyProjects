from collections import UserList

class MyList(UserList):
    def append(self, item):
        if not isinstance(item, int):
            raise ValueError("Only integers are allowed")
        super().append(item)

# Example usage
my_list = MyList([1, 2, 3])
my_list.append(4)
print(my_list)

try:
    my_list.append("not an integer")  # This should raise an error
except ValueError as e:
    print(e)
