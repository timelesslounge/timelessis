import unittest.mock
import pytest
import werkzeug.exceptions

from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method
from timeless.access_control.views import SecuredView


# @todo #181:30min This test stopped working because it was not working
#  according to requirements.
#  Write new tests that validate 'is_allowed' according to specifications in #22
@pytest.mark.skip("fix me")
def test_owner_can_access_location():
    assert is_allowed(method=Method.DELETE, resource="location")


@pytest.fixture
def secured_view(app):
    view = SecuredView()
    view.resource = "test-resource"
    with app.test_request_context("/", method="POST"):
        yield view


@unittest.mock.patch("timeless.access_control.authorization.is_allowed")
def test_secured_view_access_ok(mocked_is_allowed, secured_view, app):
    mocked_is_allowed.return_value = True
    with pytest.raises(AssertionError):
        secured_view.dispatch_request()


@unittest.mock.patch("timeless.access_control.authorization.is_allowed")
def test_secured_view_access_forbidden(mocked_is_allowed, secured_view, app):
    mocked_is_allowed.return_value = False
    with pytest.raises(werkzeug.exceptions.Forbidden):
        secured_view.dispatch_request()
