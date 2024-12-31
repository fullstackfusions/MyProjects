import pyodbc

# SQL Server connection details
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
connection_url = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish a connection
conn = pyodbc.connect(connection_url)

# Create a cursor from the connection
cursor = conn.cursor()

# Define the chunk size
chunk_size = 100  # Adjust chunk size as needed

# Execute the SQL query
cursor.execute("SELECT * FROM your_table_name")

# Fetch data in chunks
while True:
    rows = cursor.fetchmany(chunk_size)
    if not rows:
        break  # No more data

    for row in rows:
        print(row)  # Process the chunk of rows

# Close the connection
cursor.close()
conn.close()
