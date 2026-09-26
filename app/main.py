from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.db.database import Base, engine
from app.routes.product_routes import router as product_router

# Criar as tabelas no banco de dados
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Online Store - Products Service",
    description="""
    API REST responsável pela gestão
    dos produtos da Online Store.

    Este serviço permite:

    - Criar produtos
    - Consultar produtos
    - Atualizar produtos
    - Eliminar produtos
    - Importar produtos da Fake Store API

    A persistência é realizada utilizando SQLite.
    """,
    version="1.0.0"
)

# Permite as chamadas de frontend para o backend, mesmo que estejam em domínios diferentes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas de produto
app.include_router(product_router)


# Endpoint de verificação de estado
@app.get(
    "/",
    tags=["Health"],
    summary="Verificar estado do serviço"
)
def root():
    return {
        "service": "products-service",
        "status": "running"
    }