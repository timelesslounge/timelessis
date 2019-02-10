"""
@todo #169:30min Write test for creating and editing Table model. To test
 it correctly it's needed to create relations like `TableShape` and so on
 in tests. There is`factory-boy` library in requirements added. It helps
 to create instance with its relations automatically, look at
 `tests/factories.py` and see
 https://factoryboy.readthedocs.io/en/latest/orms.html#sqlalchemy. Implement
 these factories for related models and then write tests.
"""
import pytest
from http import HTTPStatus


def test_list(client):
    assert client.get("/tables/").status_code == HTTPStatus.OK


@pytest.mark.skip("fix me")
def test_create(client):
    pass


@pytest.mark.skip("fix me")
def test_edit(client):
    pass


@pytest.mark.skip("fix me")
def test_delete(client):
    pass
