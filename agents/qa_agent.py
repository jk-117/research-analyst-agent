import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.embeddings import chunk_text, add_to_vector_store, query_vector_store
from transformers import pipeline
class QAAgent:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

    def ingest_and_index(self, text):
        """
        Chunks input text and adds to vector store.
        """
        chunks = chunk_text(text)
        add_to_vector_store(chunks)



    
    
    def answer_query(self, context, query):
        """
        Answers query based on given context using QA model.
        """
        result = self.qa_pipeline(question=query, context=context)
        return result['answer']

if __name__ == "__main__":
    agent = QAAgent()
    sample_context = "This is a sample sentence about AI agents and summarisation."
    sample_query = "What is summarisation?"
    response = agent.answer_query(sample_context, sample_query)
    print("Answer:\n", response)
