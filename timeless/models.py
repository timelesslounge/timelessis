from datetime import datetime
from timeless import DB


class TimestampsMixin(object):
    """Mixin for adding created_on and updated_on attributes
     to any models that need to keep track of their updates.
    """
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(
        DB.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=False
    )
