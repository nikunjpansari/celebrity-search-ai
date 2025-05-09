import streamlit as st
from agents.chains import parent_chain
from clients.wiki_client import fetch_image_url
from clients.serper_client import fetch_search_snippet
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI


def show_search():
    st.title("Celebrity Search")
    name = st.text_input("Enter a celebrity name", placeholder="e.g. Michelle Obama")

    if not name:
        st.info("Type a name above and click **Search**")
        return

    if st.button("Search"):
        use_openai = st.session_state.get("use_openai", True)
        use_gemini = st.session_state.get("gemini_llm") is not None

        # 1) Try OpenAI chain
        result = {}
        if use_openai:
            try:
                result = parent_chain({"name": name})
            except Exception:
                use_openai = False

        # 2) If OpenAI failed and Gemini is configured, run Gemini chain
        if not use_openai and use_gemini:
            gemini_llm: ChatGoogleGenerativeAI = st.session_state["gemini_llm"]

            tpl_bio    = PromptTemplate.from_template("Give me a concise biography of {name}.")
            tpl_dob    = PromptTemplate.from_template("When was {name} born?")
            tpl_works  = PromptTemplate.from_template("List 5 of the most notable works or accomplishments of {name}.")
            tpl_events = PromptTemplate.from_template("List 5 major world events that happened around {dob}.")

            mem_bio    = ConversationBufferMemory(input_key="name", memory_key="bio_history")
            mem_dob    = ConversationBufferMemory(input_key="name", memory_key="dob_history")
            mem_works  = ConversationBufferMemory(input_key="name", memory_key="works_history")
            mem_events = ConversationBufferMemory(input_key="dob",  memory_key="events_history")

            chain_bio    = LLMChain(llm=gemini_llm, prompt=tpl_bio,    output_key="bio",   memory=mem_bio)
            chain_dob    = LLMChain(llm=gemini_llm, prompt=tpl_dob,    output_key="dob",   memory=mem_dob)
            chain_works  = LLMChain(llm=gemini_llm, prompt=tpl_works,  output_key="works", memory=mem_works)
            chain_events = LLMChain(llm=gemini_llm, prompt=tpl_events, output_key="events",memory=mem_events)

            seq = SequentialChain(
                chains=[chain_bio, chain_dob, chain_events, chain_works],
                input_variables=["name"],
                output_variables=["bio","dob","events","works"],
                verbose=False
            )
            result = seq({"name": name})

        # 3) Always fetch Google snippet & Wikipedia image
        snippet = fetch_search_snippet(name)
        img_url  = fetch_image_url(name)

        # 4) Display results
        col1, col2 = st.columns([1,2])
        with col1:
            if img_url:
                st.image(img_url, caption=name, use_column_width=True)
            else:
                st.write("No image found.")
        with col2:
            st.subheader("Google Top Snippet")
            st.write(snippet or "No snippet found.")
            if result:
                st.subheader("Biography")
                st.write(result.get("bio", ""))
                st.subheader("Date of Birth")
                st.write(result.get("dob", ""))
                st.subheader("Notable Works")
