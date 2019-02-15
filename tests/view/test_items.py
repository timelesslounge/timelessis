""" Tests for the items.
"""

from http import HTTPStatus

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
