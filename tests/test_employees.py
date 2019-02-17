from datetime import datetime
from pytest import raises
from timeless.employees.models import Employee


def test_new_employee():
    birth_date = datetime.utcnow()
    registration_date = datetime.utcnow()
    created_on = datetime.utcnow(),
    employee = Employee(username="alice", password="coop1", first_name="Alice",
                        last_name="Cooper", phone_number="1223", pin_code=1234,
                        birth_date=birth_date, email="test@test.com",
                        registration_date=registration_date,
                        created_on=created_on,
                        account_status="Not Activated", user_status="Working")
    assert (employee.first_name == "Alice" and
            employee.last_name == "Cooper" and
            employee.account_status == "Not Activated" and
            employee.user_status == "Working" and
            employee.pin_code == 1234 and
            employee.created_on is not None and
            len(str(employee.pin_code)) == 4 and
            employee.registration_date == registration_date)


def test_missing_required_params():
    with raises(KeyError, match="Missing required param: password"):
        Employee(username="bob", first_name="Bob")
    with raises(KeyError, match="Missing required param: phone_number"):
        Employee(username="bob", password="bob1", first_name="Bob",
                 last_name="Dylan", birth_date=datetime.utcnow,
                 email="bob@bob.com")
