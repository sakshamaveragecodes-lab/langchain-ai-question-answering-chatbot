"""Offline verification for the LangChain mini-project.

This test does not call Gemini or require third-party packages. It verifies the
local application logic and pushes five questions through ask_question() using
an in-memory fake chain.
"""

from __future__ import annotations

import ast
from pathlib import Path

import app

ROOT = Path(__file__).resolve().parent

TEST_QUESTIONS = [
    "What is a Python list and how is it different from a tuple?",
    "Explain the difference between = and == in Python.",
    "Write a Python function to check whether a number is prime.",
    "What does range(1, 6) produce and why?",
    'Why do I get TypeError: can only concatenate str (not "int") to str?',
]


class FakeChain:
    def __init__(self) -> None:
        self.seen: list[str] = []

    def invoke(self, values: dict[str, str]) -> str:
        question = values["question"]
        self.seen.append(question)
        return f"Validated test answer for: {question}"


def check(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    print(f"PASS - {name}")


def main() -> None:
    app_source = (ROOT / "app.py").read_text(encoding="utf-8")
    ast.parse(app_source)
    check(True, "app.py parses as valid Python")

    for filename in ["app.py", ".env", "requirements.txt", "README.md"]:
        check((ROOT / filename).is_file(), f"required file exists: {filename}")

    reqs = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    check("langchain==" in reqs, "LangChain dependency declared")
    check("langchain-google-genai==" in reqs, "Gemini LangChain integration declared")
    check("python-dotenv==" in reqs, "python-dotenv dependency declared")

    check("{question}" in app.PROMPT_TEMPLATE, "prompt template contains question variable")
    check("GOOGLE_API_KEY=" in (ROOT / ".env").read_text(encoding="utf-8"), ".env contains API key variable")

    fake = FakeChain()
    for index, question in enumerate(TEST_QUESTIONS, start=1):
        answer = app.ask_question(fake, question)
        check(bool(answer), f"test question {index} returns an output")
    check(len(fake.seen) == 5, "five questions passed through application flow")

    try:
        app.validate_question("   ")
    except ValueError:
        check(True, "empty input is rejected")
    else:
        raise AssertionError("empty input is rejected")

    try:
        app.validate_question("x" * 2001)
    except ValueError:
        check(True, "overlong input is rejected")
    else:
        raise AssertionError("overlong input is rejected")

    print("\nALL OFFLINE TESTS PASSED")
    print("Live Gemini connectivity is intentionally not tested without a private API key.")


if __name__ == "__main__":
    main()
