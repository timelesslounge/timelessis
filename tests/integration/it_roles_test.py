from http import HTTPStatus

from flask import url_for

from timeless.roles.models import Role


def test_list(client):
    assert client.get("/roles/").status_code == HTTPStatus.OK


def test_create(client):
    response = client.post(url_for("role.create"), data={
        "name": "owner"
    })
    assert response.location.endswith(url_for("role.list_roles"))
    assert Role.query.count() == 1
    assert Role.query.get(1).name == "owner"


def test_edit(client):
    assert client.get("/roles/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    response = client.post("/roles/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/roles/"

