import punq
from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.schemas import (
    ApiResponse,
    ListPaginatedResponse,
    PaginationOutSchema,
    ProductInSchema,
    ProductOutSchema,
)
from src.core.container import get_container
from src.domain.commands import (
    CreateProductCommand,
    DeleteProductCommand,
    GetProductCommand,
    GetProductListCommand,
    PaginationQuery,
    ProductSortQuery,
    SortOrderEnum,
    UpdateProductCommand,
)
from src.domain.entities import ProductSortFieldsEnum
from src.domain.errors import ProductNotFoundException
from src.domain.use_cases import (
    CreateProductUseCase,
    DeleteProductUseCase,
    GetProductListUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)

router = APIRouter()


def get_pagination(
    page: int = 0,
    limit: int = 10,
) -> PaginationQuery:
    return PaginationQuery(page=page, limit=limit)


def get_list_command_factory(
    search: str | None = None,
    pagination: PaginationQuery = Depends(get_pagination),
    sort_field: ProductSortFieldsEnum = ProductSortFieldsEnum.oid,
    sort_order: SortOrderEnum = SortOrderEnum.asc,
):
    return GetProductListCommand(
        search=search,
        pagination=pagination,
        sort=ProductSortQuery(
            field=sort_field.value,
            order=sort_order,
        ),
    )


@router.get(
    "/",
    response_model=ApiResponse[ListPaginatedResponse[ProductOutSchema]],
)
async def find_many_products_views(
    command: GetProductListCommand = Depends(get_list_command_factory),
    container: punq.Container = Depends(get_container),
) -> ApiResponse[ListPaginatedResponse[ProductOutSchema]]:
    use_case: GetProductListUseCase = container.resolve(GetProductListUseCase)
    products, count = await use_case.execute(command)

    response = ListPaginatedResponse(
        items=[ProductOutSchema.from_entity(product) for product in products],
        pagination=PaginationOutSchema(
            page=command.pagination.page,
            limit=command.pagination.limit,
            total=count,
        ),
    )
    return ApiResponse(data=response)


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
