from datetime import datetime

import flask
import pytest

from tests import factories
from timeless.access_control.director_privileges import has_privilege
from timeless.access_control.methods import Method
from timeless.employees.models import Employee
from timeless.roles.models import RoleType


def test_can_access_if_no_profile(app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                            username="alice", phone_number="1",
                            birth_date=datetime.utcnow(),
                            pin_code=1111,
                            account_status="on",
                            user_status="on",
                            registration_date=datetime.utcnow(),
                            email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee")


def test_can_access_his_profile(app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      pin_code=9999,
                      account_status="on",
                      user_status="on",
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee", employee_id=1)


@pytest.mark.parametrize('method', (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE,
))
def test_cannot_access_other_company_employees(method,app, db_session):
    """
    Even though the authenticated user is a director, they cannot access a
    manager's profile because the manager works for another company.
    """
    director = factories.EmployeeFactory(
        company=factories.CompanyFactory(),
        role=factories.RoleFactory(
            name="Director"
        )
    )
    manager = factories.EmployeeFactory(
        company=factories.CompanyFactory(),
        role=factories.RoleFactory(
            name="Manager"
        )
    )
    flask.g.user = director
    assert not has_privilege(
        method=Method.READ, resource="employee", employee_id=manager.id
    )


@pytest.mark.parametrize('method', (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE,
))
def test_can_access_subalterns(method, app, db_session):
    """
    A director of a company should be able to access
    the profiles of employees with a lower role.
    """
    company = factories.CompanyFactory()

    director = factories.EmployeeFactory(
        company=company,
        role=factories.RoleFactory(
            role_type=RoleType.Director
        )
    )
    master = factories.EmployeeFactory(
        company=company,
        role=factories.RoleFactory(
            role_type=RoleType.Master
        )
    )
    manager = factories.EmployeeFactory(
        company=company,
        role=factories.RoleFactory(
            role_type=RoleType.Manager
        )
    )
    intern = factories.EmployeeFactory(
        company=company,
        role=factories.RoleFactory(
            role_type=RoleType.Intern
        )
    )
    flask.g.user = director
    assert has_privilege(
        resource="employee", employee_id=manager.id
    )
    assert has_privilege(
        resource="employee", employee_id=master.id
    )
    assert has_privilege(
        resource="employee", employee_id=intern.id
    )
