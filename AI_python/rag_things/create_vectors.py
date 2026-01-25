"""
extract text from pdfs
use gemini text embeddings to create vectors
prepare metadata for those vectors
pinecone client
upsert vectors into pinecone

use fitz to extract text from pdfs
to install fitz, use the command: pip install PyMuPDF
"""
import os
from pinecone import Pinecone
from google import genai
import fitz  # PyMuPDF


pinecone_client = Pinecone(api_key="PINE API KEY HERE")

vector_index = pinecone_client.Index("student-kb")


google_client = genai.Client(api_key="GENAI API KEY HERE")


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text


def embed_text(text):
    response = google_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config={
              'output_dimensionality': 768
          }
    )
    vector = response.embeddings[0].values
    return vector

def upsert_vectors_to_pinecone(document_texts):
    upsert_data = []
    for idx, text in enumerate(document_texts):
        embedding = embed_text(text)
        vector_id = f"doc-{idx}"
        meta_data = {"text": text}
        upsert_data.append((vector_id, embedding, meta_data))
    vector_index.upsert(upsert_data)
    print("Vectors upserted successfully.")
    

if __name__ == "__main__":
    document_texts = []
    document_dirs = os.listdir("documents")
    for file_path in document_dirs:
        text = extract_text_from_pdf(os.path.join("documents", file_path))
        document_texts.append(text)
        
    upsert_vectors_to_pinecone(document_texts)
    print("All documents processed and vectors upserted.")
    