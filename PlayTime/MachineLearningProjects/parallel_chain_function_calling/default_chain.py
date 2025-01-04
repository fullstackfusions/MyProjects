from langchain.chains.conversation.base import ConversationChain
from model import model

default_chain = ConversationChain(llm=model)
