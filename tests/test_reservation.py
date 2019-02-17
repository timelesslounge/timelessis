from datetime import datetime
from http import HTTPStatus

from timeless.restaurants.models import ReservationStatus, Reservation

"""Tests for Reservation 

"""

def test_new_reservation():
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    customer_id = 1
    num_of_persons = 4
    comment = "My comment"
    status = ReservationStatus.confirmed
    new_reservation = Reservation(
        start_time=start_time,
        end_time=end_time,
        customer_id=customer_id,
        num_of_persons=num_of_persons,
        comment=comment,
        status=status
    )
    assert (
        new_reservation.start_time == start_time and
        new_reservation.end_time == end_time and
        new_reservation.customer_id == customer_id and
        new_reservation.num_of_persons == num_of_persons and
        new_reservation.comment == comment and
        new_reservation.status == status
    )

def test_reservation_duration():
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    customer_id = 5
    num_of_persons = 4
    comment = "This is a reservation for duration test"
    status = ReservationStatus.confirmed
    new_reservation = Reservation(
        start_time=start_time,
        end_time=end_time,
        customer_id=customer_id,
        num_of_persons=num_of_persons,
        comment=comment,
        status=status
    )
    assert new_reservation.duration() == end_time - start_time

def test_retrieve_status(client):
    response = client.post("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.status_code == HTTPStatus.OK

def test_retrieve_returns_json(client):
    response = client.post("/api/reservations/", data={"location" : 1, "date" : datetime(1, 1, 1)})
    assert response.is_json