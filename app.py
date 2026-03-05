import streamlit as st
from rag_pipeline import build_vectorstore, build_rag_chain
from sample_logs import DUMMY_LOG
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(page_title="Log RAG Summarizer", layout="centered")

st.title("Log Summarizer using RAG")

mode = st.sidebar.radio("Log source", ["Dummy log", "Upload file"])

if mode == "Upload file":
    uploaded_file = st.sidebar.file_uploader("Upload log file", type=["txt", "log"])
    if uploaded_file:
        log_text = uploaded_file.read().decode("utf-8")
    else:
        log_text = DUMMY_LOG
        st.sidebar.warning("Using demo logs")
else:
    log_text = DUMMY_LOG

st.subheader("Log Preview")
st.code("\n".join(log_text.splitlines()[:50]))

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=80)
chunks = splitter.split_text(log_text)

st.write(f"Total chunks created: {len(chunks)}")

with st.spinner("Building vector index..."):
    vectorstore = build_vectorstore(chunks)

chain = build_rag_chain(vectorstore)

st.subheader("Ask Questions about Logs")

query = st.text_input("Enter question or request summary")

if st.button("Run"):
    if not query:
        st.warning("Enter a query first")
    else:
        with st.spinner("Processing..."):
            result = chain.run(query)
            st.success("Result")
            st.write(result)

if st.checkbox("Show retrieved evidence"):
    docs = vectorstore.similarity_search("What caused database errors?", k=3)
    for i, doc in enumerate(docs, 1):
        st.markdown(f"**Chunk {i}**")
        st.code(doc.page_content)

st.markdown("---")
st.caption("Demo log summarization using RAG with LangChain and Ollama")