from flask import g

from timeless.access_control import (
    administrator_privileges, manager_privileges, other_privileges,
    owner_privileges, director_privileges, unknown_privileges)


def is_allowed(method=None, resource=None, *args, **kwargs) -> bool:
    """ Check if user can access particular resource for a given method.
    Additional information needed for authorization can be passed through
    args or kwargs. This method is meant to work in conjunction with
    SecuredView.dispatch_request so that all available information about
    a user view can be accessible in the authorization process.
    @todo #358:30min Change checking of this statement below
     `name = g.user.role.name` to `name = g.user.role.role_type` and fix all
     tests, in all tests should be provided role_type instead of name of Role
     model. Example below:
    
    manager_role = factories.RoleFactory(
        name="manager", role_type=RoleType.Manager)
    me = factories.EmployeeFactory(company=my_company, role=manager_role)
    """

    if not g.user or not g.user.role:
        name = "unknown"
    else:
        name = g.user.role.name

    return __roles[name].has_privilege(
        method=method, resource=resource,  *args, **kwargs
    )


__roles = {
    "owner": owner_privileges,
    "manager": manager_privileges,
    "director": director_privileges,
    "administrator": administrator_privileges,
    "other": other_privileges,
    "unknown": unknown_privileges
}
