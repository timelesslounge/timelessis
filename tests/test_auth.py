""" Tests for auth/views.py methods """
import pytest

from flask import g
from http import HTTPStatus

from tests import factories
from timeless.auth import auth
from timeless.employees.models import Employee


def test_activate_unauthenticated_get(client):
    """ Tests if unauthenticated GET to activate returns 405"""
    response = client.get("/auth/activate")
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_activate_unauthenticated(client):
    """ Tests if unauthenticated POST to activate returns correct screen"""
    response = client.post("/auth/activate")
    assert b"<h1>You are not logged in</h1>" in response.data
    assert response.status_code == HTTPStatus.OK


def test_activate_authenticated(client):
    """
    Tests if authenticated POST to activate returns correct screen
    """
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory(),
        account_status=False
    )
    with client.session_transaction() as session:
        session["logged_in"] = True
        session["user_id"] = employee.id
    response = client.post("/auth/activate")
    assert b"<h1>Successfully activated your account.</h1>" in response.data
    assert Employee.query.get(employee.id).account_status
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize('email,masked_email', (
    ('v@gmail.com', '*@gmail.com'),
    ('vr@gmail.com', 'v*@gmail.com'),
    ('john.black@gmail.com', 'john.*****@gmail.com'),
))
def test_mask_email(email, masked_email):
    """ Tests if masking of email works correctly """
    assert auth.mask_email(email) == masked_email
