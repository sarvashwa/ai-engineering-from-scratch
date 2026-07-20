from src.services.llm_service import LLMService
from src.config.config import load_settings

settings = load_settings()
llm_service = LLMService(settings)

prompt = """
You are a helpful AI assistant.

Use ONLY the provided context to answer the user's question.

Context:

MongoDB stores patient and application data.

Question:
How does MongoDB store patient data?

Answer:
"""

response = llm_service.generate_stream_response(prompt)

print("=" * 80)
print("LLM RESPONSE")
print("=" * 80)

for token in response:
    print(token, end="", flush=True)