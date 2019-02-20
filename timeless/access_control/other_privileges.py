""" Permissions for Master / Intern / Others roles """
import flask


def has_privilege(resource=None, *args, **kwargs) -> bool:
    """Check if user with Master / Intern / Others role can access a
    particular resource."""
    return __resources.get(resource, lambda *arg: False)(*args, **kwargs)


def __employee_access(*args, **kwargs):
    """Owner of this role can view and update only self"""
    user = flask.g.get("user")
    return kwargs.get("employee_id") == user.id if user else False


__resources = {
    "employee": __employee_access
}
