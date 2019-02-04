from timeless.access_control.methods import Method


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Owner role can access a particular resource.
    @todo 22:30min Implement the rest of the owner privileges.
     1) Create/modify/activate/deactivate accounts for all Employee
     associated with owned Company
     2) View self-profile
     3) View Employee profiles associated with owned Company
    """
    return __resources.get(resource, lambda *arg: False)(method, args)


def __location_access(method=None, *args):
    """
    @todo 22:30min Implement __location_access. Owner should
     Create / modify / delete Locations associated with owned Company.
     Fetch owner from g.user (if it doesn't exist than fetch it's id from
     session. Location id can be obtained from args.
    """
    permitted = False
    if method in (Method.CREATE, Method.UPDATE, Method.DELETE):
        permitted = True
    return permitted


__resources = {
    "location": __location_access
}
