from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen


class ProductBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(64)] = Field(
        description="Наименование продукта"
    )
    description: Annotated[str, MinLen(2), MaxLen(512)] = Field(
        description="Описание продукта"
    )
    product_code: Annotated[str, MinLen(6), MaxLen(128)] = Field(
        description="Артикул продукта"
    )
    brand: Annotated[str, MinLen(1), MaxLen(32)] = Field(description="Бренд продукта")
    price: int = Field(gt=0, description="Цена должна быть положительной")


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=64)
    description: str | None = Field(default=None, min_length=2, max_length=512)
    product_code: str | None = Field(default=None, min_length=2, max_length=32)
    brand: str | None = Field(default=None, min_length=1, max_length=128)
    price: int | None = Field(default=None, gt=0)
