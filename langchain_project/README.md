# PyMentor AI - LangChain Python Doubt Solver

**Project type:** AI Question-Answering Chatbot  
**Topic selected:** Python Doubt Solver  
**Core stack:** Python + LangChain + Google Gemini + python-dotenv

## Project Objective

Build a simple chatbot with LangChain that accepts a user question and returns an AI-generated answer. This implementation is intentionally beginner-friendly and follows the required mini-project structure.

## Features

- Uses **Google Gemini** as the language model.
- Uses a **LangChain PromptTemplate** to control answer style.
- Accepts a **user question** from the console.
- Displays an **AI-generated answer**.
- Stores the API key in a private **`.env` file**.
- Includes input validation and basic API/setup error handling.
- Supports repeated questions until the user types `exit` or `quit`.
- Supports a one-question command-line mode.

## Files

```text
langchain_project/
├── app.py
├── .env
├── .env.example
├── requirements.txt
├── README.md
├── .gitignore
├── run.bat
├── self_test.py
└── TEST_QUESTIONS.md
```

The four files specifically suggested in the assignment are `app.py`, `.env`, `requirements.txt`, and `README.md`.

## Setup and Run

### Windows - easiest method

1. Put your Gemini API key in `.env` after `GOOGLE_API_KEY=`.
2. Double-click `run.bat`.

The script creates a virtual environment, installs dependencies, and starts the chatbot.

### Manual method

```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

On macOS/Linux, activate with:

```bash
source .venv/bin/activate
```

## API Key

Create a Gemini API key in Google AI Studio, then edit `.env`:

```env
GOOGLE_API_KEY=your_real_key_here
GEMINI_MODEL=gemini-3.8-flash
```

Never publish a real `.env` file. The included `.gitignore` protects it from accidental Git commits.

## How the LangChain Flow Works

```text
User question
    ↓
Input validation
    ↓
LangChain PromptTemplate
    ↓
ChatGoogleGenerativeAI (Gemini)
    ↓
StrOutputParser
    ↓
Answer printed to the console
```

The central LangChain pipeline is created with:

```python
chain = prompt | llm | StrOutputParser()
```

and each question is passed using:

```python
chain.invoke({"question": cleaned_question})
```

## Five Required Test Questions

Use these exact questions for a live demonstration:

1. What is a Python list and how is it different from a tuple?
2. Explain the difference between `=` and `==` in Python.
3. Write a Python function to check whether a number is prime.
4. What does `range(1, 6)` produce and why?
5. Why do I get `TypeError: can only concatenate str (not "int") to str`?

More test details are in `TEST_QUESTIONS.md`.

## Error Handling Included

The app handles:

- Empty questions.
- Questions longer than 2000 characters.
- Missing or placeholder API key.
- Missing Python packages.
- Network/API/quota/model errors.
- Empty model responses.
- Keyboard interruption and end-of-file input.

## Security

- The API key is read only from `.env`.
- `.env` is ignored by Git.
- The key is never hard-coded into `app.py`.
- `.env.example` can be shared safely because it contains only a placeholder.

## Offline Self-Test

Run:

```bash
python self_test.py
```

This validates the project structure, Python syntax, prompt template, input validation, and five-question application flow using a local test double. A live Gemini call still requires a valid user-owned API key.

## Expected Result

After startup, the console displays the chatbot title. The user enters a Python question, LangChain formats it with the prompt template, Gemini generates the answer, and the response is displayed. The loop continues until `exit` or `quit` is entered.
