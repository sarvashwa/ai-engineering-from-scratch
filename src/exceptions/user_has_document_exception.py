class UserHasDocumentException(Exception):
    """Exception raised when a user has associated documents and cannot be deleted."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__(
            f"User with ID {user_id} cannot be deleted because "
            f"documents still belong to this user."
            )