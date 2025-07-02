import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.summariser_agent import SummariserAgent
from models.embeddings import generate_embedding

def test_summariser_agent():
    agent = SummariserAgent()
    input_text = """
    I'm a new coder who wants to level up my skills and stand out in today's job market by building coding projects that use AI in a meaningful way.
    Give me 3 unique project ideas that:
    Teach me real-world development skills
    Use beginner-friendly but powerful AI tools (like OpenAI, Langchain, or Hugging Face)
    Solve actual problems or provide value to users
    Can be built with a full-stack JavaScript or Python stack
    For each project, include:
    A one-sentence project description
    The real-world use case
    Suggested tech stack (frontend, backend, AI tools, database, etc.)
    AI feature(s) and how they are used
    One advanced feature to help the project stand out
    How I could pitch this project on my resume or in an interview
    Avoid basic CRUD apps or toy examples. I want real projects that make me job-ready and show that I can work with AI.
    """
    summary = agent.run(input_text)
    assert isinstance(summary, str)
    assert len(summary) < len(input_text)

def test_generate_embedding():
    text = "Test embedding generation for this sample text."
    embedding = generate_embedding(text)
    assert isinstance(embedding, list)
    assert len(embedding) > 0

if __name__ == "__main__":
    test_summariser_agent()
    test_generate_embedding()
    print("All tests passed.")
