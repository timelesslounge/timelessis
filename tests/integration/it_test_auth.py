from http import HTTPStatus


def test_login(client, auth):
    assert client.get("/auth/login").status_code == HTTPStatus.OK
    response = auth.login()
    assert response.status_code == HTTPStatus.OK


def test_forgot_password(client):
    assert client.get("/auth/forgotpassword").status_code == HTTPStatus.OK


def test_activate(client):
    assert client.get("/auth/activate").status_code == HTTPStatus.METHOD_NOT_ALLOWED
