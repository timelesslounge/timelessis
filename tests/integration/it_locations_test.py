"""Integration tests for Locations"""
from http import HTTPStatus
from flask import url_for
import pytest

from timeless.restaurants.models import Location


def test_list(client, db_session):
    """ List all locations """
    db_session.add(__create_location__())
    db_session.commit()
    response = client.get(url_for("location.list"))
    assert response.status_code == HTTPStatus.OK
    assert b"Test location" in response.data


@pytest.mark.skip(reason="location.create() is not yet implemented")
def test_create(client, db_session):
    assert client.get("/locations/create").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="location.edit(id) is not yet implemented")
def test_edit(client):
    assert client.get("/locations/edit/1").status_code == HTTPStatus.OK


@pytest.mark.skip(reason="location.delete() is not yet implemented")
def test_delete(client, db_session):
    response = client.post("/locations/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/locations/"


def __create_location__():
    return Location(
        name="Test location", code="1", country="USA", region="West",
        city="LA", type="Type", address="Address", longitude="11223344",
        latitude="44332211", status="T")
