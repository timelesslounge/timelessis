from http import HTTPStatus
from flask import url_for
import pytest


def test_list(client):
    assert client.get("/floors/").status_code == HTTPStatus.OK


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
