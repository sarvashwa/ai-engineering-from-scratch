from src.services.llm_service import LLMService

llm_service = LLMService()

prompt = """
You are a helpful AI assistant.

Use ONLY the provided context to answer the user's question.

If the answer cannot be found in the context, say:
"I don't have enough information to answer that."

Context:

MongoDB stores patient and application data.

Question:
How does MongoDB store patient data?

Answer:
"""

response = llm_service.generate_response(prompt)

print("=" * 80)
print("LLM RESPONSE")
print("=" * 80)
print(response)