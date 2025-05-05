from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from app import kairos
from flask_version import app as flask_app

app = FastAPI(title="Kairos FastAPI Ver")
app.include_router(router=kairos)
app.mount("/", WSGIMiddleware(flask_app))
