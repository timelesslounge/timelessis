from http import HTTPStatus
import flask
import pytest

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
    # @todo #260:30min Uncomment below assertion and fix the test once #273 is fixed.
    #  Currently there is an issue with template caching which is reported by #273 1st point. Lets uncomment
    #  below assertion checking if filter logic works as expected by checking table shapes rendered within list route.

    # html = response.data.decode('utf-8')
    # assert html.count('<article class="table_shape">') == 1
    # assert html.count('<a class="action" href="/table_shapes/edit/1">Edit</a>') == 1


@pytest.mark.skip(reason="test should submit multipart request with real image as picture")
def test_create(client, db_session):
    response = client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    assert response.location.endswith(flask.url_for('table_shape.list'))
    assert TableShape.query.count() == 0


# @todo #206:30min Fix timeless.forms.ModelForm so it will use instance
#  when populating fields in form, not only during save and update. After the
#  it has been fixed enable two assertions below.
# @todo #206:15min After the form.save() issue with picture is solved enable
#  test_edit and test_delete. Both were disabled because picture validation was
#  added but the form for it wasn't updated, so create method doesn't save
#  anything right now.
@pytest.mark.skip(reason="create method doesn't have form.save()")
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


@pytest.mark.skip(reason="create method doesn't have form.save()")
def test_delete(client):
    client.post(flask.url_for("table_shape.create"), data={
        "description": "It's new shape",
        "picture": "http://...."
    })
    identifier = models.TableShape.query.first().id

    result = client.post(flask.url_for('table_shape.delete', id=identifier))
    assert result.status_code == HTTPStatus.FOUND
    assert models.TableShape.query.filter_by(id=identifier).count() == 0
