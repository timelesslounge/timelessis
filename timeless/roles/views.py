"""roles views module.
@todo #255:30min Continue implementing edit() method,
 using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for edit() route.
 Remember not to use DB layer directly. Please refer to
 timeless/companies/views.py as an example on how routes
 should be implemented.
"""
from http import HTTPStatus

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for,
    abort)

from timeless import DB
from timeless.roles.forms import RoleForm
from timeless.roles.models import Role

bp = Blueprint("role", __name__, url_prefix="/roles")


@bp.route("/", methods=["GET"])
def list_roles():
    """List roles route"""
    return render_template("roles/list.html", roles=Role.query.all())


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    form = RoleForm(request.form)
    if request.method == "POST" and form.validate():
        form.save()
        return redirect(url_for("role.list_roles"))
    return render_template(
        "roles/create_edit.html", form=form)


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """
    Role edit route
    :param id: Role id
    :return: Current role edit view
    """
    if request.method == "POST":
        table = Role.query.get(id)
        if not table:
            return abort(HTTPStatus.NOT_FOUND)
        flash("Edit not yet implemented")
    action = "edit"
    companies = [
        {"id": 1, "name": "Foo Inc.", "selected": False},
        {"id": 3, "name": "Foomatic Co.", "selected": True},
    ]
    return render_template(
        "roles/create_edit.html", action=action,
        companies=companies
    )


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """
    @todo #255:30min Get rid of DB usage from the view.
     Please refer to timeless/companies/views.py
     file to see how it should be implemented
    """
    roles = Role.query.get(id)
    if not roles:
        return abort(HTTPStatus.NOT_FOUND)
    roles = Role.query.get(id)
    DB.session.delete(roles)
    DB.session.commit()
    return redirect(url_for("role.list_roles"))
