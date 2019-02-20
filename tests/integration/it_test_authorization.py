import random
import string
from datetime import datetime

import flask
import pytest

from timeless.access_control.authorization import is_allowed
from timeless.access_control.methods import Method
from timeless.companies.models import Company
from timeless.employees.models import Employee


# @todo #329:30min After #298 is finished update this test cases with
#  appropriate roles and make sure that current test cases diffrentiate enough
#  between roles, so we can be sure that is_allowed takes into account all
#  exiting roles. Also remove pytest.mark.skip from all test methods here.
def test_manager_can_access_employee(app, db_session):
    my_company = Company(
        name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    me = create_employee(my_company, "manager")
    db_session.add(me)
    flask.g.user = me
    other = create_employee(my_company, "master")
    db_session.add(other)
    db_session.commit()
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_director_can_access_manager(app, db_session):
    my_company = Company(
        name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    me = create_employee(my_company, "director")
    db_session.add(me)
    flask.g.user = me
    other = create_employee(my_company, "manager")
    db_session.add(other)
    db_session.commit()
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


@pytest.mark.skip()
def test_administrator_can_access_director_from_other_company(app, db_session):
    my_company = Company(
        name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    me = create_employee(my_company, "administrator")
    db_session.add(me)
    flask.g.user = me
    other_company= Company(
        name="Foo Inc.", code="code1", address="addr"
    )
    db_session.add(other_company)
    other = create_employee(other_company, "director")
    db_session.add(other)
    db_session.commit()
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_owner_can_access_director(app, db_session):
    my_company = Company(
        name="Acme Inc.", code="code1", address="addr"
    )
    db_session.add(my_company)
    db_session.commit()
    me = create_employee(my_company, "owner")
    db_session.add(me)
    flask.g.user = me
    other = create_employee(my_company, "director")
    db_session.add(other)
    db_session.commit()
    assert is_allowed(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def create_employee(my_company, role):
    return Employee(
        first_name=random_string(),
        last_name="Cooper",
        username=random_string(), phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=random_number(4),
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=my_company.id,
        email="test@test.com", password="bla"
    )


def random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


def random_number(n):
    return ''.join(random.choices(string.digits, k=n))
