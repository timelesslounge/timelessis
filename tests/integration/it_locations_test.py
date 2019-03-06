"""Integration tests for Locations"""
from http import HTTPStatus
from flask import url_for

from tests import factories
from timeless.restaurants.models import Location


def test_list(client):
    """ List all locations """
    location = factories.LocationFactory()
    response = client.get(url_for("location.list"))
    assert response.status_code == HTTPStatus.OK
    html = response.data.decode("utf-8")
    assert html.count(location.name) == 1
    assert html.count(location.comment) == 1


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
    response = client.post(
        url_for("location.create"), data=location_data, follow_redirects=True)
    assert Location.query.count() == 1
    assert location_data["name"].encode() in response.data


def test_edit(client):
    location_old = factories.LocationFactory()
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
    url = url_for("location.edit", id=location_old.id)
    response = client.post(url, data=location_data)
    assert response.status_code == HTTPStatus.FOUND
    assert response.location.endswith(url_for('location.list'))
    assert Location.query.count() == 1
    location = Location.query.get(location_old.id)
    for attr in location_data.keys():
        assert getattr(location, attr) == location_data[attr]


def test_delete(client):
    location = factories.LocationFactory()
    url = url_for("location.delete", id=location.id)
    response = client.post(url)
    assert response.status_code == HTTPStatus.FOUND
    assert response.location.endswith(url_for('location.list'))
