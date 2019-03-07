from http import HTTPStatus
import flask
import pytest

from tests import factories
from timeless.restaurants import models
from timeless.restaurants.models import TableShape
from timeless.restaurants.table_shapes.views import order_by, filter_by


def test_order_by_description(db_session):
    db_session.add(TableShape(id=1, description="B", picture="pic"))
    db_session.add(TableShape(id=2, description="A", picture="pic"))
    db_session.commit()
    shapes = TableShape.query.order_by(TableShape.description).all()
    assert shapes[0].id == 2
    assert shapes[1].id == 1


def test_filter_by_description(db_session):
    db_session.add(TableShape(id=1, description="B", picture="pic"))
    db_session.add(TableShape(id=2, description="A", picture="pic"))
    db_session.add(TableShape(id=3, description="BB", picture="pic"))
    db_session.commit()
    shapes = filter_by(TableShape.query, ["description=B"]).all()
    assert len(shapes) == 1
    assert shapes[0].id == 1


def test_list(client):
    assert client.get("/table_shapes/").status_code == HTTPStatus.OK


def test_ordered_list(client):
    assert client.get(
        flask.url_for('table_shape.list', order_by=["id:asc", "description"])
    ).status_code == HTTPStatus.OK


def test_filtered_list(client, db_session):
    db_session.add(TableShape(id=1, description="B", picture="pic"))
    db_session.add(TableShape(id=2, description="A", picture="pic"))
    db_session.add(TableShape(id=3, description="BB", picture="pic"))
    db_session.commit()
    response = client.get(flask.url_for('table_shape.list', filter_by=["description=B"]))
    assert response.status_code == HTTPStatus.OK
    # @todo #260:30min Lets encapsulate the way test checks for the returned table spaces. Currently all
    #  the specifics on how to check the amount of returned table shapes and specific table shape details is exposed
    #  directly in client code. There is a need to have a so called Page Object abstraction for the table_shapes.list
    #  route that will encapsulate parsing, length and index access in a single entity, having a single place to fix in
    #  case UI layout is changed. Please consider following draft client code as a reference:
    #  table_shapes = TableShapes(client, filter_by=["description=B"]
    #  assert len(table_shapes) == 1
    #  assert iter(table_shapes).next().id == 1

    html = response.data.decode("utf-8")
    assert html.count("<article class=\"table_shape\">") == 1
    assert html.count(
        "<a class=\"action\" href=\"/table_shapes/edit/1\">Edit</a>"
    ) == 1


def test_create(client):
    files = {'file': open(
        'tests/integration/fixtures/test_image.jpg', 'rb')}
    response = client.post(
        flask.url_for("table_shape.create"),
        data={
            "description": "It's new shape",
            "files": files
        }
    )
    assert response.location.endswith(flask.url_for('table_shape.list'))
    table_shape = TableShape.query.first()
    assert table_shape
    assert table_shape.picture


def test_edit(client):
    table_shape = factories.TableShapeFactory(
        description="Description 1",
        picture="picture-path-1"
    )
    response = client.post(
        flask.url_for("table_shape.edit", id=table_shape.id),
        data={
            "description": "Description 2",
            "picture": "picture-path-2",
        }, follow_redirects=True)

    assert "Description 2" in response.data.decode()
    # @todo #285:30m This test should send file to picture input. Implement
    #  file uploading and then uncomment the following line. Logic of saving
    #  picture is already implemented in TableShapeForm, it's time to test.

    # assert "picture-path-2" in response.data.decode()


def test_delete(client):
    table_shape = factories.TableShapeFactory()
    response = client.post(
        flask.url_for("table_shape.delete", id=table_shape.id))
    assert response.status_code == HTTPStatus.FOUND
    assert not models.TableShape.query.count()
