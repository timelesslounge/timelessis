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

def test_reservation_list(client, db_session):
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory()
    )

    with client.session_transaction() as session:
        session["user_id"] = employee.id

    #Cheated reservations
    factories.ReservationFactory()
    factories.ReservationFactory()
    factories.ReservationFactory()
    factories.ReservationFactory()

    response = client.get("/reservations/teste/")

    assert b"<a class=\"action\" href=\"/reservations/edit/1\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/2\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/3\">Edit</a>" in response.data
    assert b"<a class=\"action\" href=\"/reservations/edit/4\">Edit</a>" in response.data
    assert response.status_code == HTTPStatus.OK

@pytest.mark.skip
def test_edit():
    start_time = datetime.datetime
    end_time = datetime.datetime
    customer = Customer(
        id=1,
        first_name="First",
        last_name="Last",
        phone_number="555"
    )
    num_of_persons = 4
    comment = "My comment"
    status = 2
    new_reservation = Reservation(
        id=1,
        start_time=start_time,
        end_time=end_time,
        customer_id=customer.id,
        num_of_persons=num_of_persons,
        comment=comment,
        status=status
    )
    view = views.edit(id=new_reservation.id)
    assert "<h1>Reservation management - Edit</h1>" in view
