from datetime import datetime
from http import HTTPStatus


def test_retrieve_status(client):
    response = client.get("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.status_code == HTTPStatus.OK
    assert response.is_json
