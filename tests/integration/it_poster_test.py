import pytest

from timeless.poster.api import Poster, Authenticated

"""Integration tests for Poster"""

"""
@todo #113:30min Implement auth process for Poster API.
 client_id is required for authentication process, this id is the public key
 provided by the poster service to identify the applications
"""

@pytest.mark.skip(
    reason="Authentication mechanism (Authenticated#auth()) is not yet implemented!"
)
def test_auth():
    assert Authenticated(
        clientid="$0m3C1i3ntId"
    ).access_token(), "Poster did not authenticate the user!"

