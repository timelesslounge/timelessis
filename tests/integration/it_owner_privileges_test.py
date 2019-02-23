''""" Tests for privilege of owner.
"""

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
    assert not has_privilege(method=Method.READ, resource="employee", employee_id=1)


def test_can_access_his_profile(clean_app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1", account_status="T",
                      birth_date=datetime.utcnow(), pin_code=1234,
                      registration_date=datetime.utcnow(), user_status="T",
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee", employee_id=1)


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

@pytest.mark.skip(reason="Implement owner privileges to check for company")
def test_can_manage_employees_from_same_company(clean_app, db_session):
    my_company = Company(
        name="Mothers Of Invention Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    role = Role(
        id = 1,
        name = "owner",
        works_on_shifts = False,
        company_id = my_company.id
    )
    db_session.add(role)
    db_session.commit()
    boss = Employee(
        first_name="Frank", last_name="Zappa",
        username="frank", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=1248,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="fank@mothers.com",
        password="bla",
        role_id=role.id
    )
    db_session.add(boss)
    db_session.commit()
    flask.g.user = boss
    employee = Employee(
        first_name="Jack", last_name="Black",
        username="jack", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=5648,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="jack@black.com",
        password="bla"
    )
    db_session.add(employee)
    db_session.commit()
    assert has_privilege(
        method=Method.READ, resource="employee", id=employee.id
    )
    assert has_privilege(
        method=Method.CREATE, resource="employee"
    )
    assert has_privilege(
        method=Method.UPDATE, resource="employee", id=employee.id
    )
    assert has_privilege(
        method=Method.DELETE, resource="employee", id=employee.id
    )


@pytest.mark.skip(reason="Implement owner privileges to check for company")
def test_can_not_manage_employees_from_different_company(clean_app, db_session):
    boss_company = Company(
        name="Mothers Of Invention Inc.", code="code1", address="addr"
    )
    db_session.add(boss_company)
    db_session.commit()
    owner_role = Role(
        id = 1,
        name = "owner",
        works_on_shifts = False,
        company_id = boss_company.id
    )
    db_session.add(owner_role)
    db_session.commit()
    boss = Employee(
        first_name="Frank", last_name="Zappa",
        username="frank", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=6547,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=boss_company.id,
        email="fank@mothers.com",
        password="bla",
        role_id=owner_role.id
    )
    db_session.add(boss)
    flask.g.user = boss
    employee_company = Company(
        name="Damage Inc.", code="code2", address="addr"
    )
    db_session.add(employee_company)
    db_session.commit()
    employee_role = Role(
        id = 2,
        name = "employee",
        works_on_shifts = False,
        company_id = employee_company.id
    )
    db_session.add(employee_role)
    db_session.commit()
    employee = Employee(
        first_name="James", last_name="Hetfield",
        username="jaymz", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=7777,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=employee_company.id,
        email="jaymz@metallica.com",
        password="bla",
        role_id=employee_role.id
    )
    db_session.add(employee)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="employee", id=employee.id
    )
    assert not has_privilege(
        method=Method.CREATE, resource="employee"
    )
    assert not has_privilege(
        method=Method.UPDATE, resource="employee", id=employee.id
    )
    assert not has_privilege(
        method=Method.DELETE, resource="employee", id=employee.id
    )
