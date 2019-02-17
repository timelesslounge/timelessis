from datetime import datetime

import flask

from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege
from timeless.employees.models import Employee
import pytest


@pytest.fixture
def clean_app(app):
    user = getattr(flask.g, "user", None)
    if(user != None):
        flask.g.user = None

def test_can_access_location(clean_app):
    assert has_privilege(method=Method.CREATE, resource="location")


def test_cant_access_unknown_resource(clean_app):
    assert not has_privilege(method=Method.CREATE, resource="unknown")


def test_cant_access_his_profile(clean_app):
    assert not has_privilege(method=Method.READ, resource="employee", employee_id=1)


def test_can_access_his_profile(clean_app):
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee", employee_id=1)


def test_can_access_own_employees(clean_app):
    """
    @todo #180:30min We need to clean global object after test finish
     its execution to prevent collision with other tests. Probably we need
     to make a pytest fixture for this.
    """
    flask.g.user = Employee(id=1, first_name="Alice", last_name="Cooper",
                      username="alice", phone_number="1",
                      birth_date=datetime.utcnow(),
                      registration_date=datetime.utcnow(),
                      email="test@test.com", password="bla")
    assert has_privilege(method=Method.READ, resource="employee")

