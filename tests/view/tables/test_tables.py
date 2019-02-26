import pytest

from http import HTTPStatus
from datetime import datetime

from tests.view.tables.mock_tables import TableMock
from timeless.restaurants.models import Table
from timeless.restaurants.tables.views import TableListView

""" Tests for the Table views."""


@pytest.mark.skip(reason="create mock authentication for tables/list")
def test_list(client):
    """ Test list is okay """
    TableListView.model = TableMock(
        tables=
        [
            {
                "id": 1,
                "name": "Table 01",
                "floor_id": 1,
                "x": 10,
                "y": 10,
                "width": 5,
                "height": 5,
                "status": "active",
                "max_capacity": 5,
                "multiple":  False,
                "playstation":  False,
                "shape_id": 1
            },
            {
                "id": 2,
                "name": "Table 02",
                "floor_id": 1,
                "x": 20,
                "y": 20,
                "width": 10,
                "height": 10,
                "status": "active",
                "max_capacity": 10,
                "multiple":  True,
                "playstation":  True,
                "shape_id": 2
            },
            {
                "id": 3,
                "name": "Table 03",
                "floor_id": 1,
                "x": 30,
                "y": 30,
                "width": 15,
                "height": 15,
                "status": "active",
                "max_capacity": 2,
                "multiple":  True,
                "playstation":  True,
                "shape_id": 3
            }
        ]
    )
    response = client.get("/tables/")
    assert response.status_code == HTTPStatus.OK
    assert b"<div><h1>Table 01</h1></div>" in response.data
    assert b"<div><h1>Table 02</h1></div>" in response.data
    assert b"<div><h1>Table 03</h1></div>" in response.data
    TableListView.model = Table


@pytest.mark.skip(reason="/tables/create not implemented")
def test_create(client):
    """ Test create is okay """
    assert client.get("/tables/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/tables/edit not implemented")
def test_edit(client):
    """ Test edit is okay """
    assert client.get("/tables/edit").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/tables/delete not implemented")
def test_delete(client):
    """ Test delete is okay """
    response = client.post("/tables/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost//tables"