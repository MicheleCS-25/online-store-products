from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    category = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(1000),
        nullable=True
    )

    image = Column(
        String(500),
        nullable=True
    )