from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.session import engine
from db.base import Base  # Import models here to ensure they are created

from api.api_v1.api import api_router

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_app():
    app = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion)
    create_tables()
    return app

app = get_application()
