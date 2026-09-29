from app import models
from fastapi import FastAPI

from app.database import engine
from app.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine) # it is used to create the tables in the database based on the models defined in app/models.py

@app.get("/")
def root():
    return {"message": "Python CRUD API is running"}