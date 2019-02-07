def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.status_code == 200


def test_forgot_password(client):
    assert client.get("/auth/forgotpassword").status_code == 200


def test_activate(client):
    assert client.get("/auth/activate").status_code == 405
