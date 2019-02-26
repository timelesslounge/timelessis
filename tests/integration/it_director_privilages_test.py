from datetime import datetime

import flask

from timeless.access_control.director_privileges import has_privilege
from timeless.access_control.methods import Method
from timeless.companies.models import Company
from timeless.employees.models import Employee
from timeless.roles.models import Role


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


def test_cannot_access_other_company_employees(app, db_session):
    mine_company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    db_session.add(mine_company)
    me = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=1234,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=2,
        email="test@test.com", password="bla"
    )
    db_session.add(me)
    flask.g.user = me
    other_company = Company(
        id=2, name="Bar Inc.", code="code2", address="addr"
    )
    db_session.add(other_company)
    other = Employee(
        id=2, first_name="Bob", last_name="Cooper",
        username="bob", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3454,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=1,
        email="test@test.com", password="bla"
    )
    db_session.add(other)
    db_session.commit()
    assert not has_privilege(
        method=Method.READ, resource="employee", employee_id=other.id
    )


def test_can_access_subalterns(app, db_session):
    """
    A director of a company should be able to access
    the profiles of employees with a lower role.
    """
    company = Company(
        id=1, name="Foo Inc.", code="code1", address="addr"
    )
    db_session.add(company)

    dir_role = Role(id=1, name="director",company_id=1)
    master_role = Role(id=2, name="master",company_id=1)
    manager_role = Role(id=3, name="manager",company_id=1)
    intern_role = Role(id=4, name="intern",company_id=1)
    db_session.add(dir_role)
    db_session.add(master_role)
    db_session.add(manager_role)
    db_session.add(intern_role)

    director = Employee(
        id=1, first_name="Alice", last_name="Cooper",
        username="alice", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=1234,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=2,
        role_id=1,
        email="alice@test.com", password="bla"
    )
    db_session.add(director)
    flask.g.user = director
    master = Employee(
        id=2, first_name="Bob", last_name="Cooper",
        username="bob", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3454,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=1,
        role_id=2,
        email="bob@test.com", password="bla"
    )
    manager = Employee(
        id=3, first_name="Rod", last_name="Stewart",
        username="rob", phone_number="2",
        birth_date=datetime.utcnow(),
        pin_code=3454,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=1,
        role_id=3,
        email="rob@test.com", password="bla"
    )
    intern = Employee(
        id=4, first_name="Johnny", last_name="Good",
        username="jon", phone_number="1",
        birth_date=datetime.utcnow(),
        pin_code=3454,
        account_status="on",
        user_status="on",
        registration_date=datetime.utcnow(),
        company_id=1,
        role_id=4,
        email="jon@test.com", password="bla"
    )
    db_session.add(master)
    db_session.add(manager)
    db_session.add(intern)
    db_session.commit()

    assert has_privilege(
        method=Method.READ, resource="employee", employee_id=manager.id
    )
    assert has_privilege(
        method=Method.READ, resource="employee", employee_id=master.id
    )
    assert has_privilege(
        method=Method.READ, resource="employee", employee_id=intern.id
    )
