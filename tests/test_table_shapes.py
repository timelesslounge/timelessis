import flask
from http import HTTPStatus

from timeless.db import DB
from timeless.restaurants import models


def test_list(client):
    assert client.get("/table_shapes/").status_code == HTTPStatus.OK


def test_create(client, app):
    response = client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    assert response.location.endswith(flask.url_for('table_shape.list'))
    assert models.TableShape.query.count() == 1


def test_edit(client):
    assert client.get("/table_shapes/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    table_shape = models.TableShape(
        description="Shape for deleting", picture="test")
    DB.session.add(table_shape)
    DB.session.commit()
    DB.session.refresh(table_shape)

    client.post(flask.url_for('table_shape.delete', id=table_shape.id))
    assert not models.TableShape.query.count()
