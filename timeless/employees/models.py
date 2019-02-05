"""File for models in employees module"""
from datetime import datetime
from passlib.hash import bcrypt_sha256
from timeless.db import DB
from timeless.models import TimestampsMixin


class Employee(TimestampsMixin, DB.Model):
    """Model for employee business entity.
    @todo #4:30min Continue implementation. Employees should have its own
     management pages to list, create, edit and delete them. In the index page
     it should be possible to sort and filter for every column. Other possible
     actions are described in more detail in issue #4. Specific details about
     Employee default values are in another puzzle.
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

    company = DB.relationship("Company", back_populates="employees")

    def __init__(self, username, password, first_name, last_name, phone_number,
                 birth_date, pin_code, email, comment=""):
        super().__init__()
        self.username = username
        self.password = bcrypt_sha256.hash(password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.pin_code = pin_code
        self.email = email
        self.registration_date = datetime.utcnow()
        self.account_status = "Not Activated"
        self.user_status = "Working"
        self.created_on = datetime.utcnow()
        self.comment = comment

    def __repr__(self):
        return "<Employee(username=%s)>" % self.username

    def validate_password(self, password):
        """ Validate user password """
        return bcrypt_sha256.verify(password, self.password)
