from http import HTTPStatus

from flask import url_for

import pytest
from tests import factories
from timeless.restaurants.models import Reservation


@pytest.mark.skip("reservations.list does not implemented yet")
def test_list(client):
    reservation = factories.ReservationFactory()
    response = client.get(url_for("reservations.list"))
    assert response.status_code == HTTPStatus.OK
    assert reservation.comment in response.data


def test_create(client):
    reservation = factories.ReservationFactory.build()
    # convert reservation instance to dict
    reservation_dict = {
        column.name: str(getattr(reservation, column.name))
        for column in reservation.__table__.columns
    }
    url = url_for("reservations.create_reservation")
    response = client.post(url, data=reservation_dict)
    assert response.status_code == HTTPStatus.CREATED
    assert Reservation.query.count() == 1


@pytest.mark.skip("reservations.edit does not implemented yet")
def test_edit(client):
    reservation_old = factories.ReservationFactory()
    reservation_new = factories.ReservationFactory()
    url = url_for("reservations.edit", id=reservation_old.id)
    response = client.post(url, data=reservation_new)
    assert response.status_code == HTTPStatus.OK
    assert reservation_new.comment in response.data


def test_delete(client):
    reservation = factories.ReservationFactory()
    url = url_for("reservations.delete", id=reservation.id)
    response = client.post(url)
    assert response.location.endswith(url_for("reservations.list"))
    assert Reservation.query.filter_by(id=reservation.id).count() == 0
