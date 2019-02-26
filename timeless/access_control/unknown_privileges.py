""" Permissions for Unknown roles
@todo #182:30min Create tests for `unknown_privilege.has_privilege`. Users
 which does not have eny privilege should fall into this category and doesn't
 have access to any part of the system.
"""


def has_privilege(*args, resource=None, **kwargs):
    """Unknown role does not have any privileges."""
    return False
