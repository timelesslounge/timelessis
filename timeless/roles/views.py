"""
@todo #338:30min Continue to implement html templates using html mockups and
 use generic views for list / create routes. See `templates/_formhelpers.html`,
 it helps to render inputs in templates correctly.
"""
from http import HTTPStatus

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for,
    abort)

from timeless import views
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


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """
    Role delete route
    :param id: Role id
    :return: List roles view
    """
    roles = Role.query.get(id)
    if not roles:
        return abort(HTTPStatus.NOT_FOUND)
    Role.query.filter_by(id=id).delete()
    return redirect(url_for("role.list_roles"))


class Edit(views.UpdateView):
    """ Base class for updating roles. """
    model = Role
    form_class = RoleForm
    template_name = "roles/create_edit.html"
    success_view_name = "role.list_roles"


Edit.register(bp, "/edit/<int:id>")
