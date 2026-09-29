from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


from app.database import SessionLocal, engine
from app.models import Base, Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()

    return products

@app.post("/products")
def create_product(
    name: str,
    description: str,
    price: float,
    quantity: int,
    db: Session = Depends(get_db)
):
    product = Product(
        name=name,
        description=description,
        price=price,
        quantity=quantity
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product