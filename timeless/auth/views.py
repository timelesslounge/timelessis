"""Auth views module.
@todo #5:30min Continue implementing login(), forgot_password() and activate()
 methods, once Employee model is available. Fetch the user using Employee model
 and check password hash using Employee.validate_password method. Update html
 templates when methods are implemented. Create more tests for all methods.
@todo #5:30min Implement before_app_request function that will get the user id
 from session, get user data from db and store it in g.user, which lasts for the
 length of the request. Also, create a decorator that will check, for each view
 if g.user exists and if not, redirect user to login page.
"""
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("auth", __name__, url_prefix="/auth")


from timeless.employees.models import Employee

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Employee.query.filter_by(username=username).first()
        error = None
        if user is None:
            error = "Incorrect username."
        elif not user.validate_password(password):
            error = "Incorrect password."
        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("index"))

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main"))


@bp.route("/forgotpassword", methods=("GET", "POST"))
def forgot_password():
    if request.method == "POST":
        # send user link for password reset
        flash("Forgot password not yet implemented")
    return render_template("auth/forgot_password.html")


@bp.route("/activate", methods=["POST"])
def activate():
    flash("Activate link is not yet implemented")
    return render_template("auth/activate.html")
