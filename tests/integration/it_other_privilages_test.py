import flask
import pytest

from tests import factories
from timeless.access_control.other_privileges import has_privilege
from timeless.access_control.methods import Method


@pytest.mark.parametrize("method", (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE
))
def test_can_access_to_emloyee_resource(method, app):
    """ Check that user can access only to own employee account """
    employee = factories.EmployeeFactory()
    flask.g.user = employee
    assert has_privilege(
        method=method, resource="employee", employee_id=employee.id)
    assert not has_privilege(
        method=method, resource="employee", employee_id=-1)
