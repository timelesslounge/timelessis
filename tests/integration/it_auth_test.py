from datetime import datetime

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
                        username="vgv", phone_number="1",
                        birth_date=datetime.utcnow(),
                        registration_date=datetime.utcnow(),
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    error = login("vgv", "unknown")
    assert (error == "login.failed")


def test_login(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1",
                        birth_date=datetime.utcnow(),
                        registration_date=datetime.utcnow(),
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    error = login("vgv", "pass")
    db_session.delete(employee)
    db_session.commit()
    db_session.remove()
    assert (error is None)


def test_forgot_password(client):
    assert client.get("/auth/forgotpassword").status_code == 200


def test_activate(client):
    assert client.get("/auth/activate").status_code == 405
