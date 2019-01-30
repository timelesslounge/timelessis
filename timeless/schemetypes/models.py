from timeless.db import DB
from datetime import datetime

class WeekDay(DB.Model):
    __tablename__ = "weekdays"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    weekday = DB.Column(DB.Integer, unique=True, nullable=False)
    scheme_condition_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_conditions.id"))

    scheme_condition = DB.relationship("SchemeCondition", back_populates="weekdays")

    def __repr__(self):
        return "<Weekday %r>" % self.id

class MonthDay(DB.Model):
    __tablename__ = "monthdays"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    monthday = DB.Column(DB.Integer, unique=True, nullable=False)
    scheme_condition_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_conditions.id"))

    scheme_condition = DB.relationship("SchemeCondition", back_populates="monthdays")

    def __repr__(self):
        return "<MonthDay %r>" % self.id     

class Date(DB.Model):
    __tablename__ = "dates"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    date = DB.Column(DB.DateTime, unique=True, nullable=False)
    scheme_condition_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_conditions.id"))

    scheme_condition = DB.relationship("SchemeCondition", back_populates="dates")

    def __repr__(self):
        return "<Date %r>" % self.id        

class SchemeCondition(DB.Model):
    __tablename__ = "scheme_conditions"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    scheme_type_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))

    value = DB.Column(DB.String, unique=True, nullable=False)
    priority = DB.Column(DB.Integer, nullable=False)
    start_time = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    end_time = DB.Column(DB.DateTime, nullable=False)
    weekdays = DB.relationship("WeekDay", order_by=WeekDay.id, back_populates="scheme_condition")
    monthdays = DB.relationship("MonthDay", order_by=MonthDay.id, back_populates="scheme_condition")
    dates = DB.relationship("Date", order_by=Date.id, back_populates="scheme_condition")

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
