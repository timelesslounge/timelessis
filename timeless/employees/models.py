"""File for models in employees module"""
from passlib.hash import bcrypt_sha256

from timeless.db import DB
from timeless.models import TimestampsMixin, validate_required


class Employee(TimestampsMixin, DB.Model):
    """Model for employee business entity."""
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

    company = DB.relationship("Company", back_populates="employees")
    items = DB.relationship("Item", back_populates="empolyee")
    history = DB.relationship("ItemHistory", back_populates="employee")

    @validate_required("username", "password", "first_name", "last_name",
                       "phone_number", "birth_date", "email", "pin_code",
                       "registration_date", "account_status", "user_status")
    def __init__(self, **kwargs):
        super(Employee, self).__init__(**kwargs)

    def __repr__(self):
        return "<Employee(username=%s)>" % self.username

    def validate_password(self, password):
        """ Validate user password """
        return bcrypt_sha256.verify(password, self.password)
