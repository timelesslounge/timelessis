"""Integration tests for Employees"""
import pytest
from http import HTTPStatus
from flask import url_for, g
from datetime import datetime

from tests import factories
from timeless.employees.models import Employee
from timeless.roles.models import Role, RoleType

"""
@todo #278:30min Tests are not using secured views. We should authenticate users 
 to test correct behavior in employee views tests. Correct the tests mocking 
 user authentication and role information and then uncomment skipped tests.  
"""


def test_insert_employee(db_session):
    """Integration test for adding and selecting Employee"""
    employee = factories.EmployeeFactory(
        company=factories.CompanyFactory(), role=factories.RoleFactory()
    )
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


@pytest.mark.skip(reason="Authentication injection not implemented")
def test_list(client, db_session):
    """ List all employees """
    company = factories.CompanyFactory()
    manager_role = factories.RoleFactory()
    employee = factories.EmployeeFactory(company=company, role=manager_role)
    response = client.get(url_for("employee.list"))
    assert response.status_code == HTTPStatus.OK
    assert str.encode(employee.username) in response.data


def test_cannot_access_list(client, db_session):
    """ Show 403 - Forbidden when user cannot access employee list """
    company = factories.CompanyFactory()
    manager_role = factories.RoleFactory()
    employee = factories.EmployeeFactory(company=company, role=manager_role)
    response = client.get(url_for("employee.list"))
    assert response.status_code == HTTPStatus.FORBIDDEN


@pytest.mark.skip(reason="Authentication injection not implemented")
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


def test_cannot_access_create(client, db_session):
    """ Show 403 - Forbidden when user cannot access employee list """
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
    assert client.get("/employees/create").status_code == HTTPStatus.FORBIDDEN


"""
@todo #412:30min timeless/employees/views.py::Delete is not working. Fix it and 
 then uncomment the tests below. Also refactor Delete to EmployeeDeleteView to
 make it uniform with the rest of the applicaton. 
"""


@pytest.mark.skip(reason="Correct EmployeeDeleteView")
def test_delete(client):
    company = factories.CompanyFactory()
    intern = factories.EmployeeFactory(
        company=company, role_id=Role(role_type=RoleType.Intern.name).id
    )
    boss = factories.EmployeeFactory(
        company=company, role_id=Role(role_type=RoleType.Manager.name).id
    )
    with client.session_transaction() as session:
        session["user_id"] = boss.id
    g.user = boss
    intern_id = intern.id
    response = client.post(url_for("employee.delete", id=intern_id))
    assert len(Employee.query.all()) == 1
    assert Employee.query.get(intern_id) is None
    assert response.status_code == HTTPStatus.OK


def test_cannot_delete(client, db_session):
    """ Show 403 - Forbidden when user cannot access employee list """
    employee = factories.EmployeeFactory()
    response = client.post(url_for('employee.delete', id=employee.id))
    assert response.status_code == HTTPStatus.FORBIDDEN
