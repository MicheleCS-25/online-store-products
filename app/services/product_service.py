from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    product_data: ProductCreate
):
    product = Product(
        title=product_data.title,
        price=product_data.price,
        category=product_data.category,
        description=product_data.description,
        image=product_data.image
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_products(db: Session):
    return db.query(Product).all()


def get_product(
    db: Session,
    product_id: int
):
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):
    product = get_product(
        db,
        product_id
    )

    if product is None:
        return None

    product.title = product_data.title
    product.price = product_data.price
    product.category = product_data.category
    product.description = product_data.description
    product.image = product_data.image

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product_id: int
):
    product = get_product(
        db,
        product_id
    )

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product

def import_products(
    db: Session,
    products
):
    imported_products = []

    for product_data in products:
        existing_product = get_product(
            db,
            product_data["id"]
        )

        if existing_product:
            continue

        product = Product(
            id=product_data["id"],
            title=product_data["title"],
            price=product_data["price"],
            category=product_data["category"],
            description=product_data.get("description"),
            image=product_data.get("image")
        )

        db.add(product)
        imported_products.append(product)

    db.commit()

    for product in imported_products:
        db.refresh(product)

    return imported_products