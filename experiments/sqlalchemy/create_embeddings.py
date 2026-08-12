from sqlalchemy.orm import Session

from src.storage.database import SessionLocal
from src.storage.models.document import Document
from src.storage.models.embedding import Embedding

session: Session = SessionLocal()
document = session.get(Document, 10)

embedding_1 = Embedding(
    document=document,
)

embedding_2 = Embedding(
    document=document,
)

embedding_3 = Embedding(
    document=document,
)

session.add_all([
    embedding_1,
    embedding_2,
    embedding_3
])

session.commit()

print(document.embeddings)
print(embedding_1.document.title)