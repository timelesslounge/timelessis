import datetime
import pytest

from timeless.customers.models import Customer
from timeless.restaurants.models import Reservation
from timeless.reservations import views

from tests import factories
from http import HTTPStatus

"""
    Tests for Reservations view.
    @todo #235:30min Continue implementation of views. Index and a
     view page should be created to list all reservations. In the
     index page there should be also a function to delete the reservation
     (after confirmation). In the index page it should be possible
     to sort and filter for every column.

"""

def test_reservation_list(client):
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory()
    )

    with client.session_transaction() as session:
        session["user_id"] = employee.id

    #Cheated reservations
    factories.ReservationFactory.create_batch(size=4)

    response = client.get("/reservations/")

    assert b"<a class=\"action\" href=\"/reservations/edit/3\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/4\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/5\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/6\">Edit</a>" in response.data
    assert response.status_code == HTTPStatus.OK

