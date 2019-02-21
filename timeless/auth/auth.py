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


"""
@todo #340:30min Continue implementing forgot_password. End the function that
 will be responsible for sending the email with the link to reset the password.
"""
def forgot_password(email=""):
    user = Employee.query.filter_by(email=email).first()
    error = None
    if user is None:
        error = "failed"
    if error is None:
        session.clear()
    return error
