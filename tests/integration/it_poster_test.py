from unittest import mock

from timeless.poster.api import Authenticated, PosterAuthData

"""Integration tests for Poster"""


@mock.patch("timeless.poster.api.requests")
def test_auth(requests_mock):
    auth_data = PosterAuthData(
        application_id="test_id",
        application_secret="test_secret",
        redirect_uri="test_uri",
        code="test_code",
    )
    auth_token = "861052:02391570ff9af128e93c5a771055ba88"
    json_object = mock.Mock()
    json_object.return_value = {"access_token": auth_token}

    requests_mock.post.return_value = type(
        'Mock date',
        (),
        {
            'ok': True,
            'json': json_object,
        }
    )

    auth_token = Authenticated(auth_data).auth()
    assert auth_token == auth_token
