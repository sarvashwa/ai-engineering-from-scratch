from sqlalchemy.orm import Session

from src.storage.database import SessionLocal
from src.storage.models.document import Document

session: Session = SessionLocal()

try:
    document = session.get(Document, 1)

    session.delete(document)

    session.commit()

finally:
    session.close()