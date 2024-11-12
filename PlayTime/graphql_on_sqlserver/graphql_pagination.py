"""

The example shows how to implement offset-based pagination in a GraphQL API, allowing clients to request a specific chunk of data by setting the offset and limit arguments.

"""

# pip install strawberry-graphql fastapi pyodbc

import pyodbc
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from typing import List

# Database connection function
def get_connection():
    server = "your_server_name"
    database = "your_database_name"
    username = "your_username"
    password = "your_password"
    connection_url = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_url)
    return conn

# Define a GraphQL type for your data
@strawberry.type
class DataItem:
    id: int
    name: str
    value: str

# Define the query to fetch data with pagination (offset and limit)
@strawberry.type
class Query:
    @strawberry.field
    def items(self, offset: int = 0, limit: int = 10) -> List[DataItem]:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, name, value FROM your_table_name ORDER BY id OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [DataItem(id=row[0], name=row[1], value=row[2]) for row in rows]

# Create the Strawberry schema
schema = strawberry.Schema(query=Query)

# Initialize FastAPI app and Strawberry's GraphQL router
app = FastAPI()
graphql_app = GraphQLRouter(schema)

# Add the GraphQL route to the FastAPI app
app.include_router(graphql_app, prefix="/graphql")

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
