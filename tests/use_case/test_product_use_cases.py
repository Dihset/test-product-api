import pytest

from src.domain.use_cases import (
    CreateProductUseCase,
    DeleteProductUseCase,
    GetProductListUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)
from tests.mocks.factories import (
    CreateProductCommandFactory,
    DeleteProductCommandFactory,
    GetProductCommandFactory,
    GetProductListCommandFactory,
    UpdateProductCommandFactory,
)


@pytest.fixture
def mock_get_product_list_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductListUseCase)


@pytest.fixture
def mock_get_product_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductUseCase)


@pytest.fixture
def mock_create_product_use_case(mock_test_container):
    return mock_test_container.resolve(CreateProductUseCase)


@pytest.fixture
def mock_update_product_use_case(mock_test_container):
    return mock_test_container.resolve(UpdateProductUseCase)


@pytest.fixture
def mock_delete_product_use_case(mock_test_container):
    return mock_test_container.resolve(DeleteProductUseCase)


async def test_get_product_list(mock_get_product_list_use_case):
    command = GetProductListCommandFactory.build()
    products, _ = await mock_get_product_list_use_case.execute(command)

    assert len(products) < command.pagination.limit


async def test_get_product_by_id(mock_get_product_use_case):
    command = GetProductCommandFactory.build()
    product = await mock_get_product_use_case.execute(command)

    assert product.oid == command.oid


async def test_create_product(mock_create_product_use_case):
    command = CreateProductCommandFactory.build()
    product = await mock_create_product_use_case.execute(command)

    assert product == command.product


async def test_update_product(mock_update_product_use_case):
    command = UpdateProductCommandFactory.build()
    product = await mock_update_product_use_case.execute(command)

    assert product == command.product


async def test_delete_product(mock_delete_product_use_case):
    command = DeleteProductCommandFactory.build()
    product = await mock_delete_product_use_case.execute(command)

    assert product.oid == command.oid
