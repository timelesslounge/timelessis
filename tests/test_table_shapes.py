from http import HTTPStatus


def test_list(client):
    assert client.get("/table_shapes/").status_code == HTTPStatus.OK


def test_create(client):
    assert client.get("/table_shapes/create").status_code == HTTPStatus.OK


def test_edit(client):
    assert client.get("/table_shapes/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    response = client.post("/table_shapes/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/table_shapes/"
