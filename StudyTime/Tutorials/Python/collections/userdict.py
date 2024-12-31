from collections import UserDict

class MyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.add_count = {}
        super().__init__(*args, **kwargs)
        for key in self.data:
            self.add_count[key] = 1

    def __setitem__(self, key, value):
        self.data[key] = value
        self.add_count[key] = self.add_count.get(key, 0) + 1

# Example usage
my_dict = MyDict(apple=4, banana=2)
my_dict['apple'] = 5  # Update
my_dict['orange'] = 1  # Add new
print(my_dict)
print("Add/Update count:", my_dict.add_count)

