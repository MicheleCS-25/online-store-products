import os

import httpx
from dotenv import load_dotenv

load_dotenv()

FAKE_STORE_URL = os.getenv(
    "FAKE_STORE_URL",
    "https://fakestoreapi.com"
)


def get_products_from_fake_store():
    response = httpx.get(
        f"{FAKE_STORE_URL}/products",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def get_product_from_fake_store(
    product_id: int
):
    response = httpx.get(
        f"{FAKE_STORE_URL}/products/{product_id}",
        timeout=10
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return response.json()
