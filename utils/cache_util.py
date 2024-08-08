from typing import List
from utils.csv_util import load_csv
from utils.pdf_util import load_pdfs
from utils.text_util import get_text_chunks
from utils.embedding_util import get_vector_store

data_cache = {
    "cvs": None,
    "resource": None
}

async def load_csv_data(file_path: str):
    raw_text = load_csv(file_path)
    text = "\n".join(raw_text.astype(str).values.flatten())
    text_chunks = get_text_chunks(text)
    vector_store = get_vector_store(text_chunks)
    data_cache["resource"] = vector_store

async def load_pdf_data(file_paths: List[str]):
    raw_text = load_pdfs(file_paths)
    text_chunks = get_text_chunks(raw_text)
    vector_store = get_vector_store(text_chunks)
    data_cache["cvs"] = vector_store

def get_data_cache(source: str):
    return data_cache.get(source)
