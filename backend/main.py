from fastapi import FastAPI
from core.config import settings
from db.session import eng
from db.base import BASE


def create_tables():
    BASE.metadata.create_all(bind=eng)


def start_app():
    app = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion)
    create_tables()
    return app


app = start_app()


@app.get("/")
def hi():
    return {'message': 'Hello World!'}
