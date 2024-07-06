import punq
from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.schemas import (
    ApiResponse,
    ListPaginatedResponse,
    ProductInSchema,
    ProductOutSchema,
)
from src.core.container import get_container
from src.domain.commands import (
    CreateProductCommand,
    DeleteProductCommand,
    GetProductCommand,
    UpdateProductCommand,
)
from src.domain.errors import ProductNotFoundException
from src.domain.use_cases import (
    CreateProductUseCase,
    DeleteProductUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)

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
async def create_product_views(
    product_in: ProductInSchema,
    container: punq.Container = Depends(get_container),
) -> ApiResponse[ProductOutSchema]:
    use_case: CreateProductUseCase = container.resolve(CreateProductUseCase)
    command = CreateProductCommand(product=product_in.to_entity())
    product = await use_case.execute(command)
    return ApiResponse(data=ProductOutSchema.from_entity(product))


@router.get(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
async def get_product_views(
    oid: str,
    container: punq.Container = Depends(get_container),
) -> ApiResponse[ProductOutSchema]:
    use_case: GetProductUseCase = container.resolve(GetProductUseCase)
    command = GetProductCommand(oid=oid)
    try:
        product = await use_case.execute(command)
    except ProductNotFoundException as error:
        raise HTTPException(status_code=404, detail="Product not found") from error
    else:
        return ApiResponse(data=ProductOutSchema.from_entity(product))


@router.put(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
async def update_product_views(
    oid: str,
    product_in: ProductInSchema,
    container: punq.Container = Depends(get_container),
) -> ApiResponse[ProductOutSchema]:
    use_case: UpdateProductUseCase = container.resolve(UpdateProductUseCase)
    command = UpdateProductCommand(product=product_in.to_entity(oid=oid))
    product = await use_case.execute(command)
    return ApiResponse(data=ProductOutSchema.from_entity(product))


@router.delete(
    "/{oid}",
    response_model=ApiResponse[ProductOutSchema],
)
async def delete_product_views(
    oid: str,
    container: punq.Container = Depends(get_container),
) -> ApiResponse[ProductOutSchema]:
    use_case: DeleteProductUseCase = container.resolve(DeleteProductUseCase)
    command = DeleteProductCommand(oid=oid)
    try:
        product = await use_case.execute(command)
    except ProductNotFoundException as error:
        raise HTTPException(status_code=404, detail="Product not found") from error
    else:
        return ApiResponse(data=ProductOutSchema.from_entity(product))
