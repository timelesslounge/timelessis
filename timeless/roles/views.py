"""roles views module.
@todo #95:30min Continue implementing list(), create(), edit() and
 delete() methods, using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for all methods.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)


bp = Blueprint("role", __name__, url_prefix="/roles")


@bp.route("/")
def list_roles():
    # remove this dummy roles object and use db
    roles = [{
        "id": 1,
        "name": "Intern",
        "works_on_shifts": True,
        "company_id": 3
        }]
    companies = {
        1: "Foo Inc.",
        3: "Foomatic Co.",
    }
    return render_template("roles/list.html", roles=roles, companies=companies)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        flash("Create not yet implemented")
    action = "create"
    companies = [
        {"id": 1, "name": "Foo Inc.", "selected": False},
        {"id": 3, "name": "Foomatic Co.", "selected": True},
    ]
    return render_template(
        "roles/create_edit.html", action=action,
        companies=companies
    )


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
