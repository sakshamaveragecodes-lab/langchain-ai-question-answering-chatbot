# Test Questions and Expected Behaviour

These five questions cover concepts, syntax, code generation, built-in functions, and debugging.

| # | Test question | What a good answer should contain |
|---|---|---|
| 1 | What is a Python list and how is it different from a tuple? | Lists are mutable; tuples are immutable; both are ordered sequences; small examples. |
| 2 | Explain the difference between `=` and `==` in Python. | `=` assigns a value; `==` compares values; examples showing both. |
| 3 | Write a Python function to check whether a number is prime. | Correct handling of numbers below 2; loop only as far as needed; returns Boolean. |
| 4 | What does `range(1, 6)` produce and why? | Values 1 through 5; stop value is excluded. |
| 5 | Why do I get `TypeError: can only concatenate str (not "int") to str`? | Explains string/int mismatch and fixes using `str()` or numeric conversion as appropriate. |

## Additional negative tests

- Empty input -> `Question cannot be empty.`
- More than 2000 characters -> friendly validation error.
- Missing API key -> setup error explaining how to configure `.env`.
- API/network failure -> friendly error instead of a raw traceback.

## Live-test note

The software flow is also covered by `self_test.py` with a local fake chain. To verify real AI generation, add a valid Gemini API key to `.env` and run the five questions above through `python app.py`.
