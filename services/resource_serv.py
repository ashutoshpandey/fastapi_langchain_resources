import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from utils.csv_util import load_csv
from utils.text_util import get_text_chunks
from utils.embedding_util import get_vector_store

async def get_resource_response(query: str):
    load_dotenv()
    
    resource_path = os.getenv('RESOURCE_PATH')
    conversation_chain = await setup_data('../' + resource_path)
    return await process_query(query, conversation_chain)


# ---------------------- helper functions ------------------------------

# Setup data
async def setup_data(resource_path: str):
    csv_data = load_csv(resource_path)

   # Extract text from DataFrame
    raw_text = "\n".join(csv_data.astype(str).values.flatten())

    #Split the Text into Chunks
    text_chunks = get_text_chunks(raw_text)
    #Create Vector Store
    vector_store = get_vector_store(text_chunks)
    # Create conversation chain for memory    
    return get_conversation_chain(vector_store)


# Setup conversation
def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm,retriever=vectorstore.as_retriever(),memory=memory)

    return conversation_chain

# Process user input 
async def process_query(query: str, conversation_chain):
    return conversation_chain({'question': query})
