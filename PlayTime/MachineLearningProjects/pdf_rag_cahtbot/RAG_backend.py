# %pip install langchain langchain-community python_dotenv
# %pip install langchain-openai

# %pip install pandas numpy
# %pip install streamlit

# %pip install "unstructured[all-docs]<=0.16.10"
# %pip install langchain_postgres

# %pip install redis>=4.1.0

from unstructured.partition.pdf import partition_pdf
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough,RunnableLambda

from langchain_postgres.vectorstores import PGVector
from database_setup import COLLECTION_NAME, CONNECTION_STRING
from langchain_community.storage import RedisStore
from langchain.schema.document import Document
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers.multi_vector import MultiVectorRetriever
from pathlib import Path
from IPython.display import display, HTML, Markdown
from base64 import b64decode
import os, hashlib, shutil, uuid, json, time
import torch, redis, streamlit as st
import logging
# Initialize Redis client
client = redis.Redis(host="localhost", port=6379, db=0)


from dotenv import load_dotenv
load_dotenv()


FILE_PATH = Path("data/hbspapers_48__1.pdf")


def data_loading():

    raw_pdf_elements = partition_pdf(
        filename=FILE_PATH,

        infer_table_structure=True,
        strategy = "hi_res",

        extract_image_block_types = ["Image"],
        extract_image_block_to_payload  = True,

        chunking_strategy="by_title",
        mode='elements',
        max_characters=10000,
        new_after_n_chars=5000,
        combine_text_under_n_chars=2000,
        image_output_dir_path="data/",
    )
    return raw_pdf_elements

pdf_elements = data_loading()
# pdf elements are a list of unstructured elements
# each element has a type, text, and metadata
# we will convert them to langchain documents


tables = [element.metadata.text_as_html for element in pdf_elements if 'Table' in str(type(element))]
text = [element.text for element in pdf_elements if 'CompositeElement' in str(type(element))]
# example of the data in tables[0].metadata.to_dict()
# you can also check text
# display(HTML(tables[0])) will display the table as HTML


# Summarize the Data
# Summarize extracted text and tables using LLM
def summarize_text_and_tables(text, tables):
    logging.info("Ready to summarize data with LLM")
    prompt_text = """You are an assistant tasked with summarizing text and tables. \

                    You are to give a concise summary of the table or text and do nothing else.
                    Table or text chunk: {element} """
    prompt = ChatPromptTemplate.from_template(prompt_text)
    model = ChatOpenAI(temperature=0.6, model="gpt-4o-mini")
    summarize_chain = {"element": RunnablePassthrough()}| prompt | model | StrOutputParser()
    logging.info(f"{model} done with summarization")
    return {
        "text": summarize_chain.batch(text, {"max_concurrency": 5}),
        "table": summarize_chain.batch(tables, {"max_concurrency": 5})
    }

data_summary = summarize_text_and_tables(text, tables)
text_summary = data_summary['text']
tables_summary = data_summary['table']



# Initialize the retriever with PGVector and RedisStore
def initialize_retriever():

    store = RedisStore(client=client)
    id_key = "doc_id"
    vectorstore = PGVector(
            embeddings=OpenAIEmbeddings(),
            collection_name=COLLECTION_NAME,
            connection=CONNECTION_STRING,
            use_jsonb=True,
            )
    retrieval_loader = MultiVectorRetriever(vectorstore=vectorstore, docstore=store, id_key="doc_id")
    return retrieval_loader

load_retriever = initialize_retriever()


# Add Summary to vectorstore & Raw data to RedisStore

# Store text, tables, and their summaries in the retriever

def store_docs_in_retriever(text, text_summary, table, table_summary, retriever):
    """Store text and table documents along with their summaries in the retriever."""

    def add_documents_to_retriever(documents, summaries, retriever, id_key = "doc_id"):
        """Helper function to add documents and their summaries to the retriever."""
        if not summaries:
            return None, []

        doc_ids = [str(uuid.uuid4()) for _ in documents]
        summary_docs = [
            Document(page_content=summary, metadata={id_key: doc_ids[i]})
            for i, summary in enumerate(summaries)
        ]

        retriever.vectorstore.add_documents(summary_docs, ids=doc_ids)
        retriever.docstore.mset(list(zip(doc_ids, documents)))

# Add text, table, and image summaries to the retriever
    add_documents_to_retriever(text, text_summary, retriever)
    add_documents_to_retriever(table, table_summary, retriever)
    return retriever

retriever  = store_docs_in_retriever(text, text_summary, tables,  tables_summary, load_retriever)

query = "What is the comparison of the composition of red meat and vegetarian protein sources"

docs = retriever.invoke(query)

print(docs)


# RAG Pipeline

# Parse the retriever output
def parse_retriver_output(data):
    parsed_elements = []
    for element in data:
        # Decode bytes to string if necessary
        if isinstance(element, bytes):
            element = element.decode("utf-8")

        parsed_elements.append(element)

    return parsed_elements

# Chat with the LLM using retrieved context
def chat_with_llm():


    prompt_text = """
                You are an AI Assistant tasked with understanding detailed
                information from text and tables. You are to answer the question based on the
                context provided to you. You must not go beyond the context given to you.

                Context:
                {context}

                Question:
                {question}
                """

    prompt = ChatPromptTemplate.from_template(prompt_text)
    model = ChatOpenAI(temperature=0.6, model="gpt-4o-mini")

    rag_chain = {
       "context": retriever | RunnableLambda(parse_retriver_output), "question": RunnablePassthrough(),
        } | RunnablePassthrough().assign(
        response=(
        prompt
        | model
        | StrOutputParser()
        )
        )

    return rag_chain

rag_chain = chat_with_llm()

response = rag_chain.invoke("What is the nutrient composition of beef, veal, lamb and mutton")

print(response['response'])

response = rag_chain.invoke("What is the nutrient composition of organ meats")

print(response['response'])

response = rag_chain.invoke("What is Meat?")
