from flask import g

from timeless.access_control.methods import Method


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Owner role can access a particular resource.
    @todo #180:30min Implement the rest of the owner privileges.
     1) Create /modify /activate /deactivate accounts for all Employee
     associated with owned Company
    """
    return __resources.get(resource, lambda *arg: False)(method, *args, **kwargs)


def __location_access(method=None, *args, **kwargs):
    """
    @todo #22:30min Implement __location_access. Owner should
     Create / modify / delete Locations associated with owned Company.
     Fetch owner from g.user (if it doesnt exist than fetch its id from
     session. Location id can be obtained from args.
    """
    permitted = False
    if method in (Method.CREATE, Method.UPDATE, Method.DELETE):
        permitted = True
    return permitted


def __employee_access(method=None, *args, **kwargs):
    permitted = False
    user = g.pop("user", None)
    employee_id = kwargs.get("employee_id")
    if method == Method.READ and user:
        if not employee_id:
            permitted = True
        else:
            permitted = method == Method.READ and employee_id == user.id
    return permitted


__resources = {
    "location": __location_access,
    "employee": __employee_access
}
