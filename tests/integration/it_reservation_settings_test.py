"""
@todo #186:30min Write tests for creating and editing, deleting Settings
 Reservation model. Now set up 4 tests with pytest.mark.skip option, remove
 it when tests will be done
"""
import pytest
from http import HTTPStatus

from flask import url_for


def test_list(client):
    assert client.get(
        url_for("reservation_settings_list")
    ).status_code == HTTPStatus.OK


@pytest.mark.skip
def test_create(client):
    assert client.get(
        url_for("reservation_settings_create")
    ).status_code == HTTPStatus.OK


@pytest.mark.skip
def test_edit(client):
    assert client.get(
        url_for("reservation_settings_detail", id=1)
    ).status_code == HTTPStatus.OK


@pytest.mark.skip
def test_delete(client):
    assert client.get(
        url_for("reservation_settings_delete", id=1)
    ).status_code == HTTPStatus.OK
