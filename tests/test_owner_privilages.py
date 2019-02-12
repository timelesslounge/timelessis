from datetime import datetime

import flask

from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege
from timeless.employees.models import Employee


def test_can_access_location():
    assert (
            has_privilege(method=Method.CREATE, resource="location")
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
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert (
            has_privilege(method=Method.READ, resource="employee", employee_id=1)
    )


def test_can_access_own_employees():
    """@todo #180:30min We need to clean global object after test finish
     its execution to prevent collision with other tests. Probably we need
     to make a pytest fixture for this.
    """
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert (has_privilege(method=Method.READ, resource="employee"))

