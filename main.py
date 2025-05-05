from fastapi import FastAPI

from app import kairos

app = FastAPI(title="Kairos FastAPI Ver")
app.include_router(router=kairos)
