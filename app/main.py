from app import models
from fastapi import FastAPI
from sqlalchemy.orm import Session


from app.database import SessionLocal, engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Python CRUD API is running"}