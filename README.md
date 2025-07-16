


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



## 📁 **Project Structure**



research\_analyst\_agent/
├── agents/
│   ├── orchestrator\_agent.py
│   ├── summariser\_agent.py
│   ├── qa\_agent.py
│   └── critic\_agent.py
├── models/
│   ├── summarisation.py
│   └── embeddings.py
├── tools/
│   └── scraper\_tool.py
├── app/
│   └── main.py
├── tests/
│   └── test\_agents.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md





## ⚡ **Quick Start**

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/research_analyst_agent.git
cd research_analyst_agent
````

2. **Setup virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run summarisation module test**

```bash
python models/summarisation.py
```

4. **Run Q\&A Agent test**

```bash
python agents/qa_agent.py
```

5. **Run unit tests**

```bash
pytest tests/
```

---

## 🐳 **Docker Deployment**

1. **Build the image**

```bash
docker build -t research_analyst_agent .
```

2. **Run the container**

```bash
docker run -it -p 8501:8501 research_analyst_agent
```
2. **Open the Link**

```bash
https:/localhost:8501/ or https:/127.0.0.1:8501/
```


---

## 🤖 **Future Enhancements**

* 🌐 **Autonomous web scraping tool** integration
* 🔍 **OpenAI LLM-based critique agent** for advanced evaluation
* 🎛️ **Streamlit frontend with user authentication**
* ☁️ **Deploy to Azure / AWS ECS / GCP Cloud Run**

---

## ✨ **Author**

**Jaisimha Kothari**
AI Engineer | Passionate about scalable, real-world AI solutions.

[LinkedIn]((https://www.linkedin.com/in/jaisimha-kothari/)) • [GitHub]((https://github.com/jk-117))


> ⚡ **“Empowering research through autonomous, intelligent agents.”**


