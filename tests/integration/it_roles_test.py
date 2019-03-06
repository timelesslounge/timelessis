from http import HTTPStatus

from flask import url_for

from tests import factories
from timeless.roles.models import Role, RoleType


def test_list(client):
    assert client.get("/roles/").status_code == HTTPStatus.OK


def test_create(client, db_session):
    response = client.post(url_for("role.create"), data={
        "name": "John"
    })
    assert response.location.endswith(url_for('role.list_roles'))
    assert Role.query.filter_by(name="John").count() == 1


def test_edit(client):
    role = factories.RoleFactory(role_type=RoleType.Manager)
    url = url_for("role.edit", id=role.id)

    client.post(url, data={"role_type": RoleType.Director.value})
    assert Role.query.filter_by(
        id=role.id, role_type=RoleType.Director.value).count() == 1


def test_delete_not_found(client):
    assert Role.query.filter_by(id=1).count() == 0
    assert client.post(
        url_for('role.delete', id=1)).status_code == HTTPStatus.NOT_FOUND


def test_delete(client):
    name = 'role_for_deletion'
    assert Role.query.filter_by(name=name).count() == 0
    client.post(url_for("role.create"), data={
        "name": name
    })
    assert Role.query.filter_by(name=name).count() == 1
    created = Role.query.filter_by(name=name).first()

    result = client.post(url_for('role.delete', id=created.id))
    assert result.status_code == HTTPStatus.FOUND
    assert Role.query.filter_by(id=created.id).count() == 0
    assert result.headers["Location"] == "http://localhost/roles/"

