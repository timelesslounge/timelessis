"""Integration tests for Locations"""
from http import HTTPStatus
from flask import url_for

from timeless.restaurants.models import Location


def test_list(client, db_session):
    """ List all locations """
    db_session.add(_create_test_location())
    db_session.commit()
    response = client.get(url_for("location.list"))
    assert response.status_code == HTTPStatus.OK
    assert b"Test location" in response.data
    assert response.data.count(b"<article class=\"location\">",
                               response.data.find(b"<!doctype html>")) == 1


def test_create(client):
    location_data = {
        "name": "Name",
        "code": "Code",
        "country": "Country",
        "region": "Region",
        "city": "City",
        "address": "Address",
        "longitude": "0.0000000",
        "latitude": "0.0000000",
        "type": "Type",
        "status": "Active",
        "comment": "No comments",
    }
    client.post(url_for("location.create"), data=location_data)
    assert Location.query.count() == 1


def test_edit(client):
    assert client.get("/locations/edit/1").status_code == HTTPStatus.OK


def test_delete(client):
    response = client.post("/locations/delete", data={"id": 1})
    assert response.headers["Location"] == "http://localhost/locations/"


def _create_test_location():
    return Location(
        name="Test location", code="1", country="USA", region="West",
        city="LA", type="Type", address="Address", longitude="11223344",
        latitude="44332211", status="T")
