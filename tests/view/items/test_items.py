from http import HTTPStatus

from tests import factories


""" Tests for the items."""


def test_list(client):
    """ Test list is okay """
    factories.ItemFactory()
    factories.ItemFactory()
    factories.ItemFactory()
    factories.ItemFactory()
    response = client.get("/items/")
    assert "<article class=\"item\"><header><div><h1>1</h1></div>" in response
    assert "<article class=\"item\"><header><div><h1>2</h1></div>" in response
    assert "<article class=\"item\"><header><div><h1>3</h1></div>" in response
    assert "<article class=\"item\"><header><div><h1>4</h1></div>" in response
    assert response.status_code == HTTPStatus.OK


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
