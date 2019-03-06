""" Tests for auth/views.py methods """
import pytest

from flask import g
from http import HTTPStatus

from tests import factories


def test_activate_unauthenticated_get(client):
    """ Tests if unauthenticated GET to activate returns 405"""
    response = client.get("/auth/activate")
    assert response.status_code ==  HTTPStatus.METHOD_NOT_ALLOWED


def test_activate_unauthenticated(client):
    """ Tests if unauthenticated POST to activate returns correct screen"""
    response = client.post("/auth/activate")
    assert b"<h1>You are not logged in</h1>" in response.data
    assert response.status_code ==  HTTPStatus.OK


@pytest.mark.skip(reason="Test must set user in session")
def test_activate_authenticated(client):
    """
    Tests if authenticated POST to activate returns correct screen
    @todo #385:30min Inject user into session in the test below. Test is broken
     because we do not set user in session and then auth/views.py does not
     redirect to correct page. Fix this behavior and uncomment this test.
    """
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory(),
        account_status=False
    )
    with client.session_transaction() as session:
        session["user_id"] = employee.id
    g.user = employee
    response = client.post("/auth/activate")
    assert b"<h1>Successfully activated your account.</h1>" in response.data
    assert employee.account_status
    assert response.status_code ==  HTTPStatus.OK
