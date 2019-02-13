from unittest import mock

from timeless.poster.api import Authenticated, PosterAuthData

"""Integration tests for Poster"""


def test_auth():
    auth_data = PosterAuthData(
        application_id="test_id",
        application_secret="test_secret",
        redirect_uri="test_uri",
        code="test_code",
    )
    auth_token = "test_auth_token"

    def auth(*args, **kwargs):
        mocked = mock.Mock()
        mocked.return_value = auth_token
        return mocked

    with mock.patch.object(Authenticated, 'auth', auth):
        auth_token = Authenticated(auth_data).auth()
        assert auth_token == auth_token
