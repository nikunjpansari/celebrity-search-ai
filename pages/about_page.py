import streamlit as st

def show_about():
    st.title("About This App")
    st.write(
        """
        **Celebrity Search** is a multipage Streamlit demo that:
        - Uses LangChain + OpenAI for chained LLM prompts  
        - Fetches Google snippets via SerperAPI  
        - Pulls portraits from Wikipedia  
        - Lets you clear & re-run searches  
        - Shows your conversation history  
        """
    )
