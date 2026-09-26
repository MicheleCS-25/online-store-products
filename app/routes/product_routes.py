from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import product_controller
from app.db.database import get_db
from app.schemas import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)
from app.services import fake_store_service
from app.services import product_service


# O router tem de ser criado ANTES das rotas
router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=201,
    summary="Criar produto",
    description="Cria um novo produto."
)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db)
):
    return product_controller.create_product_controller(
        db,
        product_data,
        product_service
    )


@router.get(
    "",
    response_model=list[ProductResponse],
    summary="Listar produtos",
    description="Retorna todos os produtos guardados na SQLite."
)
def get_products(
    db: Session = Depends(get_db)
):
    return product_controller.get_products_controller(
        db,
        product_service
    )


# Importação da Fake Store API
@router.post(
    "/import",
    response_model=list[ProductResponse],
    summary="Importar produtos",
    description="Importa produtos da Fake Store API para a SQLite."
)
def import_products(
    db: Session = Depends(get_db)
):
    products = fake_store_service.get_products_from_fake_store()

    return product_service.import_products(
        db,
        products
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Obter produto",
    description="Retorna um produto através do seu ID."
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return product_controller.get_product_controller(
        db,
        product_id,
        product_service
    )


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Atualizar produto",
    description="Atualiza os dados de um produto."
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    return product_controller.update_product_controller(
        db,
        product_id,
        product_data,
        product_service
    )


@router.delete(
    "/{product_id}",
    summary="Eliminar produto",
    description="Elimina um produto através do seu ID."
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return product_controller.delete_product_controller(
        db,
        product_id,
        product_service
    )