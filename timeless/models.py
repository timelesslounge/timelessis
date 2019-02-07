from datetime import datetime
from functools import wraps
from timeless import DB


class TimestampsMixin(object):
    """Mixin for adding created_on and updated_on attributes
     to any models that need to keep track of their updates.
    """
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow,
                           nullable=False)
    updated_on = DB.Column(DB.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow, nullable=False)


def validate_required(*expected_args):
    """ Validate input params as mandatory """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in expected_args:
                if arg not in kwargs:
                    raise KeyError("Missing required param: {}".format(arg))
            return func(*args, **kwargs)
        return wrapper
    return decorator
