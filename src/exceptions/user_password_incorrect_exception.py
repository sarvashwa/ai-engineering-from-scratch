class UserPasswordIncorrectException(Exception):
    """Exception raised when a user password is incorrect."""

    def __init__(self):
        super().__init__(
            f"User password is incorrect"
        )