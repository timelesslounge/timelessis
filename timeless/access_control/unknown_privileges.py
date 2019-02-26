""" Permissions for Unknown roles """


def has_privilege(*args, resource=None, **kwargs) -> bool:
    """Unknown role does not have any privileges."""
    return False


