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
    @todo #22:30min Get role from actual user instead of using
     hardcoded value. User can be fetched from g.user. Make sure
     that access is not allowed for unknown role.
    @todo #242:30min Implement the rest of the owner privileges.
     Owner should be able to create, modify, activate and deactivate accounts
     for employess of his/her company. Create the tests for each of this
     operation..
    """

    return __roles(g.user.role.name, "unknown").has_privilege(
        method=method, resource=resource, args=args, kwargs=kwargs
    )


__roles = {
    "owner": owner_privileges,
    "manager": manager_privileges,
    "director": director_privileges,
    "administrator": administrator_privileges,
    "other": other_privileges,
    "unknown": unknown_privileges
}
