""" Tests for the items.
"""

# pylint: disable=unused-import
from datetime import datetime
from http import HTTPStatus
from timeless.items.models import Item, ItemHistory
from timeless.restaurants.models import Location
from timeless.roles.models import Role



def test_list(client):
    """ Test list is okay """
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

def test_new_item():
    """ Test creation on new Item """
    id = 1
    name = "First Item"
    stock_date = datetime.utcnow
    comment = "Commentary of the first item"
    company_id = 123
    new_item = Item(
        id=id,
        name=name,
        stock_date=stock_date,
        comment=comment,
        company_id=company_id
    )
    assert new_item.id == id
    assert new_item.name == name
    assert new_item.stock_date == stock_date
    assert new_item.comment == comment
    assert new_item.company_id == company_id

def test_new_item_history():
    """ Test creation of new ItemHistory """
    emp_id = 2
    item_id = 1
    item_history = ItemHistory(employee_id=emp_id, item_id=item_id)
    assert item_history.employee_id == emp_id
    assert item_history.item_id == item_id
