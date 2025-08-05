from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    product_code: str
    brand: str
    price: int
    in_stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductUpdate(ProductBase):
    name: str | None = None
    description: str | None = None
    product_code: str | None = None
    brand: str | None = None
    price: int | None = None
    in_stock: int | None = None
