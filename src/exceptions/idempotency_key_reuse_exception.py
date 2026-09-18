class IdempotencyKeyReuseException(Exception):
    """Raised when an idempotency key is reused."""

    def __init__(self, idempotency_key: str):
        self.idempotency_key = idempotency_key
        super().__init__(
            f"Idempotency key {self.idempotency_key} was already used for different request."
            )