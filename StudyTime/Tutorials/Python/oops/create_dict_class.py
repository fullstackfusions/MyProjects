class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super(MyDict, self).__init__(*args, **kwargs)

    def get(self, key, default=None):
        """Overrides the get method to return a default value if the key is not found."""
        return super(MyDict, self).get(key, default)

    def keys_as_string(self):
        """Returns all keys in the dictionary as a comma-separated string."""
        return ', '.join(str(key) for key in self.keys())

    def values_sum(self):
        """Returns the sum of all values in the dictionary."""
        return sum(self.values())

# Usage
my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})

print("Keys:", my_dict.keys_as_string())  # "a, b, c"
print("Sum of Values:", my_dict.values_sum())  # 6
print("Get 'a':", my_dict.get('a'))  # 1
print("Get 'd':", my_dict.get('d', "Not Found"))  # "Not Found"