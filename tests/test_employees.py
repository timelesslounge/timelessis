from datetime import datetime
from pytest import raises
from timeless.employees.models import Employee


def test_new_employee():
    employee = Employee(username="alice", password="coop1", first_name="Alice",
                        last_name="Cooper", phone_number="112233",
                        birth_date=datetime.utcnow(), email="test@test.com")
    assert (employee.first_name == "Alice" and
            employee.last_name == "Cooper" and
            employee.account_status == "Not Activated" and
            employee.user_status == "Working" and
            employee.created_on is not None and
            len(str(employee.pin_code)) == 4 and
            employee.validate_password("coop1") is True)


def test_missing_required_params():
    with raises(KeyError, match="Missing required param: password"):
        Employee(username="bob", first_name="Bob")
    with raises(KeyError, match="Missing required param: phone_number"):
        Employee(username="bob", password="bob1", first_name="Bob",
                 last_name="Dylan", birth_date=datetime.utcnow,
                 email="bob@bob.com")
