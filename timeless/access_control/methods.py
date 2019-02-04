from enum import Enum


class Method(Enum):
    """Method that a user can execute on a particular resource
    """
    CREATE = "post"
    UPDATE = "put"
    DELETE = "delete"

