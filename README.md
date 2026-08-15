# Restaurant Idea Generator

Generate a creative restaurant name and menu items for any cuisine using OpenAI and LangChain.

## Features

- Pick a cuisine and get a branded restaurant name
- Get 6 tailored menu item suggestions
- Simple Streamlit web UI with loading and error states
- API key stored in `.env` (not committed to git)

## Setup

### 1. Create a virtual environment

```powershell
cd RestrauntIdeaGen
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

```powershell
copy .env.example .env
```

Edit `.env` and set your key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

Get a key at [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

### 4. Run the app

```powershell
streamlit run main.py
```

Your browser will open at `http://localhost:8501`. Pick a cuisine in the sidebar and click **Generate ideas**.

## Test from the command line

```powershell
python langchain_helper.py
```

## Project structure

```
RestrauntIdeaGen/
├── main.py              # Streamlit UI
├── langchain_helper.py  # LangChain + OpenAI logic
├── requirements.txt
├── .env.example
└── README.md
```

## Tech stack

- Python
- [LangChain](https://python.langchain.com/) (LCEL chains, ChatOpenAI)
- OpenAI GPT-4o-mini
- Streamlit
## Recent Updates

- Improved project documentation
- Updated project setup instructions 