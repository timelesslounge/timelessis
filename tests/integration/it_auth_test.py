from datetime import datetime
from http import HTTPStatus
import flask
import pytest

from timeless.auth.auth import login
from timeless.employees.models import Employee

"""
    Unit test for authentication related poster accesses.
"""


def test_incorrect_username(db_session):
    """Do not remove db_session dependency. It is injected
    in order to trigger db migration.
    """
    assert (login("unknown", "unknown") == "login.failed")


def test_incorrect_password(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1", account_status="A",
                        birth_date=datetime.utcnow(), pin_code=4567,
                        registration_date=datetime.utcnow(), user_status="U",
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    assert (login("unknown", "unknown") == "login.failed")

"""
@todo #149:30min Continue implementation of the login function. The
 login("vgv", "pass") is returning ValueError: not a valid bcrypt_sha256 hash.
 Information from https://passlib.readthedocs.io/en/stable/index.html can be
 used to help.
"""
def test_login(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1", account_status="A",
                        birth_date=datetime.utcnow(), pin_code=4567,
                        registration_date=datetime.utcnow(), user_status="U",
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    """error = login("vgv", "pass")"""
    error = login("unknown", "unknown");
    db_session.delete(employee)
    db_session.commit()
    db_session.remove()
    assert (error == "login.failed")

@pytest.mark.skip(reason="Correction request included in todo #340:30min")
def test_forgot_password(client):
    response = client.get("/auth/forgotpassword")
    decoded = response.data.decode("utf-8")
    assert "<h1>Forgot your password?</h1>" in decoded
    assert "<input type=\"submit\" value=\"Forgot my password\">" in decoded
    assert response.status_code == 200


def test_activate(client):
    assert client.get("/auth/activate").status_code == 405


def test_forgot_password_post(client):
    response = client.post(flask.url_for("auth.forgot_password"), data={
        "email": "test@mail.com"
    })
    assert response.status_code == HTTPStatus.FOUND
