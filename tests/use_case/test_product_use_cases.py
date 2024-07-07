import pytest

from src.domain.use_cases import (
    CreateProductUseCase,
    GetProductUseCase,
    UpdateProductUseCase,
)
from tests.mocks.factories import (
    CreateProductCommandFactory,
    GetProductCommandFactory,
    UpdateProductCommandFactory,
)


@pytest.fixture
def mock_get_product_use_case(mock_test_container):
    return mock_test_container.resolve(GetProductUseCase)


@pytest.fixture
def mock_create_product(mock_test_container):
    return mock_test_container.resolve(CreateProductUseCase)


@pytest.fixture
def mock_update_product(mock_test_container):
    return mock_test_container.resolve(UpdateProductUseCase)


async def test_get_product_by_id(mock_get_product_use_case):
    command = GetProductCommandFactory.build()
    product = await mock_get_product_use_case.execute(command)

    assert product.oid == command.oid


async def test_create_product(mock_create_product):
    command = CreateProductCommandFactory.build()
    product = await mock_create_product.execute(command)

    assert product == command.product


async def test_update_product(mock_update_product):
    command = UpdateProductCommandFactory.build()
    product = await mock_update_product.execute(command)

    assert product == command.product
