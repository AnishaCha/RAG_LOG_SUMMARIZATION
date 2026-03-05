# Log Summarization using Retrieval Augmented Generation (RAG)

## Overview

This project demonstrates how **Retrieval Augmented Generation (RAG)** can be used to analyze and summarize system logs.

Large log files are difficult to manually inspect. This application processes logs, retrieves the most relevant entries, and uses a local Large Language Model to generate summaries or answer questions about the logs.

The application is built using:

* Python
* Streamlit
* LangChain
* FAISS Vector Store
* Ollama LLM

The goal of this project is to demonstrate how LLM-powered retrieval can assist with **log analysis, incident investigation, and root cause discovery**.

---

## Features

* Upload custom log files or use sample logs
* Automatically splits logs into manageable chunks
* Generates vector embeddings for log chunks
* Stores embeddings in a FAISS vector index
* Retrieves relevant log entries using semantic similarity
* Uses an LLM to generate summaries and answers
* Interactive UI built with Streamlit

---

## Architecture

The project uses a simple RAG pipeline:

1. **Log Input**

   * User uploads logs or uses a sample dataset

2. **Chunking**

   * Logs are split into smaller chunks for better embedding

3. **Embedding Generation**

   * Each chunk is converted into a vector representation

4. **Vector Storage**

   * Vectors are stored in FAISS for similarity search

5. **Retrieval**

   * Relevant chunks are retrieved based on the user's query

6. **Generation**

   * Ollama LLM generates summaries or answers based on retrieved logs

---

## Project Structure

```
log-rag-summarizer/
│
├── app.py
├── rag_pipeline.py
├── sample_logs.py
├── requirements.txt
├── README.md
└── .gitignore
```

### app.py

Streamlit web application for interacting with the RAG system.

### rag_pipeline.py

Contains logic for:

* building vector stores
* configuring the retrieval chain
* interacting with the LLM

### sample_logs.py

Provides example logs used for testing the application.

### requirements.txt

Lists Python dependencies required to run the project.


## Install Ollama

The application requires **Ollama** to run a local LLM.

Install Ollama from:

https://ollama.com

Pull the required model:

```
ollama pull llama3.2
```

Start Ollama:

```
ollama serve
```

---

## Running the Application

Run the Streamlit application:

```
streamlit run app.py
```

---

## Example Queries

You can ask questions such as:

* Summarize recent errors
* What caused the database connection failures?

The system retrieves relevant log entries and generates a summary.

---

## Example Logs

Example log format used in this demo:

```
[2025-11-01 10:01:12] ERROR order-db: ORA-12541: TNS:no listener
[2025-11-01 10:01:15] WARN order-api: Connection timeout to order-db
[2025-11-01 10:02:05] ERROR network: ACL update failed
```

---

## Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core programming language  |
| Streamlit  | Web interface              |
| LangChain  | RAG pipeline orchestration |
| FAISS      | Vector similarity search   |
| Ollama     | Local LLM inference        |

---

## Future Improvements

Possible enhancements for production environments:

* Persistent vector database storage
* Log anomaly detection
* Root cause analysis generation
* Multi-source log ingestion
* PII redaction
* Distributed log ingestion pipelines
* Integration with monitoring tools

---

## Limitations

This project is a demonstration and has several limitations:

* Uses a small demo dataset
* FAISS index is in-memory
* No authentication or access control
* Limited log parsing logic

---

## License

This project is released under the MIT License.

---

## Author

Created as a demonstration project for applying **RAG to log analysis and summarization**.
