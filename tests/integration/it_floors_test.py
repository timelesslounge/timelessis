from http import HTTPStatus
from flask import url_for
import pytest
from timeless.restaurants.models import Floor


def test_list(client, db_session):
    """ Test getting list of Floors objects
    @todo #173:30min Once issue with cache (#273) is resolved, remove
     clear_cache fixture and make sure that test runs ok. Also remove it from
     if they use it.
    """
    db_session.add(Floor(location_id=None, description="Test floor"))
    db_session.commit()
    floors = client.get("/floors/")
    assert floors.status_code == HTTPStatus.OK
    assert b"Test floor" in floors.data


@pytest.mark.parametrize("path", (
    "/floors/create",
    "/floors/edit/1",
    "/floors/delete",
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == url_for("auth.login",
                                                   _external=True)


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_create(client, auth):
    auth.login()
    assert client.get("/floors/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_edit(client, auth):
    auth.login()
    assert client.get("/floors/edit/1").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_delete(client, auth):
    auth.login()
    response = client.post("/floors/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/floors/"
