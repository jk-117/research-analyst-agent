# 🧠 Autonomous Research Analyst Agent

A **multi-agent AI system** capable of autonomous web search, summarisation, Q&A, and critique to accelerate research and knowledge synthesis.

---

## 🚀 **Project Overview**

This project demonstrates a **Retrieval-Augmented Generation (RAG) pipeline** with **multi-agent collaboration** to:

✅ Scrape or ingest long text data  
✅ Summarise complex content using Hugging Face Transformers  
✅ Index chunks into a vector store (ChromaDB)  
✅ Retrieve relevant context for user queries  
✅ Critique generated outputs for improvement suggestions

---

## 🏆 **Key Features**

- **Summariser Agent:** Uses `facebook/bart-large-cnn` to summarise text efficiently.  
- **Embeddings Module:** Generates embeddings with `all-MiniLM-L6-v2` Sentence Transformers.  
- **Q&A Agent:** Implements RAG pipeline with ChromaDB for context-grounded answers.  
- **Critic Agent:** Placeholder critique function for adaptive feedback (future: integrate evaluation models).  
- **Multi-Agent Orchestration:** Modular pipeline design for scalable AI agent collaboration.  
- **Streamlit UI (Upcoming):** Interactive frontend for user queries and output display.  
- **Dockerised:** Containerised for deployment readiness.  
- **CI/CD Pipeline:** GitHub Actions for automated build, test, and deploy workflows.

---

## 🔧 **Tech Stack**

- **Python 3.10+**
- **Hugging Face Transformers & Sentence Transformers**
- **LangChain**
- **ChromaDB**
- **Streamlit**
- **Docker & docker-compose**
- **GitHub Actions**
- **Pytest**

---

## 📁 **Project Structure**

