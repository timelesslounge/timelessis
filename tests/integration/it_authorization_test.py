import flask
import pytest

from tests import factories
from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method
from timeless.roles.models import RoleType


@pytest.mark.parametrize('role_name,role_type', (
        ("manager", RoleType.Manager),
        ("director", RoleType.Director),
        ("administrator", RoleType.Administrator),
        ("owner", RoleType.Owner),
))
def test_can_access_employee_resource(role_name, role_type):
    print('role_type', role_type)
    my_company = factories.CompanyFactory()
    my_role = factories.RoleFactory(
        name=role_name, role_type=role_type)
    # set my role
    me = factories.EmployeeFactory(company=my_company, role=my_role)
    flask.g.user = me
    # set employee
    other = factories.EmployeeFactory(company=my_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )
