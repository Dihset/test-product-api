from fastapi import APIRouter

from src.api.v1.views import products


api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])

