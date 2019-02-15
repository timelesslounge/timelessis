from flask import session
from timeless.employees.models import Employee


def login(username="", password=""):
    """Login user
    @todo #59:30min The backend should return only error codes for login
     procedure, not hardcoded messages. The codes should then be translated
     into (mapped to) Strings on the UI, so we can easily have
     internationalization or change error messages without having to
     rebuild + redeploy the backend.
    """
    user = Employee.query.filter_by(username=username).first()
    error = None
    if user is None:
        error = "Incorrect username."
    elif not user.validate_password(password):
        error = "Incorrect password."
    if error is None:
        session.clear()
        session["user_id"] = user.id
    return error
