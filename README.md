# Celebrity Search AI

A **Streamlit** application that lets you look up any public figure and instantly see:

- 🧠 A concise **biography**  
- 🎂 **Date of birth**  
- 🏆 **Notable works** or accomplishments  
- 🌐 **Major world events** around their birth  
- 🔍 A **Google top snippet** via SerperAPI  
- 🖼️ Their **portrait** fetched from Wikipedia  

Built with [LangChain](https://github.com/langchain-ai/langchain) + OpenAI + Streamlit + SerperAPI + Python-Wikipedia.

---

## 🚀 Features

- **Multi‐step LLM chains** (bio → DOB → events → works) via LangChain  
- **Real-time search snippets** from Google (SerperAPI)  
- **Portrait images** from Wikipedia  
- **Attractive multipage UI** (Search / History / About)  
- **“New Search”** button to reset inputs  
- **Conversation history** viewer  
- **Secure** API key loading via `.env`

---
## 🔧 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/celebrity-search.git
   cd celebrity-search

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Linux / macOS
   .venv\Scripts\activate         # Windows

3. **Install dependencies**  
   ```bash
   python3 -m venv .venv

⚙️ Configuration
Create a .env file in the project root with the following variables:

# Open AI Key
OPENAI_API_KEY=your_openai_api_key

# Google Gemini Pro (Vertex AI)
GOOGLE_API_KEY=your_gcp_api_key

# SerperAPI
SERPER_API_KEY=your_serper_api_key

▶️ Usage
1. Run as a CLI
   ```bash
   streamlit run app.py

🔍 Search: Enter a celebrity name, click Search → view image, Google snippet, bio, DOB, works, events.

🔄 New Search: Clear results and enter a new name.

📖 History: See your past queries for each LLM prompt.

⚙️ About: Overview and credits.

## 🛠️ Customization

- **Adjust LLM behavior**  
  Modify the `temperature`, `max_tokens`, or `model_name` parameters in `agents/chains.py` to tune response creativity and length.

- **Add new LLM prompts**  
  1. Define a new `PromptTemplate` in `agents/chains.py`.  
  2. Create an `LLMChain` with your template (and optional `ConversationBufferMemory`).  
  3. Include it in the `SequentialChain` (`parent_chain`) so it runs as part of the workflow.

- **Swap or extend image sources**  
  In `clients/wiki_client.py`, replace or augment the Wikipedia fetcher—e.g. integrate Unsplash, Google Images, or another API by writing a new client module.

- **Customize Google snippet logic**  
  In `clients/serper_client.py`, adjust the query parameters (like `num`) or parse additional fields (e.g. source URLs, titles) from the SerperAPI response.

- **Streamlit UI tweaks**  
  - Change layout in `pages/search_page.py` by using `st.columns`, `st.tabs`, or adding custom CSS via:
    ```python
    st.markdown(
      "<style>...your CSS here...</style>",
      unsafe_allow_html=True
    )
    ```  
  - Add new pages: update the `st.sidebar.radio` in `app.py`, then create corresponding modules under `pages/`.

- **Theming**  
  Add a `.streamlit/theme.toml` file to control colors, fonts, and layout presets.  
  ```toml
  [theme]
  primaryColor = "#1f77b4"
  backgroundColor = "#f5f5f5"
  font = "sans serif"
