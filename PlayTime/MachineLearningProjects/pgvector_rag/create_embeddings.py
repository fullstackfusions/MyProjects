# docker run --name pgvector-container -e POSTGRES_USER=<username> -e POSTGRES_PASSWORD=<password> -e POSTGRES_DB=<db> -p <port>:5432 -d ankane/pgvector

# pip install langchain_postgres

from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector # remember PGVector will add vector extension automatically if don't then you have to add "CREATE EXTENSION vector" in each db

# See docker command above to launch a postgres instance with pgvector enabled.
connection = "postgresql+psycopg://<username>:<password>@<host>:<port>/<db>"  # Uses psycopg3!
collection_name = "my_docs"
embeddings = OpenAIEmbeddings()

# run following is helpful when you try to upload the large document
# vectorstore = PGVector.from_documents(
#     embeddings=embeddings,
#     collection_name=collection_name,
#     connection=connection,
#     use_jsonb=True,
# )

# if your collection has embeddings then you can query against vectorstore.
vectorstore = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

normal_answer_from_collection = vectorstore.similarity_search("where is Canada?")

# if you don't have embeddings in vectorstore then add documents in collection and then query against them
vectorstore.drop_tables()

docs = [
    Document(
        page_content="there are cats in the pond",
        metadata={"id": 1, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="ducks are also found in the pond",
        metadata={"id": 2, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="fresh apples are available at the market",
        metadata={"id": 3, "location": "market", "topic": "food"},
    ),
    Document(
        page_content="the market also sells fresh oranges",
        metadata={"id": 4, "location": "market", "topic": "food"},
    ),
    Document(
        page_content="the new art exhibit is fascinating",
        metadata={"id": 5, "location": "museum", "topic": "art"},
    ),
    Document(
        page_content="a sculpture exhibit is also at the museum",
        metadata={"id": 6, "location": "museum", "topic": "art"},
    ),
    Document(
        page_content="a new coffee shop opened on Main Street",
        metadata={"id": 7, "location": "Main Street", "topic": "food"},
    ),
    Document(
        page_content="the book club meets at the library",
        metadata={"id": 8, "location": "library", "topic": "reading"},
    ),
    Document(
        page_content="the library hosts a weekly story time for kids",
        metadata={"id": 9, "location": "library", "topic": "reading"},
    ),
    Document(
        page_content="a cooking class for beginners is offered at the community center",
        metadata={"id": 10, "location": "community center", "topic": "classes"},
    ),
]

vectorstore.add_documents(docs, ids=[doc.metadata["id"] for doc in docs])

normal_answer = vectorstore.similarity_search("kitty", k=10)

# similarity searcch with filter
# filtered_answer = vectorstore.similarity_search("kitty", k=10, filter={"id": {"$in": [1, 5, 2, 9]}})

# adding location in filter
# location_filtered_answer = vectorstore.similarity_search(
#     "ducks",
#     k=10,
#     filter={"id": {"$in": [1, 5, 2, 9]}, "location": {"$in": ["pond", "market"]}},
# )

# adding and operation in filter
# and_operator_answer = vectorstore.similarity_search(
#     "ducks",
#     k=10,
#     filter={
#         "$and": [
#             {"id": {"$in": [1, 5, 2, 9]}},
#             {"location": {"$in": ["pond", "market"]}},
#         ]
#     },
# )

# adding not equal to operator in filter
# ne_answer = vectorstore.similarity_search("bird", k=10, filter={"location": {"$ne": "pond"}})

print(normal_answer)
