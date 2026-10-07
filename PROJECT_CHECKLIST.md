# Assignment Requirement Checklist

| Guideline requirement | Status | Where implemented |
|---|---|---|
| AI Question-Answering Chatbot | Complete | `langchain_project/app.py` |
| Any allowed topic | Complete - Python Doubt Solver | `README.md`, prompt in `app.py` |
| One language model such as Gemini | Complete - Google Gemini | `ChatGoogleGenerativeAI` in `app.py` |
| Prompt template | Complete | `PROMPT_TEMPLATE` + `PromptTemplate.from_template()` |
| User question as input | Complete | Console input loop and one-shot CLI mode |
| AI-generated answer as output | Complete | LangChain chain output printed to console |
| API key stored in `.env` | Complete | `.env` + `python-dotenv` |
| Basic error handling | Complete | Input, setup, dependency and API error handling |
| `app.py` | Complete | Included |
| `.env` | Complete | Included with safe placeholder |
| `requirements.txt` | Complete | Included and version-pinned |
| `README.md` | Complete | Included |
| Python | Complete | Main implementation language |
| LangChain | Complete | Prompt + runnable chain |
| Gemini or another LLM | Complete | Gemini 3.8 Flash |
| Python Dotenv | Complete | Used in `load_settings()` |
| Test at least five questions | Complete at software-flow level | `self_test.py` + `TEST_QUESTIONS.md` |

## Verification note

All local/offline checks have been run successfully. A real Gemini response cannot be executed without a private user-owned API key; the project therefore contains a safe placeholder rather than fabricating or exposing a credential.
