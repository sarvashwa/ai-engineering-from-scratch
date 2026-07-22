import time
import logging

from litellm import completion

from src.config.config import Settings
from src.utils.timer import Timer
from src.context.request_context import get_request_id

logger = logging.getLogger(__name__)
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
        
    def generate_response_stream(self, prompt: str):

        with Timer("Total Request"):
            request = {
                "model": self._model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": self._temperature,
                "max_tokens": self._max_tokens,
                "stream": True,
            }

            try:
                with Timer("LLM Total"):

                    ttft_start = time.perf_counter()
                    response = completion(**request, base_url=self._base_url)

                    is_first_token = True
                    for chunk in response:
                        
                        if is_first_token:
                            ttft = (time.perf_counter() - ttft_start) * 1000
                            logger.info(f"TTFT took {ttft:.2f} ms")
                            first_token_generated_at = time.perf_counter()
                            is_first_token = False

                        token = chunk.choices[0].delta.content
                        if token is not None:
                            yield token
                    generation = (time.perf_counter() - first_token_generated_at) * 1000
                    logger.info(f"Generation took {generation:.2f} ms")
                    
            except Exception as error:
                print(f"Error generating response: {error}")
                raise RuntimeError(
                    f"Failed to generate response: {error}"
                ) from error