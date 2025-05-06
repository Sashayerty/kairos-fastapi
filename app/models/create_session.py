from sqlmodel import Session, SQLModel, create_engine

from app.models.__all_models import *  # noqa


def get_session():
    with Session(engine) as session:
        yield session
