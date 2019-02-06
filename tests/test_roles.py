from http import HTTPStatus


def test_list(client):
    assert client.get("/roles/").status_code == HTTPStatus.OK


def test_create(client):
    assert client.get("/roles/create").status_code == HTTPStatus.OK


def test_edit(client):
    assert client.get("/roles/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    response = client.post("/roles/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/roles/"
