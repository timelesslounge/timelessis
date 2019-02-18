from timeless.access_control import owner_privileges
from timeless.access_control import director_privileges
from timeless.access_control import administrator_privileges


def is_allowed(method=None, resource=None, *args, **kwargs) -> bool:
    """ Check if user can access particular resource for a given method.
    Additional information needed for authorization can be passed through
    args or kwargs. This method is meant to work in conjunction with
    SecuredView.dispatch_request so that all available information about
    a user view can be accessible in the authorization process.
    @todo #22:30min Get role from actual user instead of using
     hardcoded value. User can be fetched from g.user. Make sure
     that access is not allowed for unknown role.
    """
    return __roles.get("owner").has_privilege(
        method=method, resource=resource, args=args, kwargs=kwargs
    )


__roles = {
    "owner": owner_privileges,
    "director": director_privileges,
    "administrator": administrator_privileges,
}

