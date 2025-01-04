from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.llms.openai import OpenAI
from langchain.chains import ConversationChain

# First initialize the llm
llm = OpenAI(model_name='gpt-4', temperature=0, max_tokens=256)

# create a memory object
# Note: we keep low=2 to only keep the last 2 interactions in memory
summary_memory = ConversationBufferWindowMemory(k=2)

# initialize conversationchain
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=summary_memory
)

conversation.predict(input="Hi there! I am Mihir.")
