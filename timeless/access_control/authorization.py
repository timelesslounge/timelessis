from flask import g

from timeless.access_control import (
    administrator_privileges, manager_privileges, other_privileges,
    owner_privileges, director_privileges, unknown_privileges)


def is_allowed(method=None, resource=None, *args, **kwargs) -> bool:
    """ Check if user can access particular resource for a given method.
    Additional information needed for authorization can be passed through
    args or kwargs. This method is meant to work in conjunction with
    SecuredView.dispatch_request so that all available information about
    a user view can be accessible in the authorization process."""

    if g.user is None or g.user.role is None:
        name = "unknown"
    else:
        name = g.user.role["name"]

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
