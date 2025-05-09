# app.py
import os
from constants import openai_key
import streamlit as st
from dotenv import load_dotenv
import openai
from langchain_google_genai import ChatGoogleGenerativeAI

# ── Load & configure API keys ───────────────────────────────────────────────
load_dotenv()
OPENAI_API_KEY = openai_key
GOOGLE_API_KEY = googleai_key
SERPER_API_KEY = serperai_key=""

# ── Check OpenAI availability ───────────────────────────────────────────────
def check_openai() -> bool:
    if not OPENAI_API_KEY:
        return False
    openai.api_key = OPENAI_API_KEY
    try:
        openai.Engine.list()
        return True
    except Exception:
        return False

use_openai = check_openai()
use_gemini = (not use_openai) and bool(GOOGLE_API_KEY)

# ── Streamlit page config & sidebar ────────────────────────────────────────
st.set_page_config(
    page_title="Celebrity Search AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    if use_openai:
        st.success("✅ Using OpenAI")
    elif use_gemini:
        st.success("✅ Using Gemini Pro")
    else:
        st.error("❌ No valid OpenAI or Gemini key. Exiting.")
        st.stop()
    st.title("Navigate")
    page = st.radio("", ["Search", "History", "About"])

# ── Instantiate Gemini LLM once if needed ─────────────────────────────────
if use_gemini:
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,
        verbose=False
    )
    st.session_state["gemini_llm"] = gemini_llm

# ── Route to pages ─────────────────────────────────────────────────────────
if page == "Search":
    from pages.search_page import show_search
    show_search()

elif page == "History":
    from pages.history_page import show_history
    show_history()

else:  # About
    from pages.about_page import show_about
    show_about()
