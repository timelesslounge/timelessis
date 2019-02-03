"""File for models in employees module"""
from datetime import datetime

from timeless.db import DB
from timeless.reservations.models import Comment


class Employee(DB.Model):
    """Model for employee business entity.
    @todo #4:30min Continue implementation. Employees should have its own
     management pages to list, create, edit and delete them. In the index page
     it should be possible to sort and filter for every column. Other possible
     actions are described in more detail in issue #4. Specific details about
     Employee default values are in another puzzle.
    @todo #4:30min Create constructor for Employee model. Default
     values for these variables should be set: registration_date, account_status
     user_status, created_on and password. Password is special and it should be
     hashed and salted - one can use bcrypt_sha256.hash() function. See more at:
     https://pythonhosted.org/passlib/lib/passlib.hash.bcrypt_sha256.html
     Also create a method to validate the password, using:
     bcrypt_sha256.verify("password", h)
    """
    __tablename__ = "employees"

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    first_name = DB.Column(DB.String, nullable=False)
    last_name = DB.Column(DB.String, nullable=False)
    username = DB.Column(DB.String(15), unique=True, nullable=False)
    phone_number = DB.Column(DB.String, nullable=False)
    birth_date = DB.Column(DB.Date(), nullable=False)
    registration_date = DB.Column(DB.DateTime(), nullable=False)
    account_status = DB.Column(DB.String, nullable=False)
    user_status = DB.Column(DB.String, nullable=False)
    email = DB.Column(DB.String(300), nullable=False)
    password = DB.Column(DB.String(300), nullable=False)
    pin_code = DB.Column(DB.Integer, unique=True, nullable=False)
    comment = DB.Column(DB.String)
    company_id = DB.Column(DB.Integer, DB.ForeignKey("companies.id"))
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow, nullable=False)
    updated_on = DB.Column(DB.DateTime, onupdate=datetime.utcnow)

    company = DB.relationship("Company", back_populates="employees")

    def __repr__(self):
        return "<Employee(username=%s)>" % self.username
