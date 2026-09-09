class DocumentAccessDeniedException(Exception):
    
    def __init__(self, document_id: int):

        self.document_id = document_id

        super().__init__(
            f"Access denied for document with ID {document_id}."
        )