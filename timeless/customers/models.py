"""File for models in customer module"""
from datetime import datetime
from timeless import DB
from timeless.poster.models import PosterSyncMixin
from timeless.models import validate_required


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

    @classmethod
    def merge_with_poster(cls, customer: "Customer", poster_customer: dict):
        """
        Method should return Customer object with merged data from table entity
        and poster customer dict
        """
        return Customer(
            id=customer.id,
            first_name=customer.first_name,
            last_name=customer.last_name,
            phone_number=poster_customer["phone_number"],
            created_on=poster_customer["date_activate"],
            updated_on=datetime.utcnow(),
            poster_id=poster_customer["client_id"],
            synchronized_on=datetime.utcnow()
        )

    @classmethod
    def create_by_poster(cls, poster_customer: dict):
        """
        Method should return Customer object with given data from
        poster_customer dict
        """
        return Customer(
            first_name=poster_customer["firstname"],
            last_name=poster_customer["lastname"],
            phone_number=poster_customer["phone_number"],
            created_on=poster_customer["date_activate"],
            updated_on=datetime.utcnow(),
            poster_id=poster_customer["client_id"],
            synchronized_on=datetime.utcnow()
        )
