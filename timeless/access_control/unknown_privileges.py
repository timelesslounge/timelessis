""" Permissions for Unknown roles """


def has_privilege(*args, resource=None, **kwargs) -> bool:
    """unknow role does not have any privileges."""
    return False


def __employee_access(*args, **kwargs):
    """Owner of this role cannot see anything"""
    return False


