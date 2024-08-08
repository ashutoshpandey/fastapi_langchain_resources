from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from utils.cache_util import get_data_cache

source = 'resource'

# ---------------------- helper functions ------------------------------

# Setup conversation
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm,retriever=vectorstore.as_retriever(),memory=memory)

    return conversation_chain

# Process user input 
async def process_query(query: str):
    vector_store = get_data_cache(source)
    if not vector_store:
        raise ValueError(f"No data loaded for source: {source}")

    conversation_chain = get_conversation_chain(vector_store)
    return conversation_chain({'question': query})
