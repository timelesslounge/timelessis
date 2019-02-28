""" Authentication methods are implemented here. """
import random
import string

from flask import session
from passlib.hash import bcrypt_sha256
from timeless.employees.models import Employee
from timeless.mail import MAIL
from flask_mail import Message

PASS_LENGTH = 8
"""
    @todo #370:30min Decouple routines from database. Database
     implementation and routines are tightly coupled, which prevents
     unit testing. Decouple Employee model from routines creating Employee and
     Employees abstractions (see
     https://github.com/timelesslounge/timelessis/pull/375) for examples.
     Then create mocks and use these mocks to test auth.
"""
def login(username="", password=""):
    """Login user

    """
    user = Employee.query.filter_by(username=username).first()
    error = None
    if user is None or not user.validate_password(password):
        error = "login.failed"
    if error is None:
        session.clear()
        session["user_id"] = user.id
    return error


def forgot_password(email=""):
    """ Handle the forgot password routine. """
    user = Employee.query.filter_by(email=email).first()
    error = None
    if not user:
        error = "failed"
    if not error:
        password = "".join(random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(PASS_LENGTH))
        user.password = bcrypt_sha256.hash(password)
        session.commit()
        MAIL.send(
            Message(
                f"Hello! your new password is {password}, please change it!",
                recipients=[email]
            )
        )
        session.clear()
    return error
