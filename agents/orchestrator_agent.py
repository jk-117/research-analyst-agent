# agents/orchestrator_agent.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.summariser_agent import SummariserAgent
from agents.qa_agent import QAAgent
from agents.critic_agent import CriticAgent

class OrchestratorAgent:
    """
    Orchestrates summarisation, QA, and critique pipeline.
    """

    def __init__(self):
        self.summariser = SummariserAgent()
        self.qa = QAAgent()
        self.critic = CriticAgent()

    def run_pipeline(self, user_query: str, context_text: str) -> dict:
        """
        Executes the full pipeline:
        1. Summarises context
        2. Answers query using QA Agent
        3. Critiques the answer
        Returns a structured dictionary.
        """
        # Step 1: Summarise context
        summary = self.summariser.run(context_text)

        # Step 2: Get QA answer
        answer = self.qa.answer_query(summary, user_query)

        # Step 3: Critique the answer
        critique = self.critic.critique(user_query, answer)

        # Step 4: Return structured result
        result = {
            "summary": summary,
            "answer": answer,
            "critique": critique
        }

        return result


if __name__ == "__main__":
    # Quick test
    orchestrator = OrchestratorAgent()
    sample_context = "Artificial Intelligence is transforming industries by automating tasks and providing insights from data."
    sample_query = "How is AI transforming industries?"
    output = orchestrator.run_pipeline(sample_query, sample_context)
    print(output)
