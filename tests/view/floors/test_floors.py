import pytest

from http import HTTPStatus

from tests import factories
from timeless.restaurants.models import Floor


""" Tests for floors. """


@pytest.mark.skip(reason="authentication not implemented for floors")
def test_list(client):
    """ Test list is okay """

    response = client.get("/floors/")
    factories.FloorFactory()
    factories.FloorFactory()
    factories.FloorFactory()
    factories.FloorFactory()
    assert response.status_code == HTTPStatus.OK
    assert b"<p class=\"description\">1st Floor</p>" in response.data
    assert b"<p class=\"description\">2nd Floor</p>" in response.data
    assert b"<p class=\"description\">3rd Floor</p>" in response.data
    assert b"<p class=\"description\">4th Floor</p>" in response.data


def test_not_authenticated(client):
    """ Test if not authenticated user is redirected to login page """

    response = client.get("/floors/")
    print(response.data)
    assert response.status_code == HTTPStatus.OK
    assert b"<li><a href=\"/auth/login\">Log In</a>" in response.data
    assert b"<a href=\"#\">Register</a>" in response.data


@pytest.mark.skip(reason="/floors/create not implemented")
def test_create(client):
    """ Test create is okay """
    assert client.get("/floors/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/floors/edit not implemented")
def test_edit(client):
    """ Test edit is okay """
    assert client.get("/floors/edit").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="/floors/delete not implemented")
def test_delete(client):
    """ Test delete is okay """
    response = client.post("/floors/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/restaurant/floors"
