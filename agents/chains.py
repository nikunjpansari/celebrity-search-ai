from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory.buffer import ConversationBufferMemory

_llm = OpenAI(temperature=0.7)

# Biography chain
_tpl_bio = PromptTemplate(
    input_variables=["name"],
    template="Give me a concise biography of {name}."
)
_mem_bio = ConversationBufferMemory(input_key="name", memory_key="bio_history")
chain_bio = LLMChain(
    llm=_llm, prompt=_tpl_bio,
    output_key="bio", memory=_mem_bio
)

# DOB chain
_tpl_dob = PromptTemplate(
    input_variables=["name"],
    template="When was {name} born?"
)
_mem_dob = ConversationBufferMemory(input_key="name", memory_key="dob_history")
chain_dob = LLMChain(
    llm=_llm, prompt=_tpl_dob,
    output_key="dob", memory=_mem_dob
)

# Events chain
_tpl_events = PromptTemplate(
    input_variables=["dob"],
    template="List 5 major world events that happened around {dob}."
)
_mem_events = ConversationBufferMemory(
    input_key="dob", memory_key="events_history"
)
chain_events = LLMChain(
    llm=_llm, prompt=_tpl_events,
    output_key="events", memory=_mem_events
)

# Notable works chain
_tpl_works = PromptTemplate(
    input_variables=["name"],
    template="List 5 of the most notable works or accomplishments of {name}."
)
_mem_works = ConversationBufferMemory(
    input_key="name", memory_key="works_history"
)
chain_works = LLMChain(
    llm=_llm, prompt=_tpl_works,
    output_key="works", memory=_mem_works
)

# Master sequence
parent_chain = SequentialChain(
    chains=[chain_bio, chain_dob, chain_events, chain_works],
    input_variables=["name"],
    output_variables=["bio", "dob", "events", "works"],
    verbose=False
)
