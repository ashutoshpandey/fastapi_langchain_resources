from langchain_text_splitters import CharacterTextSplitter

# Break string data into chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=20, length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks
