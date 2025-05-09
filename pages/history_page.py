import streamlit as st
from agents.chains import chain_bio, chain_dob, chain_works, chain_events

def show_history():
    st.title("Conversation History")
    st.subheader("Biography Prompts")
    st.write(chain_bio.memory.buffer or "_No biography queries yet._")
    st.subheader("DOB Prompts")
    st.write(chain_dob.memory.buffer or "_No DOB queries yet._")
    st.subheader("Works Prompts")
    st.write(chain_works.memory.buffer or "_No works queries yet._")
    st.subheader("Events Prompts")
    st.write(chain_events.memory.buffer or "_No events queries yet._")
