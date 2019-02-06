import unittest

from tests.poster_mock import free_port, start_server
from timeless.poster.api import Poster, Authenticated

"""
    Unit test for authentication related poster accesses.
"""

def test_login(client, auth):
    assert client.get("/auth/login").status_code == 200
    response = auth.login()
    assert response.status_code == 200


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
    """
    def test_token_retrieval(self):
        assert (
            Authenticated(Poster()).access_token() != ""
        )



