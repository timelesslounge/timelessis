"""Auth views module.
@todo #5:30min Continue implementing login(), forgot_password() and activate()
 methods, once Employee model is available. Fetch the user using Employee model
 and check password hash using Employee.validate_password method. Update html
 templates when methods are implemented. Create more tests for all methods.
"""
from functools import wraps
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from timeless.employees.models import Employee

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = Employee.query.get(user_id)


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        # fetch user using DB and Employee model
        # check that password hash matches
        # if user is None
        #     error = "Incorrect username."
        # elif not user.validate_password(password):
        #      error = "Incorrect password."
        # if error is None:
        #     session.clear()
        #     session["user_id"] = user[id]
        #     return redirect(url_for("index"))
        flash("Login not yet implemented")

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
