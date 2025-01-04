from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.llms.openai import OpenAI
from langchain.chains import ConversationChain

# First initialize the llm
llm = OpenAI(model_name='gpt-4', temperature=0, max_tokens=256)

# create a memory object
# Note: Here we are calling the llm again to help us summarize the conversation
summary_memory = ConversationSummaryMemory(llm=OpenAI())

# initialize conversationchain
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=summary_memory
)

conversation.predict(input="Hi there! I am Mihir.")