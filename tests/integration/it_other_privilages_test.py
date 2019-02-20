import flask
import pytest

from tests import factories
from timeless.access_control.other_privileges import has_privilege
from timeless.access_control.methods import Method


@pytest.mark.parametrize('method', (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE
))
def test_can_access_to_self_account(method, app):
    employee = factories.EmployeeFactory()
    flask.g.user = employee
    assert has_privilege(method=method, resource="employee", employee_id=employee.id)


@pytest.mark.parametrize('method', (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE
))
def test_cannot_access_to_foreign_account(method, app):
    employee = factories.EmployeeFactory()
    flask.g.user = employee
    assert not has_privilege(method=method, resource="employee", employee_id=-1)
