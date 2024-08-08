import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def get_vector_store(text_chunks):
    load_dotenv()
    
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key is None:
        print("Environment variable 'OPENAI_API_KEY' is not set.")

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore
