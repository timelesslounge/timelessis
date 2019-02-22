import flask

from timeless.restaurants.models import Table


def has_privilege(method=None, resource=None, *args, **kwargs) -> bool:
    """Check if user with Location Admin role can access a particular resource.
    """
    return __resources.get(resource, lambda *arg: False)(
        method, *args, **kwargs
    )


def __table_access(method=None, *args, **kwargs):
    """Check if a user has access to a location's tables
    @todo #177:30min Continue implementing access check for reservations,
     reservation settings and reservation comments. Don't forget to add
     integration tests. See issue #22 as reference for what a Location Admin
     should be able to do.
    """
    permitted, user = False, flask.g.get("user")
    table_id = kwargs.get("id")
    if user and table_id:
        if Table.query.get(table_id).floor.location.company_id == user.company_id:
            permitted = True
    return permitted


__resources = {
    "tables": __table_access
}
