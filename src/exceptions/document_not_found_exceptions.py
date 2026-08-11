class DocumentNotFoundException(Exception):
    def __init__(self, document_id: int):
        super().__init__(f"Document with ID {document_id} was not found.")