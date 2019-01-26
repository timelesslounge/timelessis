"""SchemeCondition DB model"""

from datetime import datetime
from timeless import DB


class SchemeCondition(DB.Model):
    """
    @todo #18:30min Continue implementation as in #18. Weekdays, months and dates
     still need to be added -- we'll probably need additional tables to represent these
     relations.
    """
    __tablename__ = "schemeconditions"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    value = DB.Column(DB.String, unique=True, nullable=False)
    priority = DB.Column(DB.Integer, nullable=False)
    start_time = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    end_time = DB.Column(DB.DateTime, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return "<SchemeCondition %r>" % self.id
