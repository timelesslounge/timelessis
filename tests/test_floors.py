import pytest


def test_list(client):
    assert client.get("/floors/").status_code == 200


@pytest.mark.parametrize("path", (
    "floors/create",
    "/floors/edit/1",
    "/floors/delete",
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "http://localhost/auth/login"


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_create(client, auth):
    auth.login()
    assert client.get("/floors/create").status_code == 200


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_edit(client, auth):
    auth.login()
    assert client.get("/floors/edit/1").status_code == 200


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_delete(client, auth):
    auth.login()
    response = client.post("/floors/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/floors/"
