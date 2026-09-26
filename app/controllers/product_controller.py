from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas import ProductCreate, ProductUpdate


def create_product_controller(
    db: Session,
    product_data: ProductCreate,
    service
):
    return service.create_product(
        db,
        product_data
    )


def get_products_controller(
    db: Session,
    service
):
    return service.get_products(db)


def get_product_controller(
    db: Session,
    product_id: int,
    service
):
    product = service.get_product(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def update_product_controller(
    db: Session,
    product_id: int,
    product_data: ProductUpdate,
    service
):
    product = service.update_product(
        db,
        product_id,
        product_data
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


def delete_product_controller(
    db: Session,
    product_id: int,
    service
):
    product = service.delete_product(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully"
    }