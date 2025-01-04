from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from common.config import Config

config = Config()
token = config.openai.token
openai_api_base = config.openai.openai_api
model = ChatOpenAI(model_name="gpt4", openai_api_key=token, openai_api_base=openai_api_base)

