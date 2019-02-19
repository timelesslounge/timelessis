import pytest

from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method


# @todo #181:30min This test stopped working because it was not working
#  according to requirements.
#  Write new tests that validate 'is_allowed' according to specifications in #22
@pytest.mark.skip("fix me")
def test_owner_can_access_location():
    assert (
        is_allowed(method=Method.DELETE, resource="location") == True
    )
