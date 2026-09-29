from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    quantity: int

    # from_attributes=True tells Pydantic that it can build the response model from an object's attributes.
    model_config = ConfigDict(from_attributes=True)
    