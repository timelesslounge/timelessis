from flask import session
from timeless.employees.models import Employee


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

