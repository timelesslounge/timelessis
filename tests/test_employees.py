from timeless.employees.models import Employee


def test_new_employee():
    employee = Employee(first_name="Alice", last_name="Cooper")
    assert (employee.first_name == "Alice"
            and employee.last_name == "Cooper")
