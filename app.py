import streamlit as st
from rag_pipeline import ask_question

st.set_page_config(page_title="Enterprise KB Q&A", layout="wide")

st.title("📊 Enterprise Knowledge Base Q&A")

query = st.text_input("Ask your question:")

if st.button("Search"):
    if query.strip():
        with st.spinner("Searching..."):
            answer, docs = ask_question(query)

        st.subheader("📌 Answer:")
        st.write(answer)

        st.subheader("📄 Sources:")

        if docs:
            for i, doc in enumerate(docs, 1):
                st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Unknown')}")
        else:
            st.write("No sources found.")
    else:
        st.warning("⚠️ Please enter a question.")