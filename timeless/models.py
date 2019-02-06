from datetime import datetime
from timeless import DB


class TimestampsMixin(object):
    """Mixin for adding created_on and updated_on attributes
     to any models that need to keep track of their updates.
    @todo #40:30min Create a unit test for TimestampsMixin. We need to check if
     created_on field is correctly populated, and updated_on field is correctly
     updated.
    """
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(
        DB.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=False
    )
