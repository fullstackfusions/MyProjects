import csv

# Writing to a CSV file
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

# Reading from a CSV file
with open('example.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)