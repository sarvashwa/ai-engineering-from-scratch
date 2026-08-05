from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import load_settings
from src.storage.models.base import Base
import src.storage.models

settings = load_settings()

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base.metadata.create_all(engine)

print("Tables created successfully!")