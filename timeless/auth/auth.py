from flask import session
from timeless.employees.models import Employee


def login(username="", password=""):
    """Login user
    @todo #201:30min Translate login error codes.
      The codes returned from login errors should then be translated into (
      mapped to) Strings on the UI, so we can easily have
      internationalization or change error messages without having to
      rebuild + redeploy the backend.
    """
    user = Employee.query.filter_by(username=username).first()
    error = None
    if user is None or not user.validate_password(password):
        error = "login.failed"
    if error is None:
        session.clear()
        session["user_id"] = user.id
    return error

