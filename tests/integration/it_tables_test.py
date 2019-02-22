"""
@todo #169:30min Write test for creating and editing Table model. To test
 it correctly it's needed to create relations like `TableShape` and so on
 in tests. There is`factory-boy` library in requirements added. It helps
 to create instance with its relations automatically, look at
 `tests/factories.py` and see
 https://factoryboy.readthedocs.io/en/latest/orms.html#sqlalchemy. Implement
 these factories for related models and then write tests.
"""
from http import HTTPStatus

import flask
import pytest

from timeless.restaurants import models


def test_list(client):
    assert client.get("/tables/").status_code == HTTPStatus.OK


def test_create(client):
    client.post(flask.url_for("table.create"), data={
        "name": "Test",
        "x": 1,
        "y": 2,
        "width": 3,
        "height": 4,
        "status": 5,
        "max_capacity": 6,
    })
    assert models.Table.query.count() == 1


@pytest.mark.skip("fix me")
def test_edit(client):
    pass


@pytest.mark.skip("fix me")
def test_delete(client):
    pass
