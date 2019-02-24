import flask

from timeless.access_control.methods import Method
from timeless.employees.models import Employee


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Manager role can access a particular resource."""
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __employee_access(method=None, *args, **kwargs):
    permitted, user = False, flask.g.get("user")
    employee_id = kwargs.get("employee_id")
    if user:
        if employee_id:
            permitted = check_employee(employee_id, method, user)
        else:
            permitted = True
    return permitted


def check_employee(employee_id, method, user):
    if employee_id == user.id:
        return True

    employee = Employee.query.get(employee_id)
    if user.company_id != employee.company_id:
        # User cannot do anything if employee does not belong to his company
        return False

    # Manager can edit not own account only if it is a master or intern
    return employee.role.is_master_or_intern()


__resources = {
    "employee": __employee_access,
}
