from http import HTTPStatus


def test_list(client):
    assert client.get("/tables/").status_code == HTTPStatus.OK


def test_create(client):
    assert client.get("/tables/create").status_code == HTTPStatus.OK


def test_edit(client):
    assert client.get("/tables/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    response = client.post("/tables/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/tables/"
