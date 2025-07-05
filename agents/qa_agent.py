import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.embeddings import chunk_text, add_to_vector_store, query_vector_store

class QAAgent:
    def __init__(self):
        pass  # placeholder for future configurations

    def ingest_and_index(self, text):
        """
        Chunks input text and adds to vector store.
        """
        chunks = chunk_text(text)
        add_to_vector_store(chunks)

    def answer_query(self, query):
        """
        Retrieves relevant text chunks for the query.
        """
        results = query_vector_store(query, top_k=3)
        combined = " ".join(results)
        return combined  # for now returns retrieved text, later integrate summarisation

if __name__ == "__main__":
    agent = QAAgent()
    sample_text = " ".join(["This is a sample sentence about AI agents and summarisation."] * 50)
    agent.ingest_and_index(sample_text)
    response = agent.answer_query("What is summarisation?")
    print("Retrieved Context:\n", response)
