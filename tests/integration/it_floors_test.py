from http import HTTPStatus

import pytest
from flask import g, url_for

from tests import factories
from timeless.restaurants.models import Floor


def test_list(client, db_session):
    db_session.add(Floor(location_id=None, description="Test floor"))
    db_session.commit()
    floors = client.get("/floors/")
    assert floors.status_code == HTTPStatus.OK
    assert b"Test floor" in floors.data


@pytest.mark.skip(reason="Order is not yet implemented")
def test_ordered_list(client):
    factories.FloorFactory(description="B")
    factories.FloorFactory(description="A")
    response = client.get(url_for("floor.list", order_by=["description:asc"]))
    html = response.data.decode('utf-8')
    assert html.count(
        "</header>\n\n\n<article class=\"floor\">\n<header>\n<div>\n<h1>A</h1>"
    ) == 1
    assert response.status_code != HTTPStatus.OK


@pytest.mark.skip(reason="Order is not yet implemented")
def test_filtered_list(client):
    response = client.get(url_for('floor.list', filter_by=["description=B"]))
    html = response.data.decode('utf-8')
    assert html.count('<h1>A</h1>') == 0
    assert html.count('<h1>B</h1>') == 1
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize("path", (
    "/floors/edit/1",
    "/floors/delete/1",
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == url_for("auth.login",
                                                   _external=True)


def test_create(client, auth):
    location = factories.LocationFactory()
    auth.login()
    floor_data = {
        "description": "Test floor",
        "location_id": location.id
    }
    response = client.post(url_for('floor.create'), data=floor_data)
    assert response.headers["Location"] == "http://localhost/floors/"
    assert response.status_code == HTTPStatus.FOUND
    assert Floor.query.count() == 1
    floor = Floor.query.first()
    assert floor.description == floor_data["description"]
    assert floor.location_id == floor_data["location_id"]


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_edit(client, auth):
    auth.login()
    assert client.get("/floors/edit/1").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="auth.login() is not yet implemented")
def test_delete(client, auth):
    auth.login()
    floor = factories.FloorFactory()
    response = client.post(url_for("floor.delete", id=floor.id))
    assert response.headers["Location"] == "http://localhost/floors/"
    assert response.status_code == HTTPStatus.FOUND
    assert Floor.query.count() == 0
