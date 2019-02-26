from flask import session
from passlib.handlers.bcrypt import bcrypt_sha256

from timeless.employees.models import Employee

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
    if user is None or not verify(password, user.password):
        error = "login.failed"
    if error is None:
        session.clear()
        session["user_id"] = user.id
    return error


def forgot_password(email=""):
    user = Employee.query.filter_by(email=email).first()
    error = None
    if user is None:
        error = "failed"
    if error is None:
        session.clear()
    return error


def verify(password, hash):
    """
    Verifies password against hash
    :param password: Password to check
    :param hash: Hash to check password against
    :return: True in case of successful password verification
    """
    return bcrypt_sha256.verify(password, hash)


def hash(password):
    """
    Hash password
    :param password: Password to hash
    :return: Hashed password
    """
    return bcrypt_sha256.hash(password)
