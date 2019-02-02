"""Floors views module.
@todo #42:30min Continue implementing list_floors(), create(), edit() and
 delete() methods, using SQLAlchemy and Floor model. In the index page it
 should be possible to sort and filter for every column. Floor management page
 should be accessed by the Location page. Update html templates when methods
 are implemented. Create more tests for all methods.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint("floor", __name__, url_prefix="/floors")


@bp.route("/")
def list_floors():
    """ List all floors """
    # remove this dummy floors object and use db
    floors = [{
        "id": 1,
        "location": "Test location",
        "description": "This is a test"
        }]
    return render_template("restaurants/floors/list.html", floors=floors)


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new floor """
    if request.method == "POST":
        flash("Create not yet implemented")
    action = 'create'
    return render_template(
        "restaurants/floors/create_edit.html",
        action=action
        )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """ Edit floor with id """
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = 'edit'
    return render_template(
        "restaurants/floors/create_edit.html",
        action=action
        )


@bp.route("/delete", methods=["POST"])
def delete():
    """ Delete floor with id """
    flash("Delete not yet implemented")
    return redirect(url_for("floor.list_floors"))
