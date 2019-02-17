from datetime import datetime
from http import HTTPStatus


def test_retrieve_status(client):
    response = client.post("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.status_code == HTTPStatus.OK


def test_retrieve_returns_json(client):
    response = client.post("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.is_json
