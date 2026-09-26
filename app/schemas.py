from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    title: str
    price: float
    category: str
    description: str | None = None
    image: str | None = None


class ProductUpdate(BaseModel):
    title: str
    price: float
    category: str
    description: str | None = None
    image: str | None = None


class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    category: str
    description: str | None
    image: str | None

    model_config = ConfigDict(
        from_attributes=True
    )