from fastapi import APIRouter

from src.api.v1.schemas import ApiResponse, ListPaginatedResponse, ProductOutSchema

router = APIRouter()


@router.get(
    "/",
    response_model=ApiResponse[ListPaginatedResponse[ProductOutSchema]],
)
def find_many_products_views() -> ApiResponse[ListPaginatedResponse[ProductOutSchema]]:
    pass


@router.post(
    "/",
    response_model=ApiResponse[ProductOutSchema],
)
def create_product_views() -> ApiResponse[ProductOutSchema]:
    pass


@router.get(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
def get_product_views() -> ApiResponse[ProductOutSchema]:
    pass


@router.put(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
def update_product_views() -> ApiResponse[ProductOutSchema]:
    pass


@router.delete(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
def delete_product_views() -> ApiResponse[ProductOutSchema]:
    pass
