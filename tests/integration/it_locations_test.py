from http import HTTPStatus


def test_list(client):
    assert client.get("/locations/").status_code == HTTPStatus.OK


def test_create(client, db_session):
    assert client.get("/locations/create").status_code == HTTPStatus.OK


def test_edit(client):
    assert client.get("/locations/edit/1").status_code == HTTPStatus.OK


def test_delete(client, db_session):
    response = client.post("/locations/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/locations/"
