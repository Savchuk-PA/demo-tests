from .base import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Product(Base):

    name: str
    description: str
    product_code: str
    brand: str
    price: int
    in_stock: int
