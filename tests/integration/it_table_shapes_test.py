from http import HTTPStatus
import flask

from timeless.restaurants import models
from timeless.restaurants.models import TableShape
from timeless.restaurants.table_shapes.views import order_by


def test_order_by_description(db_session):
    db_session.add(TableShape(id=1, description="B", picture="pic"))
    db_session.add(TableShape(id=2, description="A", picture="pic"))
    db_session.commit()
    shapes = TableShape.query.order_by(TableShape.description).all()
    assert shapes[0].id == 2
    assert shapes[1].id == 1


def test_list(client):
    assert client.get("/table_shapes/").status_code == HTTPStatus.OK


def test_ordered_list(client):
    assert client.get(
        flask.url_for('table_shape.list')
    ).status_code == HTTPStatus.OK


def test_create(client, db_session):
    response = client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    assert response.location.endswith(flask.url_for('table_shape.list'))
    assert TableShape.query.count() == 0


def test_edit(client):
    assert client.get("/table_shapes/edit/1").status_code == HTTPStatus.OK


def test_delete(client, db_session):
    table_shape = models.TableShape(
        description="Shape for deleting", picture="test")
    db_session.add(table_shape)
    db_session.commit()
    db_session.refresh(table_shape)

    client.post(flask.url_for('table_shape.delete', id=table_shape.id))
    assert not models.TableShape.query.count()
