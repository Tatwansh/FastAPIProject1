from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from core.config import settings

# Creation of Engine
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL: ", SQLALCHEMY_DATABASE_URL)
eng = create_engine(SQLALCHEMY_DATABASE_URL)

# Session Generation
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=eng)


def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
# Useful for testing
