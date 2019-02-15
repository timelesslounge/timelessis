"""File for models in reservations module"""
from timeless.models import TimestampsMixin, validate_required
from timeless import DB


class Comment(TimestampsMixin, DB.Model):
    """Model for comment business entity"""
    __tablename__ = "comments"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    employee_id = DB.Column(DB.Integer, DB.ForeignKey("employees.id"))
    body = DB.Column(DB.String, nullable=False)
    date = DB.Column(DB.DateTime, nullable=False)
    employee = DB.Column(DB.Integer, DB.ForeignKey("employees.id"))

    @validate_required("body", "date")

    def __repr__(self):
        return "<Comment %r>" % self.description


class ReservationSettings(TimestampsMixin, DB.Model):
    """Settings model for Reservations"""

    __tablename__ = "reservation_settings"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String, unique=True)
    default_duration = DB.Column(DB.SmallInteger)
    default_deposit = DB.Column(DB.SmallInteger)
    sms_notifications = DB.Column(DB.Boolean)
    threshold_sms_time = DB.Column(DB.SmallInteger)
    greeting_by_time = DB.Column(DB.JSON)
    sex = DB.Column(DB.String)
