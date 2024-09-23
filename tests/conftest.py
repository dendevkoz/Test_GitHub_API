import pytest

from api_client.api_client import ApiClient
from routes.routes import Routes


@pytest.fixture
def api_client():
    return ApiClient()


@pytest.fixture
def routes():
    return Routes()


