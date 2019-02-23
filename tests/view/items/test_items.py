""" Tests for the items.
"""
from http import HTTPStatus
from datetime import datetime

from tests.view.items.mock_items import ItemMock, ItemsMock
from timeless.items.views import ItemListView


def test_list(client):
    """ Test list is okay """
    items = ItemListView(
        items = ItemsMock(
            [
                {
                    "id": 1,
                    "name": "Pancakes",
                    "stock_date": datetime.utcnow,
                    "comment": "Really delicious pancakes made from flour and eggs",
                    "company_id": 1,
                    "created_on": datetime.utcnow,
                    "updated_on": datetime.utcnow,
                    "employee_id": 1
                },
                {
                    "id": 2,
                    "name": "Dental Floss",
                    "stock_date": datetime.utcnow,
                    "comment": "Dental floss from Montana salesmen",
                    "company_id": 1,
                    "created_on": datetime.utcnow,
                    "updated_on": datetime.utcnow,
                    "employee_id": 1
                },
                {
                    "id": 3,
                    "name": "Power Cable",
                    "stock_date": datetime.utcnow,
                    "comment": "Power cable made of leather and heavy metal",
                    "company_id": 1,
                    "created_on": datetime.utcnow,
                    "updated_on": datetime.utcnow,
                    "employee_id": 1
                },
                {
                    "id": 4,
                    "name": "Brick Block",
                    "stock_date": datetime.utcnow,
                    "comment": "Red block made from bricks, sometimes hide coins",
                    "company_id": 1,
                    "created_on": datetime.utcnow,
                    "updated_on": datetime.utcnow,
                    "employee_id": 1
                }
            ]
        ),
        item = ItemMock
    )
    assert client.get("/items/").status_code == HTTPStatus.OK


def test_create(client):
    """ Test create is okay """
    assert client.get("/items/create").status_code == HTTPStatus.OK


def test_edit(client):
    """ Test edit is okay """
    assert client.get("/items/edit").status_code == HTTPStatus.OK


def test_delete(client):
    """ Test delete is okay """
    response = client.post("/items/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/items/"
