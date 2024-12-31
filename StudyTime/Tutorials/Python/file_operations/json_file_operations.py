import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Writing to a JSON file
with open('example.json', 'w') as file:
    json.dump(data, file, indent=4)

# Reading from a JSON file
with open('example.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)