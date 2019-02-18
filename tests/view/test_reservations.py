import datetime
import pytest

from timeless.customers.models import Customer
from timeless.restaurants.models import Reservation
from timeless.reservations import views


"""
    Tests for Reservations view.
    @todo #235:30min Continue implementation of views. Index and a
     view page should be created to list all reservations. In the
     index page there should be also a function to delete the reservation
     (after confirmation). In the index page it should be possible
     to sort and filter for every column.
    @todo #172:30min Continue implementation of reservations tess for views: 
     add tests for create, list and delete and add other logic to edit() test so
     it tests if the screen is being constructed correctly , then uncomment 
     the test

"""


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
