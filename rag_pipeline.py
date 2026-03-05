from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA


def build_vectorstore(chunks):
    embeddings = OllamaEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    return vectorstore


def build_rag_chain(vectorstore):
    llm = Ollama(model="llama2")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    return chain