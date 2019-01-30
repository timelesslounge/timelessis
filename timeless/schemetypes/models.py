from timeless.db import DB
from datetime import datetime


class SchemeCondition(DB.Model):
    """
    @todo #18:30min Continue implementation as in #18. Weekdays, months and dates
     still need to be added -- we'll probably need additional tables to represent these
     relations.
    """
    __tablename__ = "scheme_conditions"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    scheme_type_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))

    value = DB.Column(DB.String, unique=True, nullable=False)
    priority = DB.Column(DB.Integer, nullable=False)
    start_time = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    end_time = DB.Column(DB.DateTime, nullable=False)

    scheme_type = DB.relationship("SchemeType", back_populates="conditions")

    def __repr__(self):
        return "<SchemeCondition %r>" % self.id


class SchemeType(DB.Model):
    """
    @todo #17:30min Continue implementation as in #17. SchemeType should have
     its own management pages to list, create, edit and delete them. In the
     index page it should be possible to sort and filter for every column.
    """
    __tablename__ = "scheme_types"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, unique=True, nullable=False)
    default_value = DB.Column(DB.String, nullable=False)
    value_type = DB.Column(DB.String, nullable=False)
    conditions = DB.relationship("SchemeCondition", order_by=SchemeCondition.id, back_populates="scheme_type")

    def __repr__(self):
        return "<SchemeType %r>" % self.id
