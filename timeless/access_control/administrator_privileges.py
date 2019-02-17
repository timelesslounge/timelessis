def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Administrator role can access a particular resource.
    """
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __location_access(method=None, *args, **kwargs):
    """
    @todo #22:30min Implement __location_access. Owner should
     Create / modify / delete Locations associated with owned Company.
     Fetch owner from g.user (if it doesnt exist than fetch its id from
     session. Location id can be obtained from args.
    """
    return True


def __employee_access(method=None, *args, **kwargs):
    return True


__resources = {
    "location": __location_access,
    "employee": __employee_access
}
