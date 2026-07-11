from litellm import completion
from src.config.config import Settings

class LLMService:
    def __init__(self, settings: Settings):
        self._model = settings.LLM_MODEL
        self._base_url = settings.LLM_BASE_URL
        self._temperature = settings.LLM_TEMPERATURE
        self._max_tokens = settings.LLM_MAX_TOKENS

    def generate_response(self, prompt: str) -> str:
        request = {
            "model": self._model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": self._temperature,
            "max_tokens": self._max_tokens,
        }

        try:
            response = completion(**request, base_url=self._base_url)
            return response.choices[0].message.content
        except Exception as error:
            print(f"Error generating response: {error}")
            raise RuntimeError(
                f"Failed to generate response: {error}"
            ) from error