from flask import g

from datetime import datetime

from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege
from timeless.employees.models import Employee


def test_can_access_location():
    assert (
            has_privilege(method=Method.CREATE, resource="location") is True
    )


def test_cant_access_unknown_resource():
    assert (
            has_privilege(method=Method.CREATE, resource="unknown") is False
    )


def test_cant_access_his_profile():
    assert (
            has_privilege(method=Method.READ, resource="employee", employee_id=1) is False
    )


def test_can_access_his_profile():
    g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert (
            has_privilege(method=Method.READ, resource="employee", employee_id=1) is True
    )


def test_can_access_own_employees():
    g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert (
            has_privilege(method=Method.READ, resource="employee") is True
    )
