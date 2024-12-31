import yaml

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Writing to a YAML file
with open('example.yaml', 'w') as file:
    yaml.dump(data, file)

# Reading from a YAML file
with open('example.yaml', 'r') as file:
    loaded_data = yaml.safe_load(file)
    print(loaded_data)