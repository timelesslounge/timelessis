from http import HTTPStatus
from flask import url_for
import pytest
from timeless.restaurants.models import Floor


@pytest.mark.skip(reason="Must use TableListView for this test")
def test_list(client, db_session):
    db_session.add(Floor(location_id=None, description="Test floor"))
    db_session.commit()
    floors = client.get("/floors/")
    assert floors.status_code == HTTPStatus.OK
    assert b"Test floor" in floors.data


@pytest.mark.parametrize("path", (
    "/floors/edit/1",
    "/floors/delete",
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == url_for("auth.login",
                                                   _external=True)


def test_create(client):
    """
    @todo #310:30m This test works without any problems so it means
     that not authenticated used can create a floor. Check permissions
     and then fix them and update this test.
    """
    floor_data = {
        "description": "Test floor"
    }
    client.post(url_for('floor.create'), data=floor_data)
    assert Floor.query.count() == 1


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_edit(client, auth):
    auth.login()
    assert client.get("/floors/edit/1").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_delete(client, auth):
    auth.login()
    response = client.post("/floors/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/floors/"
