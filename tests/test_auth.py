import unittest
from datetime import datetime

from tests.poster_mock import free_port, start_server
from timeless.auth.auth import login
from timeless.employees.models import Employee
from timeless.poster.api import Authenticated

"""
    Unit test for authentication related poster accesses.
"""

def test_incorrect_username(db_session):
    """Do not remove db_session dependency. It is injected
    in order to trigger db migration.
    """
    assert (login("unknown", "unknown") == "Incorrect username.")


def test_incorrect_password(db_session):
    employee = Employee(first_name="Alice", last_name="Cooper",
                        username="vgv", phone_number="1",
                        birth_date=datetime.utcnow(),
                        registration_date=datetime.utcnow(),
                        email="test@test.com", password="pass")
    db_session.add(employee)
    db_session.commit()
    error = login("vgv", "unknown")
    assert (error == "Incorrect password.")


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


class TestAuth(unittest.TestCase):

    port = free_port()
    locations = None

    @classmethod
    def setup_class(cls):
        cls.port = free_port()
        start_server(cls.port, locations=cls.locations)

    """
        Tests token retrieval from poster: poster should return a valid token 
        @todo #101:30min Implement other test cases for poster token 
         retrieval. The remaining test cases must be discovered, the error 
         codes in https://dev.joinposter.com/en/docs/api#authorization-in-api 
         are not specific enough.   
    """
    def test_can_retrieve_token(self):
        self.setup_class()
        assert (
            Authenticated(
                url=f"http://localhost:{self.port}"
            ).access_token() == "861052:02391570ff9af128e93c5a771055ba88"
        )



