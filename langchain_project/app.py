"""PyMentor AI - LangChain + Gemini question-answering chatbot.

Mini-project implementation based on the UNLOX LangChain guidelines.
The application intentionally keeps the interface simple: the user enters a
Python question and receives an AI-generated answer through a LangChain chain.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent
ENV_FILE = PROJECT_DIR / ".env"
DEFAULT_MODEL = "gemini-3.8-flash"

PROMPT_TEMPLATE = """
You are PyMentor AI, a patient and accurate Python study assistant for beginners.

Rules:
- Answer the user's Python or programming question clearly and correctly.
- Start with a direct explanation in simple language.
- Include a short Python example when it improves understanding.
- Explain important code line by line when the question is beginner-level.
- If there is a common mistake, mention it briefly.
- If the question is outside Python/programming, politely say that this bot is
  focused on Python learning and ask for a Python-related question.
- Do not invent code output. If output depends on an input or Python version,
  state the assumption.
- Keep the answer useful and reasonably concise.

User question:
{question}

Answer:
""".strip()


def validate_question(question: str) -> str:
    """Clean and validate user input before it is sent to the model."""
    cleaned = " ".join(question.strip().split())
    if not cleaned:
        raise ValueError("Question cannot be empty.")
    if len(cleaned) > 2000:
        raise ValueError("Question is too long. Please keep it under 2000 characters.")
    return cleaned


def load_settings() -> tuple[str, str]:
    """Load the Gemini API key and model name from the .env file."""
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise RuntimeError(
            "python-dotenv is not installed. Run: pip install -r requirements.txt"
        ) from exc

    load_dotenv(ENV_FILE)
    api_key = os.getenv("GOOGLE_API_KEY", "").strip()
    model_name = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL

    placeholder_values = {
        "YOUR_GEMINI_API_KEY_HERE",
        "PASTE_YOUR_GEMINI_API_KEY_HERE",
        "your_api_key_here",
    }
    if not api_key or api_key in placeholder_values:
        raise RuntimeError(
            "GOOGLE_API_KEY is missing. Put your Gemini API key in the .env file "
            "as GOOGLE_API_KEY=your_key_here."
        )

    return api_key, model_name


def build_chain() -> Any:
    """Create the LangChain prompt -> Gemini -> text parser pipeline."""
    api_key, model_name = load_settings()

    try:
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.prompts import PromptTemplate
        from langchain_google_genai import ChatGoogleGenerativeAI
    except ImportError as exc:
        raise RuntimeError(
            "LangChain dependencies are not installed. Run: pip install -r requirements.txt"
        ) from exc

    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
    )

    return prompt | llm | StrOutputParser()


def ask_question(chain: Any, question: str) -> str:
    """Send one validated question through the LangChain pipeline."""
    cleaned = validate_question(question)
    try:
        answer = chain.invoke({"question": cleaned})
    except Exception as exc:
        raise RuntimeError(
            "The AI request failed. Check your internet connection, API key, "
            "Gemini quota, and model availability, then try again."
        ) from exc

    answer_text = str(answer).strip()
    if not answer_text:
        raise RuntimeError("The model returned an empty response. Please try again.")
    return answer_text


def print_header(model_name: str) -> None:
    print("=" * 66)
    print(" PyMentor AI - Python Doubt Solver")
    print(f" Powered by LangChain + Google Gemini ({model_name})")
    print(" Type 'exit' or 'quit' to close the chatbot.")
    print("=" * 66)


def run_interactive() -> int:
    """Run the console chatbot until the user exits."""
    try:
        _api_key, model_name = load_settings()
        chain = build_chain()
    except RuntimeError as exc:
        print(f"\nSetup error: {exc}\n")
        return 1

    print_header(model_name)

    while True:
        try:
            question = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return 0

        if question.lower() in {"exit", "quit"}:
            print("PyMentor AI: Goodbye! Keep practicing Python.")
            return 0

        try:
            answer = ask_question(chain, question)
            print(f"\nPyMentor AI:\n{answer}")
        except ValueError as exc:
            print(f"Input error: {exc}")
        except RuntimeError as exc:
            print(f"AI error: {exc}")


def run_single_question(question: str) -> int:
    """Answer one command-line question and exit."""
    try:
        chain = build_chain()
        print(ask_question(chain, question))
        return 0
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


def main() -> int:
    if len(sys.argv) > 1:
        return run_single_question(" ".join(sys.argv[1:]))
    return run_interactive()


if __name__ == "__main__":
    raise SystemExit(main())
