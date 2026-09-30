from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session


from app.database import SessionLocal, engine
from app.models import Base, Product
from app.schemas.product import ProductCreate, ProductResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/products", response_model=ProductResponse)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    product = Product(
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        quantity=product_data.quantity  
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()

    return products

@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        return {"message": "Product not found"}

    return product

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    pName: str,
    pDescription: str,
    pPrice: float,
    pQuantity: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        return {"message": "Product not found"}

    product.name = pName
    product.description = pDescription
    product.price = pPrice
    product.quantity = pQuantity

    db.commit()
    db.refresh(product)

    return product

@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        return {"message": "Product not found"}

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }