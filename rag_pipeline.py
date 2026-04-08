from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import ollama
import os
from config import EMBED_MODEL

# STOP if index missing
if not os.path.exists("faiss_index"):
    raise Exception("❌ Run ingest.py first")

embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# DEBUG
print("Embedding dim (query):", len(embeddings.embed_query("test")))
print("FAISS dim:", db.index.d)

def ask_question(query):
    docs = db.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the context.
If not found, say "Not found".

Context:
{context}

Question:
{query}
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"], docs