from http import HTTPStatus

import flask
import pytest

from timeless.items.models import Item
from tests import factories


""" Tests for the items.
@todo #417:30min Fix ItemListView problem of returning empty list. 
 ItemListView is returning an empty list when it should return valid values. 
 Test below is valid, it calls ItemListView with an authenticated user but it 
 isn't retrieving the items. Fix the ItemListView class and then uncomment the
 test below.
@todo #311:30min CreateView is not working as intended and is not saving Items.
 Find and fix the problem and then uncomment the def test_create(client) 
 method.
"""


@pytest.mark.skip(reason="Correct the ItemListView bug")
def test_list(client):
    """ Test list is okay """
    employee = factories.EmployeeFactory()
    factories.ItemFactory(name="1")
    factories.ItemFactory(name="2")
    factories.ItemFactory(name="3")
    flask.g.user = employee
    with client.session_transaction() as session:
        session["user_id"] = employee.id
    response = client.get("/items/")
    print(response.data)
    assert b"<article class=\"item\"><header><div><h1>1</h1></div>" in response.data
    assert b"<article class=\"item\"><header><div><h1>2</h1></div>" in response.data
    assert b"<article class=\"item\"><header><div><h1>3</h1></div>" in response.data
    assert response.status_code == HTTPStatus.OK


@pytest.mark.skip(reason="Correct CreateView problem")
def test_create(client):
    """ Test create is okay """
    company = factories.CompanyFactory()
    employee = factories.EmployeeFactory(company=company)
    item_name = "Yellow Fedora"
    item_comment = "A yellow fedora that belonged to a hero from a movie"
    item = {
        "name": item_name,
        "comment": item_comment,
        "company_id": company.id,
        "employee_id": employee.id,
    }
    create_response = client.post("/items/create", data=item)
    database_item = Item.query.filter_by(name="Yellow Fedora").first()
    assert create_response.status_code == HTTPStatus.OK
    assert database_item is not None
    assert database_item.name == item_name
    assert database_item.comment == item_comment
    assert database_item.company_id == company.id
    assert database_item.employee_id == employee.id


@pytest.mark.parametrize("path", (
    "items.create",
))
def test_login_required(client, path):
    response = client.post(flask.url_for(path))
    assert response.status_code == HTTPStatus.FOUND
    assert response.headers["Location"].endswith("auth/login")


def test_edit(client):
    """ Test edit is okay """
    assert client.get("/items/edit").status_code == HTTPStatus.OK


def test_delete(client):
    """ Test delete is okay """
    response = client.post("/items/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/items/"
