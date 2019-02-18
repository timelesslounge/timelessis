import pytest
from tests.poster_mock import free_port, start_server
from timeless.poster.api import Poster


@pytest.fixture(scope='module')
def poster():
    port = free_port()
    start_server(
        port,
        locations={"data": "test_data"},
        tables={"data": "test_data"},
        customers={"data": "test_data"}
    )
    return Poster(url=f"http://localhost:{port}")


def test_locations(poster):
    assert poster.locations()["data"] == "test_data"


def test_tables(poster):
    assert poster.tables()["data"] == "test_data"


def test_customers(poster):
    assert poster.customers()["data"] == "test_data"
