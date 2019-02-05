from datetime import datetime
from timeless.employees.models import Employee


def test_new_employee():
    employee = Employee(username="alice", password="coop1", first_name="Alice",
                        last_name="Cooper", phone_number="112233",
                        birth_date=datetime.utcnow(), pin_code=4567,
                        email="test@test.com")
    assert (employee.first_name == "Alice" and
            employee.last_name == "Cooper" and
            employee.account_status == "Not Activated" and
            employee.user_status == "Working" and
            employee.created_on is not None and
            employee.validate_password("coop1") is True)
