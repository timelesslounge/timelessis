"""
Auth views module.
"""
from functools import wraps
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from timeless.auth import auth
from timeless.employees.models import Employee

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if not user_id:
        g.user = None
    else:
        g.user = Employee.query.get(user_id)


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.login"))
        return view(**kwargs)

    return wrapped_view


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        error = auth.login(
            username=request.form["username"],
            password=request.form["password"])
        if error is not None:
            return redirect(url_for("auth.login"))

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main"))


@bp.route("/forgotpassword", methods=("GET", "POST"))
def forgot_password():
    if request.method == "POST":
        email = request.form["email"]
        error = auth.forgot_password(email=email)

        if error:
            template = render_template(
                "auth/forgot_password.html", error=error)
        else:
            template = render_template(
                "auth/forgot_password_post.html", email=auth.mask_email(email))

        return template

    return render_template("auth/forgot_password.html")


@bp.route("/activate", methods=["POST"])
def activate():
    """
    Activate the user's account by setting account status to true.
    @todo #399:30min Implement tests for this method.
     Tests should include more cases.
     Currently we are testing not logged in while visiting activate.
     Tests for a logged in activation needed.
    """
    if not g.user:
        return render_template("auth/activate.html")

    g.user.account_status = True
    session.commit()
    return render_template(
        "auth/activate.html",
        message="Successfully activated your account."
    )
