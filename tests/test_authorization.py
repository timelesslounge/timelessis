from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method


def test_owner_can_access_location():
    assert (
        is_allowed(method=Method.DELETE, resource="location") == True
    )