# 📊 Enterprise Knowledge Base Q&A System

🚀 A **GenAI-powered Retrieval-Augmented Generation (RAG) system** that allows users to ask questions from enterprise documents (PDFs) and get accurate, context-based answers using a **local LLM (Ollama)**.

---

## 🧠 Overview

This project enables intelligent question-answering over enterprise documents by combining:

- 📄 Document ingestion (PDFs)
- 🔍 Semantic search (FAISS vector database)
- 🤖 Local LLM (Mistral via Ollama)
- ⚡ Fast and accurate responses using context

The system ensures answers are generated **only from provided documents**, reducing hallucinations.

---

## ✨ Features

### 📂 Document Processing
- Upload and process multiple PDF documents
- Automatic text extraction using PyPDF
- Metadata support (source tracking)

### 🔍 Semantic Search (FAISS)
- Converts documents into vector embeddings
- Performs similarity-based retrieval
- Retrieves top relevant chunks for each query

### 🤖 Local LLM (No API Cost)
- Uses **Ollama + Mistral model**
- Fully offline (no OpenAI API required)
- Secure and cost-free inference

### 🧠 RAG Pipeline
- Combines retrieval + generation
- Context-aware responses
- Reduces hallucination with strict prompt control

### 💬 Question Answering
- Ask natural language questions
- Returns accurate answers based on documents
- Fallback response if answer not found

### 📄 Source Attribution
- Displays source documents used in answering
- Improves transparency and trust

### 📊 Streamlit UI
- Clean and interactive interface
- Easy input for queries
- Displays answers and sources clearly

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **LangChain** (RAG pipeline)
- **FAISS** (Vector database)
- **HuggingFace Embeddings**
- **Ollama (Mistral LLM)**
- **PyPDF**

---

## 📂 Project Structure
```
Enterprise-Knowledge-Base-Q-A-System/
│
├── app.py               # Streamlit UI
├── rag_pipeline.py      # RAG logic (retrieval + LLM)
├── ingest.py            # Document processing & FAISS index creation
├── config.py            # Embedding model config (if used)
├── requirements.txt     # Dependencies
│
├── data/
│ └── docs/              # PDF documents
│
├── faiss_index/         # Vector database (generated)
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/pranjalsalvi/Enterprise-Knowledge-Base-Q-A-System.git
cd Enterprise-Knowledge-Base-Q-A-System
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Run Ollama (Local LLM)
```
ollama run mistral
```
### 4. Add Documents
Place your PDF files inside: data/docs/ 

### 5. Create FAISS Index
```
python ingest.py
```
 ### 6. Run Application
 ```
streamlit run app.py
```

## 🚀 Future Enhancements
- 📤 Upload PDFs directly from UI
- 💬 Chat-based interface (ChatGPT style)
- 🧠 Conversation memory
- 🔐 User authentication system
- 🌐 Deployment on cloud (Streamlit Cloud / AWS)
  
---

## 👨‍💻 Author
**Pranjal Salvi**  
Data Science Student
