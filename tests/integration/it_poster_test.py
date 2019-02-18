from unittest import mock

from timeless.poster.api import Authenticated, PosterAuthData

"""Integration tests for Poster"""

"""
@todo #113:30min Implement auth process for Poster API.
 client_id is required for authentication process, this id is the public key
 provided by the poster service to identify the applications
"""

@mock.patch("timeless.poster.api.requests")
def test_auth(requests_mock):
    auth_data = PosterAuthData(
        application_id="test_id",
        application_secret="test_secret",
        redirect_uri="test_uri",
        code="test_code",
    )

    class Response:
        auth_token = "861052:02391570ff9af128e93c5a771055ba88"

        def ok(self):
            return True

        def json(self):
            return {"access_token": self.auth_token}

    requests_mock.post.return_value = Response()

    auth_token = Authenticated(auth_data).auth()
    assert auth_token == Response.auth_token
