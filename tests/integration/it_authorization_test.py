import flask
import pytest

from tests import factories
from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method
from timeless.roles.models import RoleType


def test_manager_can_access_employee():
    my_company = factories.CompanyFactory()
    manager_role = factories.RoleFactory(
        name="manager", role_type=RoleType.Manager)
    # set manager role
    me = factories.EmployeeFactory(company=my_company, role=manager_role)
    flask.g.user = me
    other = factories.EmployeeFactory(company=my_company)  # set role to master
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_director_can_access_manager():
    my_company = factories.CompanyFactory()
    director_role = factories.RoleFactory(
        name="director", role_type=RoleType.Director)
    # set director role
    me = factories.EmployeeFactory(company=my_company, role=director_role)
    flask.g.user = me
    other = factories.EmployeeFactory(company=my_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_administrator_can_access_director_from_other_company():
    my_company = factories.CompanyFactory()
    administrator_role = factories.RoleFactory(
        name="administrator", role_type=RoleType.Administrator)
    # set role to administrator
    me = factories.EmployeeFactory(company=my_company, role=administrator_role)
    flask.g.user = me
    other_company = factories.CompanyFactory()
    # set role to director
    other = factories.EmployeeFactory(company=other_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_owner_can_access_director():
    my_company = factories.CompanyFactory()
    owner_role = factories.RoleFactory(
        name="owner", role_type=RoleType.Owner)
    # set owner role
    me = factories.EmployeeFactory(company=my_company, role=owner_role)
    flask.g.user = me
    # set role to director
    other = factories.EmployeeFactory(company=my_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )

