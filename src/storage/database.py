from sqlalchemy import create_engine
from src.config.config import load_settings

settings = load_settings()
print(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)