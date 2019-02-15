"""File for models in customer module"""
from datetime import datetime
from timeless import DB
from timeless.poster.models import PosterSyncMixin


class Customer(PosterSyncMixin, DB.Model):
    """Model for customer business entity.

    """
    __tablename__ = "customers"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    first_name = DB.Column(DB.String, nullable=False)
    last_name = DB.Column(DB.String, nullable=False)
    phone_number = DB.Column(DB.String, nullable=False)
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<Customer(name=%s %s)>" % (self.first_name, self.last_name)
