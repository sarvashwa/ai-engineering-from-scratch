import os

class Settings:
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )
    CHROMA_DB_PATH: str = os.getenv(
        "CHROMA_DB_PATH",
        "./chroma_data"
    )
    DEFAULT_TOP_K: int = int(
        os.getenv(
        "DEFAULT_TOP_K",
        "5"
        )
    )
    LLM_MODEL: str = os.getenv(
        "LLM_MODEL",
        "ollama/qwen2.5:latest"
    )
    LLM_BASE_URL: str = os.getenv(
        "LLM_BASE_URL",
        "http://localhost:11434"
    )
    LLM_TEMPERATURE: float = float(
        os.getenv(
        "LLM_TEMPERATURE",
        "0.7"
        )
    )
    LLM_MAX_TOKENS: int = int(
        os.getenv(
        "LLM_MAX_TOKENS",
        "1024"
        )
    )
    COLLECTION_NAME: str = os.getenv(
        "COLLECTION_NAME",
        "experiment_12"
    )

def load_settings() -> Settings:
    return Settings()
