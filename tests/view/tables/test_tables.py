import pytest

from http import HTTPStatus

from timeless.restaurants.models import Table
from timeless.restaurants.tables.views import TableListView
from tests import factories

""" Tests for the Table views."""


@pytest.mark.skip(reason="Inject authentication for tables/list")
def test_list(client):
    """ Test list is okay """
    floor = factories.FloorFactory()
    factories.TableFactory(floor_id=floor.id)
    factories.TableFactory(floor_id=floor.id)
    factories.TableFactory(floor_id=floor.id)
    factories.TableFactory(floor_id=floor.id)
    response = client.get("/tables/")
    assert response.status_code == HTTPStatus.OK
    assert b"<div><h1>Table 01</h1></div>" in response.data
    assert b"<div><h1>Table 02</h1></div>" in response.data
    assert b"<div><h1>Table 03</h1></div>" in response.data
    assert b"<div><h1>Table " in response.data.count == 3


def test_required_authentication(client):
    """ Test list is okay """
    response = client.get("/tables/")
    assert response.status_code == HTTPStatus.OK
    assert b"<li><a href=\"#\">Register</a>" in response.data
    assert b"<li><a href=\"/auth/login\">Log In</a>" in response.data


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
