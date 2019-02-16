from http import HTTPStatus
import flask

from timeless.restaurants import models
from timeless.restaurants.models import TableShape
from timeless.restaurants.table_shapes.views import order_by


def test_order_by_description(db_session):
    db_session.add(TableShape(id=1, description="B", picture="pic"))
    db_session.add(TableShape(id=2, description="A", picture="pic"))
    db_session.commit()
    shapes = order_by(TableShape.query, ["description:asc"]).all()
    assert shapes[0].id == 2
    assert shapes[1].id == 1


def test_list(client):
    assert client.get("/table_shapes/").status_code == HTTPStatus.OK


def test_ordered_list(client):
    assert client.get(
        flask.url_for('table_shape.list', order_by=["id:asc", "description"])
    ).status_code == HTTPStatus.OK


def test_create(client, db_session):
    response = client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    assert response.location.endswith(flask.url_for('table_shape.list'))
    assert models.TableShape.query.count() == 1


# @todo #206:30min Fix timeless.forms.ModelForm so it will use instance
#  when populating fields in form, not only during save and update. After the
#  it has been fixed enable two assertions below.
def test_edit(client):
    create_data = {
        "description": "It's new shape",
        "picture": "http://...."
    }
    client.post(flask.url_for("table_shape.create"), data=create_data)
    identifier = models.TableShape.query.first().id
    first_result = client.get(flask.url_for("table_shape.edit", id=identifier))
    assert first_result.status_code == HTTPStatus.OK
    # assert create_data["description"] in str(first_result.data, "utf-8")
    # assert create_data["picture"] in str(first_result.data, "utf-8")
    update_data = {
        "description": "Updated description",
        "picture": "http://updated...."
    }
    second_result = client.post(
        flask.url_for("table_shape.edit", id=identifier), data=update_data
    )
    assert second_result.status_code == HTTPStatus.FOUND
    db_result = models.TableShape.query.first()
    assert db_result.description == update_data["description"]
    assert db_result.picture == update_data["picture"]


def test_delete(client):
    client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    identifier = models.TableShape.query.first().id

    result = client.post(flask.url_for('table_shape.delete', id=identifier))
    assert result.status_code == HTTPStatus.FOUND
    assert models.TableShape.query.filter_by(id=identifier).count() == 0