from fastapi import FastAPI
from core.config import settings
from db.session import eng
from db.base import BASE
from apiS.base import api_router


def create_tables():
    BASE.metadata.create_all(bind=eng)


def include_router(appl):
    appl.include_router(api_router)


def start_app():
    appl = FastAPI(title=settings.ProjectName, version=settings.ProjectVersion)
    create_tables()
    include_router(appl)
    return appl


app = start_app()


@app.get("/")
def hi():
    return {'message': 'Hello World!'}
