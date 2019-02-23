from datetime import datetime
from timeless import DB
from timeless.models import validate_required


class WeekDay(DB.Model):
    """ WeekDay model"""
    __tablename__ = "weekdays"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    weekday = DB.Column(DB.Integer, unique=True, nullable=False)
    scheme_condition_id = DB.Column(
        DB.Integer,
        DB.ForeignKey("scheme_conditions.id")
        )

    scheme_condition = DB.relationship(
        "SchemeCondition",
        back_populates="weekdays"
        )

    @validate_required("weekday")
    def __init__(self, **kwargs):
        super(WeekDay, self).__init__(**kwargs)

    def __repr__(self):
        return "<Weekday %r>" % self.id


class MonthDay(DB.Model):
    __tablename__ = "monthdays"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    monthday = DB.Column(DB.Integer, unique=True, nullable=False)
    scheme_condition_id = DB.Column(
        DB.Integer,
        DB.ForeignKey("scheme_conditions.id")
        )

    scheme_condition = DB.relationship(
        "SchemeCondition",
        back_populates="monthdays"
        )

    @validate_required("monthday")
    def __init__(self, **kwargs):
        super(MonthDay, self).__init__(**kwargs)

    def __repr__(self):
        return "<MonthDay %r>" % self.id


class Date(DB.Model):
    __tablename__ = "dates"
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    date = DB.Column(DB.DateTime, unique=True, nullable=False)
    scheme_condition_id = DB.Column(
        DB.Integer,
        DB.ForeignKey("scheme_conditions.id")
        )

    scheme_condition = DB.relationship(
        "SchemeCondition",
        back_populates="dates"
        )

    @validate_required("date")
    def __init__(self, **kwargs):
        super(Date, self).__init__(**kwargs)

    def __repr__(self):
        return "<Date %r>" % self.id


class SchemeCondition(DB.Model):
    __tablename__ = "scheme_conditions"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    scheme_type_id = DB.Column(DB.Integer, DB.ForeignKey("scheme_types.id"))

    value = DB.Column(DB.String, unique=True, nullable=False)
    priority = DB.Column(DB.Integer, nullable=False)
    start_time = DB.Column(
        DB.DateTime,
        default=datetime.utcnow,
        nullable=False
        )
    end_time = DB.Column(DB.DateTime, nullable=False)
    weekdays = DB.relationship(
        "WeekDay",
        order_by=WeekDay.id,
        back_populates="scheme_condition"
        )
    monthdays = DB.relationship(
        "MonthDay",
        order_by=MonthDay.id,
        back_populates="scheme_condition"
        )
    dates = DB.relationship(
        "Date",
        order_by=Date.id,
        back_populates="scheme_condition"
        )

    scheme_type = DB.relationship("SchemeType", back_populates="conditions")

    @validate_required("value", "priority", "start_time", "end_time")
    def __init__(self, **kwargs):
        super(SchemeCondition, self).__init__(**kwargs)

    def __repr__(self):
        return "<SchemeCondition %r>" % self.id


class SchemeType(DB.Model):
    __tablename__ = "scheme_types"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    description = DB.Column(DB.String, unique=True, nullable=False)
    default_value = DB.Column(DB.String, nullable=False)
    value_type = DB.Column(DB.String, nullable=False)
    conditions = DB.relationship(
        "SchemeCondition",
        order_by=SchemeCondition.id,
        back_populates="scheme_type"
        )

    @validate_required("description", "default_value", "value_type")
    def __init__(self, **kwargs):
        super(SchemeType, self).__init__(**kwargs)

    def __repr__(self):
        return "<SchemeType %r>" % self.id
