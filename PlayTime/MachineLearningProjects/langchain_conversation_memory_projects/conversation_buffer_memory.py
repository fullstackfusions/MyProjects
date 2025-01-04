from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms.openai import OpenAI
from langchain.chains import ConversationChain

# First initialize the llm
llm = OpenAI(model_name='gpt-4', temperature=0, max_tokens=256)

# create a memory object
memory = ConversationBufferMemory()

# initialize conversationchain
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory
)

conversation.predict(input="Hi there! I am Mihir.")
