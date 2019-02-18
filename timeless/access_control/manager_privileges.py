import flask

from timeless.access_control.methods import Method
from timeless.employees.models import Employee


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Manager role can access a particular resource."""
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __employee_access(method=None, *args, **kwargs):
    """
    @todo #176:30min Add role to the employee model and check that Manager
     can only access/modify employees that have role of master or
     interns.
    """
    permitted, user = False, flask.g.get("user")
    employee_id = kwargs.get("employee_id")
    if user:
        if employee_id:
            permitted = check_employee(employee_id, method, user)
        else:
            permitted = True
    return permitted


def check_employee(employee_id, method, user):
    if employee_id == user.id and method == Method.READ:
        return True
    else:
        me = Employee.query.get(user.id)
        other = Employee.query.get(employee_id)
        return me.company_id == other.company_id


__resources = {
    "employee": __employee_access,
}
