from datetime import datetime
from timeless.employees.models import Employee


def test_insert_employee(db_session):
    """Integration test for adding and selecting Employee"""
    employee = Employee(
            first_name="Alice", last_name="Cooper",
            username="alice", phone_number="1", birth_date=datetime.utcnow(),
            registration_date=datetime.utcnow(), account_status="A",
            user_status="Working", email="test@test.com", password="bla",
            pin_code=123
            )
    db_session.add(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.username == "alice"


def test_timestamp_mixin(db_session):
    """Integration test for testing TimestampsMixin"""
    before = datetime.utcnow()
    employee = Employee(
        first_name="John", last_name="Smith",
        username="john", phone_number="123", birth_date=datetime.utcnow(),
        registration_date=datetime.utcnow(), account_status="A",
        user_status="Working", email="test@test.com", password="bla",
        pin_code=1234
    )
    db_session.add(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.created_on > before
    assert row.updated_on > before
    old_created_on = row.created_on
    old_updated_on = row.updated_on
    employee.email = "test@example.com"
    db_session.merge(employee)
    db_session.commit()
    row = db_session.query(Employee).get(employee.id)
    assert row.created_on == old_created_on
    assert row.updated_on > old_updated_on
