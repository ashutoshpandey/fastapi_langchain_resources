import os
import glob
from pypdf import PdfReader

# Load pdf files data
def load_pdfs(file_path):
    pdf_files = glob.glob(os.path.join(file_path, "*.pdf"))

    text=""
    for pdf_file in pdf_files:
        with open(pdf_file, "rb") as pdf:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text() 

    return text
