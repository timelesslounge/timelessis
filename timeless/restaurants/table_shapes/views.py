"""Floors views module.
@todo #72:30min Continue implementing list(), create(), edit() and
 delete() methods, using SQLAlchemy and TableShape model. In the index page it
 should be possible to sort and filter for every column. Table shape management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for all methods.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint("table_shape", __name__, url_prefix="/table_shapes")


@bp.route("/")
def list():
    """ List all table shapes"""
    table_shapes = [{
        "id": 1,
        "description": "This is a test",
        "picture": "shape.png"
        }]
    return render_template(
        "restaurants/table_shapes/list.html", table_shapes=table_shapes
    )


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    if request.method == "POST":
        flash("Create not yet implemented")
    action = 'create'
    return render_template(
        "restaurants/table_shapes/create_edit.html",
        action=action
        )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """ Edit table shape with id """
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = 'edit'
    return render_template(
        "restaurants/table_shapes/create_edit.html",
        action=action
        )


@bp.route("/delete", methods=["POST"])
def delete():
    """ Delete table shape with id """
    flash("Delete not yet implemented")
    return redirect(url_for("table_shape.list"))
