# Online Store — Products Service

O **Products Service** é responsável pela gestão dos produtos da aplicação Online Store.

O serviço disponibiliza uma API REST desenvolvida com **FastAPI**, utiliza **SQLite** para persistência e integra-se com a **Fake Store API** para importação de produtos externos.

## Tecnologias

* Python 3
* FastAPI
* SQLAlchemy
* SQLite
* HTTPX
* Uvicorn
* Docker
* Fake Store API

## Funcionalidades

O serviço permite:

* Criar produtos
* Listar produtos
* Consultar um produto por ID
* Atualizar produtos
* Eliminar produtos
* Importar produtos da Fake Store API

## Estrutura

```text
products-service/
├── app/
│   ├── controllers/
│   ├── routes/
│   ├── services/
│   ├── db/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
├── .env
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## API

Porta:

```text
3002
```

API:

```text
http://localhost:3002
```

Swagger:

```text
http://localhost:3002/docs
```

## Endpoints

| Método | Endpoint           | Descrição                           |
| ------ | ------------------ | ----------------------------------- |
| GET    | `/`                | Verificar o estado do serviço       |
| POST   | `/products`        | Criar um produto                    |
| GET    | `/products`        | Listar produtos                     |
| GET    | `/products/{id}`   | Consultar um produto                |
| PUT    | `/products/{id}`   | Atualizar um produto                |
| DELETE | `/products/{id}`   | Eliminar um produto                 |
| POST   | `/products/import` | Importar produtos da Fake Store API |

## Fake Store API

O serviço comunica com a Fake Store API através de HTTP para obter produtos externos.

A URL é configurada através da variável:

```text
FAKE_STORE_URL
```

Por padrão:

```text
https://fakestoreapi.com
```

Os produtos obtidos podem ser armazenados na base de dados SQLite do serviço.

## Persistência

A configuração da base de dados utiliza:

```text
DATABASE_URL
```

Na execução através de Docker é utilizado um volume para preservar os dados.

## Executar com Docker

### Construir a imagem

```bash
docker build -t online-store-products .
```

### Executar o container

```bash
docker run --name products-service -p 3002:3002 -e DATABASE_URL=sqlite:////data/products.db -e FAKE_STORE_URL=https://fakestoreapi.com -v products_data:/data online-store-products
```

Swagger:

```text
http://localhost:3002/docs
```

## Importar produtos

Com o serviço em execução, utilizar:

```http
POST /products/import
```

A operação também pode ser realizada diretamente através do Swagger.

Depois da importação, os produtos podem ser consultados através de:

```http
GET /products
```

## Executar localmente

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 3002
```

## Integração no sistema

O Products Service é utilizado pelo **Orders Service**.

Antes de criar uma encomenda, o Orders Service consulta esta API através de REST para verificar a existência do produto e obter as informações necessárias para calcular o valor da encomenda.
