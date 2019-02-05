from datetime import datetime
from timeless.employees.models import Employee


def test_new_employee():
    employee = Employee("alice", "coop1", "Alice", "Cooper", "112233",
                        datetime.utcnow(), 4567, "test@test.com")
    assert (employee.first_name == "Alice" and
            employee.last_name == "Cooper" and
            employee.account_status == "Not Activated" and
            employee.user_status == "Working" and
            employee.created_on is not None and
            employee.validate_password("coop1") is True)
