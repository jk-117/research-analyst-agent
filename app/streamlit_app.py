import os
import sys  
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))    

import streamlit as st
from agents.orchestrator_agent import OrchestratorAgent

# Initialize agent
orchestrator = OrchestratorAgent()

st.set_page_config(page_title="Research Analyst Agent", layout="wide")

st.title("📊 Research Analyst Agent")

st.markdown("""
This app uses your multi-agent pipeline to:
- Summarise context
- Answer questions
- Critique answers

🔍 Enter any topic to begin.
""")

user_input = st.text_area("Enter your research question:", height=100)
context_input = st.text_area("Enter context text (article or content to analyse):", height=200)

if st.button("Analyse"):
    if user_input.strip() == "" or context_input.strip() == "":
        st.warning("Please enter both query and context.")
    else:
        with st.spinner("Running analysis..."):
            output = orchestrator.run_pipeline(user_input, context_input)
            st.success("Analysis complete.")

            st.subheader("Summary")
            st.write(output["summary"])

            st.subheader("Answer")
            st.write(output["answer"])

            st.subheader("Critique")
            st.write(output["critique"])
