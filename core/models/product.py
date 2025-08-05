from .base import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Product(Base):

    name: Mapped[str]
    description: Mapped[str]
    product_code: Mapped[str]
    brand: Mapped[str]
    price: Mapped[int]
