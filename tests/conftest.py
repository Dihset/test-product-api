import punq
import pytest

from src.core.container import get_container
from src.domain.services import IProductService
from tests.mocks.services import DummyProductService


@pytest.fixture()
def mock_test_container() -> punq.Container:
    container = get_container()

    container.register(IProductService, DummyProductService)

    return container
