from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Python CRUD API is running"}