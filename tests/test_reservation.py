from datetime import datetime
from http import HTTPStatus

import  pytest

@pytest.mark.skip(reason="authentication not implemented for reservations")
def test_retrieve_status(client):
    response = client.get("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.status_code == HTTPStatus.OK

