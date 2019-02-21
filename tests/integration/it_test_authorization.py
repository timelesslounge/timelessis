import flask
import pytest

from tests import factories
from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method


# @todo #329:30min After #298 is finished update this test cases with
#  appropriate roles and make sure that current test cases diffrentiate enough
#  between roles, so we can be sure that is_allowed takes into account all
#  exiting roles. Also remove pytest.mark.skip from all test methods here.
def test_manager_can_access_employee():
    my_company = factories.CompanyFactory()
    me = factories.EmployeeFactory(company=my_company)  # set role to manager
    flask.g.user = me
    other = factories.EmployeeFactory(company=my_company)  # set role to master
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_director_can_access_manager():
    my_company = factories.CompanyFactory()
    me = factories.EmployeeFactory(company=my_company)  # set role to director
    flask.g.user = me
    other = factories.EmployeeFactory(company=my_company)  # set role to manager
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


@pytest.mark.skip()
def test_administrator_can_access_director_from_other_company():
    my_company = factories.CompanyFactory()
    # set role to administrator
    me = factories.EmployeeFactory(company=my_company)
    flask.g.user = me
    other_company = factories.CompanyFactory()
    # set role to director
    other = factories.EmployeeFactory(company=other_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_owner_can_access_director():
    my_company = factories.CompanyFactory()
    me = factories.EmployeeFactory(company=my_company)  # set role to owner
    flask.g.user = me
    # set role to director
    other = factories.EmployeeFactory(company=my_company)
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


