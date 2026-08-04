from sqlalchemy.orm import Session

from src.storage.database import SessionLocal
from src.storage.models.document import Document

session: Session = SessionLocal()

try:
    document = Document(
        title="Python.pdf"
    )

    session.add(document)

    session.commit()

    print(document.id)

finally:
    session.close()