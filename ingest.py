from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
from config import EMBED_MODEL

DATA_PATH = "data/docs"

documents = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(DATA_PATH, file))
        documents.extend(loader.load())

print("Docs loaded:", len(documents))

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

# DEBUG
print("Embedding dim (ingest):", len(embeddings.embed_query("test")))

db = FAISS.from_documents(docs, embeddings)

db.save_local("faiss_index")

print("✅ FAISS CREATED")