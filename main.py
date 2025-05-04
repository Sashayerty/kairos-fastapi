from fastapi import FastAPI

from app import kairos

app = FastAPI()
app.include_router(router=kairos)
