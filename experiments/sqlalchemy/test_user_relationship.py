from sqlalchemy.orm import Session

from src.storage.database import SessionLocal
from src.storage.models.document import Document
from src.storage.models.user import User

session: Session = SessionLocal()

try:
    user = User(name="Sarvashwa")

    document = Document(
        title="python.pdf",
        summary="Python notes",
        user=user,
    )

    session.add(user)
    session.add(document)
    session.commit()

    print(document.user.name)
    print(user.documents)

finally:
    session.close()