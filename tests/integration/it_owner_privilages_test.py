""" Tests for privilage of user.
"""

from datetime import datetime

import flask
import pytest
from timeless.access_control.methods import Method
from timeless.access_control.owner_privileges import has_privilege
from timeless.employees.models import Employee


@pytest.fixture
def clean_app(app):
    """ Fixture for cleaning global variables in tests. """
    flask.g.user = None

def test_can_access_location(clean_app):
    assert has_privilege(method=Method.CREATE, resource="location")


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
