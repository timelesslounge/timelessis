"""Integration tests for Employees"""
from http import HTTPStatus
from flask import url_for
from datetime import datetime

from timeless.employees.models import Employee


def test_insert_employee(db_session):
    """Integration test for adding and selecting Employee"""
    employee = create_employee()
    db_session.add(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.username == "john"


def test_timestamp_mixin_created_on(db_session):
    """Integration test for testing TimestampsMixin created_on field"""
    before = datetime.utcnow()
    employee = create_employee()
    db_session.add(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.created_on > before
    old_created_on = row.created_on
    employee.email = "test@example.com"
    db_session.merge(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.created_on == old_created_on


def test_timestamp_mixin_updated_on(db_session):
    """Integration test for testing TimestampsMixin updated_on field"""
    before = datetime.utcnow()
    employee = create_employee()
    db_session.add(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.updated_on > before
    old_updated_on = row.updated_on
    employee.email = "test@example.com"
    db_session.merge(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.updated_on > old_updated_on


def create_employee():
    """ Create new instance of Employee to reuse in other tests """
    return Employee(
        first_name="John", last_name="Smith",
        username="john", phone_number="123", birth_date=datetime.utcnow(),
        registration_date=datetime.utcnow(), account_status="A",
        user_status="Working", email="test@test.com", password="bla",
        pin_code=1234
    )


def test_list(client, db_session):
    """ List all employees """
    employee = create_employee()
    db_session.add(employee)
    db_session.commit()
    response = client.get(url_for("employee.list"))
    assert response.status_code == HTTPStatus.OK
    assert b"John Smith" in response.data
