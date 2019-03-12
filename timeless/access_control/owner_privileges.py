import flask

from timeless.access_control.methods import Method
from timeless.employees.models import Employee
from timeless.restaurants.models import Location


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Owner role can access a particular resource."""
    return __resources.get(
        resource, lambda *arg, **kwargs: False)(method, *args, **kwargs)


def __location_access(method=None, *args, **kwargs):
    user_company = flask.g.get("user").company_id
    location_company = Location.query.get(kwargs.get("id")).company_id
    return user_company == location_company


def __employee_access(method=None, *args, **kwargs):
    user, employee_id = flask.g.user, kwargs.get("employee_id")
    if not employee_id:
        return True

    employee = Employee.query.get(employee_id)

    if not employee:
        return False

    return employee.company_id == user.company_id


def __company_access(method=None, *args, **kwargs):
    user, company_id = flask.g.get("user"), kwargs.get("company_id")
    return user.company_id == company_id


__resources = {
    "location": __location_access,
    "employee": __employee_access,
    "company": __company_access,
    "reservation_settings": __employee_access,
    "reservation_comment": __employee_access
}
