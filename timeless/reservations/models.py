"""File for models in reservations module"""
from timeless import DB
from datetime import datetime


class Comment(DB.Model):
    """Model for comment business entity
    @todo #26:30min Continue implementation. Comments should have its own management pages to
     list, create, edit and delete them. In the index page it should
     be possible to sort and filter for every column.
    """
    __tablename__ = 'comments'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    employee_id = DB.Column(DB.Integer, DB.ForeignKey('employees.id'))
    body = DB.Column(DB.String, nullable=False)
    date = DB.Column(DB.DateTime, nullable=False)
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)
    employee = DB.Column(DB.Integer, DB.ForeignKey('employees.id'))

    def __repr__(self):
        return "<Comment %r>" % self.description


class ReservationSettings(DB.Model):
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
    created_on = DB.Column(
        DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)
