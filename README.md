# Log Summarization using RAG

This project demonstrates log analysis and summarization using Retrieval Augmented Generation (RAG).

Technologies used:

- Python
- Streamlit
- LangChain
- Ollama
- FAISS

## Features

- Upload logs or use demo logs
- Chunk log files
- Generate embeddings
- Build FAISS vector index
- Retrieve relevant log sections
- Generate summaries using LLM

## Run

Install dependencies

pip install -r requirements.txt

Run application

streamlit run app.py

## Example queries

Summarize recent errors  
What caused the database failure?  
Show network related issues