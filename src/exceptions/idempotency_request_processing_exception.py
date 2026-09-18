class IdempotencyRequestProcessingException(Exception):
    
    def __init__(self, key: str):
        super().__init__(
            f"Request with idempotency key '{key}' is already processing."
        )