# Viva Guide - PyMentor AI LangChain Mini-Project

1. **What is the project?**  
   PyMentor AI is a Python doubt-solving chatbot. It accepts a user question and sends it through a LangChain prompt-and-model pipeline to Google Gemini.

2. **Why did you choose this topic?**  
   A Python doubt solver is easy to demonstrate and directly shows how an LLM can support learners with explanations, examples, and debugging help.

3. **What is LangChain?**  
   LangChain is a framework for building applications around language models. It provides reusable components such as prompts, models, parsers, retrievers, tools, and runnable chains.

4. **Which LLM is used?**  
   Google Gemini, configured as `gemini-3.8-flash`.

5. **Which LangChain class connects to Gemini?**  
   `ChatGoogleGenerativeAI` from `langchain_google_genai`.

6. **What is a prompt template?**  
   A prompt template is a reusable instruction with variables. In this project, `{question}` is replaced by the user's input.

7. **Why use a prompt template instead of sending the raw question?**  
   It makes responses more consistent by defining the bot's role, scope, tone, and answer rules.

8. **What is the chain in this project?**  
   `prompt | llm | StrOutputParser()` - prompt formatting, then Gemini generation, then conversion to plain text.

9. **What does `chain.invoke()` do?**  
   It executes the pipeline once with the supplied input dictionary.

10. **Why is `.env` used?**  
    It stores configuration such as the API key outside the source code.

11. **Why should the API key not be hard-coded?**  
    Hard-coded secrets can leak when code is shared or uploaded to Git repositories.

12. **What does python-dotenv do?**  
    It loads values from `.env` into environment variables so Python can read them with `os.getenv()`.

13. **What input validation is used?**  
    Empty input is rejected, whitespace is normalized, and questions longer than 2000 characters are rejected.

14. **What error handling is present?**  
    The app handles missing dependencies, missing API keys, network/API failures, empty model responses, invalid questions, and user interruption.

15. **How is the user input taken?**  
    With Python's `input()` function inside a loop.

16. **How does the user exit?**  
    By typing `exit` or `quit`, or by interrupting the program.

17. **What is `StrOutputParser`?**  
    It converts the LangChain model response into plain text that can be printed cleanly.

18. **Why is the model temperature low?**  
    A low value such as 0.2 encourages more consistent and focused educational answers.

19. **What are the limitations?**  
    The app needs internet access and a valid Gemini API key, model output can still contain mistakes, and it does not store conversation memory.

20. **How can the project be extended?**  
    Add a graphical interface, conversation memory, document-based RAG, code execution in a sandbox, authentication, logging, or topic-specific knowledge sources.
