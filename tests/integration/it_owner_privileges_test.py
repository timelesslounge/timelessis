""" Tests for privilege of owner. """

from datetime import datetime

import flask
import pytest
from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.roles.models import Role

from timeless.restaurants.models import Location

from tests import factories


@pytest.fixture
def clean_app(app):
    """ Fixture for cleaning global variables in tests. """
    flask.g.user = None


def test_cant_access_unknown_resource(clean_app):
    assert not has_privilege(method=Method.CREATE, resource="unknown")


def test_cant_access_his_profile(clean_app):
    assert not has_privilege(
        method=Method.READ, resource="employee", employee_id=1)


def test_can_access_his_profile(clean_app):
    flask.g.user = factories.EmployeeFactory()
    assert has_privilege(
        method=Method.READ, resource="employee", employee_id=flask.g.user.id)


def test_can_access_own_employees(clean_app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1", account_status="T",
                      birth_date=datetime.utcnow(), pin_code=1234,
                      registration_date=datetime.utcnow(), user_status="T",
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee")


def test_can_manage_locations_from_same_company(clean_app, db_session):
    my_company = Company(
        name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    me = Employee(
        first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=7777,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="test@test.com", password="bla"
    )
    db_session.add(me)
    flask.g.user = me
    location = Location(
        name="name",
        code="123",
        company_id=my_company.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    db_session.add(location)
    db_session.commit()
    assert has_privilege(
        method=Method.READ, resource="location", id=location.id
    )
    assert has_privilege(
        method=Method.CREATE, resource="location", id=location.id
    )
    assert has_privilege(
        method=Method.UPDATE, resource="location", id=location.id
    )
    assert has_privilege(
        method=Method.DELETE, resource="location", id=location.id
    )


def test_can_not_manage_locations_from_different_company(clean_app, db_session):
    my_company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    me = Employee(
        id=1, first_name="Bob", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=1111,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="bob@test.com", password="bla"
    )
    db_session.add(me)
    flask.g.user = me
    other_company = Company(
        id=2, name="Bar Inc.", code="code2", address="addr"
    )
    db_session.add(other_company)
    location = Location(
        name="name",
        code="123",
        company_id=other_company.id,
        country="US",
        region="region",
        city="city",
        address="address",
        longitude="123",
        latitude="123",
        type="type",
        status="status"
    )
    db_session.add(location)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="location", id=location.id
    )
    assert not has_privilege(
        method=Method.CREATE, resource="location", id=location.id
    )
    assert not has_privilege(
        method=Method.UPDATE, resource="location", id=location.id
    )
    assert not has_privilege(
        method=Method.DELETE, resource="location", id=location.id
    )


@pytest.mark.parametrize("method", (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE,
))
def test_can_manage_employees_from_same_company(method, clean_app):
    me = factories.EmployeeFactory(company=factories.CompanyFactory())
    colleague = factories.EmployeeFactory(company=me.company)
    flask.g.user = me
    assert has_privilege(
        method=method, resource="employee", employee_id=colleague.id)


@pytest.mark.parametrize("method", (
    Method.READ,
    Method.CREATE,
    Method.UPDATE,
    Method.DELETE,
))
def test_can_not_manage_employees_from_different_company(method, clean_app):
    me = factories.EmployeeFactory(company=factories.CompanyFactory())
    someone = factories.EmployeeFactory(company=factories.CompanyFactory())
    flask.g.user = me
    assert not has_privilege(
        method=method, resource="employee", employee_id=someone.id)
