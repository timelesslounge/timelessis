from datetime import datetime
from http import HTTPStatus

from timeless.restaurants.models import Reservation
from tests import factories

import pytest

def test_retrieve_status(client, db_session):
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory()
    )

    with client.session_transaction() as session:
        session["user_id"] = employee.id

    response = client.get("/api/reservations/")
    print (response.data)
    assert response.status_code == HTTPStatus.OK
