class SimpleDatabase:
    def __init__(self):
        self.__data = {}  # Encapsulated attribute to store data

    def add_entry(self, key, value):
        self.__data[key] = value
        print(f"Entry added: {key} = {value}")

    def get_entry(self, key):
        return self.__data.get(key, "Entry not found")

    def display_all(self):
        for key, value in self.__data.items():
            print(f"{key}: {value}")

# Using the SimpleDatabase class
db = SimpleDatabase()
db.add_entry("name", "Alice")
db.add_entry("age", 30)
db.add_entry("occupation", "Engineer")

print("Retrieve 'name':", db.get_entry("name"))  # Retrieve a specific entry
db.display_all()  # Display all entries