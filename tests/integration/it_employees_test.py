"""Integration tests for Employees"""
import pytest
from http import HTTPStatus
from flask import url_for
from datetime import datetime

from tests import factories
from timeless.employees.models import Employee


def test_insert_employee(db_session):
    """Integration test for adding and selecting Employee"""
    company = factories.CompanyFactory()
    manager_role = factories.RoleFactory()
    employee = factories.EmployeeFactory(company=company, role=manager_role)
    row = db_session.query(Employee).get(employee.id)
    assert row.username == employee.username


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
    """ Create new instance of Employee to reuse it in other tests """
    return Employee(first_name="John",
                    last_name="Smith",
                    username="john",
                    phone_number="123",
                    birth_date=datetime.utcnow(),
                    registration_date=datetime.utcnow(),
                    account_status="A",
                    user_status="Working",
                    email="test@test.com",
                    password="bla",
                    pin_code=1234,
                    comment="No comments",
    )


def test_list(client, db_session):
    """ List all employees """
    company = factories.CompanyFactory()
    manager_role = factories.RoleFactory()
    employee = factories.EmployeeFactory(company=company, role=manager_role)
    response = client.get(url_for("employee.list"))
    assert response.status_code == HTTPStatus.OK
    assert str.encode(employee.username) in response.data


def test_create(client, db_session):
    assert client.get("/employees/create").status_code == HTTPStatus.OK
    employee_data = {"first_name": "Alice",
                     "last_name": "Brown",
                     "username": "alice",
                     "phone_number": "876",
                     "birth_date": datetime(2019, 2, 1, 0, 0).date(),
                     "registration_date": datetime(2019, 2, 1, 0, 0),
                     "account_status": "A",
                     "user_status": "Working",
                     "email": "test@test.com",
                     "password": "pwd1",
                     "pin_code": 1234,
                     "comment": "No comments",
    }
    client.post(url_for("employee.create"), data=employee_data)
    assert Employee.query.count() == 1

"""
@todo #411:30min Lets fix the test. Currently it fails because of passed form is not being valid, failing
 with 'Already exists.' message for username and pincode. Remember to uncomment Edit view for employee.
"""
@pytest.mark.skip
def test_edit(client):
    employee = factories.EmployeeFactory(comment="No comments")
    persisted = Employee.query.get(employee.id)
    assert persisted.comment == "No comments"
    client.post(
        url_for('employee.edit', id=employee.id), data={"comment": "One comment"})
    persisted = Employee.query.get(employee.id)
    assert persisted.comment == "One comment"
    """fails"""


@pytest.mark.skip
def test_delete(client):
    employee = factories.EmployeeFactory()
    response = client.post(url_for('employee.delete', id=employee.id))
    assert response.status_code == HTTPStatus.FOUND
    assert not Employee.query.count()
