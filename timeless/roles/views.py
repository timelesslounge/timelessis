"""roles views module.
@todo #192:30min Continue implementing edit() and
 delete() methods, using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for all methods.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless.roles.forms import RoleForm
from timeless.roles.models import Role

bp = Blueprint("role", __name__, url_prefix="/roles")


@bp.route("/", methods=["GET"])
def list_roles():
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
    if request.method == "POST":
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


@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("role.list_roles"))
