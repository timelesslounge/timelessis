from timeless.access_control import owner_privileges


def is_allowed(method=None, resource=None, **kwargs) -> bool:
    """ Check if user can access particular resource for a given method.
    @todo 22:30min Get role from actual user instead of using
     hardcoded value. User can be fetched from g.user. Make sure
     that access is not allowed for unknown role.
    """
    return __roles.get("owner").has_privilege(method=method, resource=resource, kwargs=kwargs)

__roles = {
    "owner": owner_privileges
}

