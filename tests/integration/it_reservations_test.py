from datetime import datetime

from flask import url_for

import pytest
from timeless.restaurants.models import Reservation, ReservationStatus

def test_create_reservation(client, db_session):
    reservation = Reservation.query.get(100)
    if reservation:
        db_session.delete(reservation)
        db_session.commit()

    comment = "Comment for verification"
    response = client.post(url_for("reservations.create"), data={
        "id": 100,
        "start_time": datetime(2019, 2, 20, 21, 30),
        "end_time": datetime(2019, 2, 20, 22, 30),
        "customer_id": 1,
        "num_of_persons": 2,
        "comment": comment,
        "status": ReservationStatus.confirmed.name
    })
    assert response.location.endswith(url_for("reservations.list_reservations"))
    assert Reservation.query.count() == 1
    assert Reservation.query.get(100).comment == comment

def test_delete_reservation(client, db_session):
    id = 1
    reservation = Reservation(
        id=id,
        start_time=datetime.utcnow(),
        end_time=datetime.utcnow(),
        num_of_persons=2,
        status=ReservationStatus.confirmed,
        comment="test comment"
    )
    db_session.add(reservation)
    db_session.commit()
    response = client.post(url_for('reservations.delete', id=id))
    assert response.location.endswith(url_for("reservations.list_reservations"))
    assert Reservation.query.filter_by(id=id).count() == 0
