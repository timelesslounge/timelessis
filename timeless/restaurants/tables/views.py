"""tables views module.
@todo #112:30min Continue implementing list_tables(), create(), edit() and
 delete() methods, using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for all methods.
 Table management pages should be accessed by the Location and Floor pages.
@todo #112:30min Modify this file and also all other views.py files so the
 endpoints are registered inside timeless/__init__.py file in register_api
 method. Just like it was done for companies management views.
"""
import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)


bp = Blueprint("table", __name__, url_prefix="/tables")


@bp.route("/")
def list_tables():
    # remove this dummy tables object and use db
    tables = [{
        "id": 1,
        "name": "Test table",
        "description": "This is a test",
        "floor_id": 1,
        "x": 10,
        "y": 20,
        "width": 12,
        "height": 22,
        "status": 1,
        "max_capacity": 6,
        "multiple": True,
        "playstation": False,
        "shape_id": 3,
        "min_capacity": 4,
        "deposit_hour": 3,
        "created": datetime.datetime.now(),
        "updated": datetime.datetime.now(),
        }]
    floors = {
        1: "Test location",
        2: "Second floor location",
    }
    shapes = {
        1: "Square",
        3: "Triangle",
    }
    return render_template(
        "restaurants/tables/list.html", tables=tables, floors=floors,
        shapes=shapes
    )


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        flash("Create not yet implemented")
    floors = [
        {"id": 1, "name": "First location", "selected": True},
        {"id": 2, "name": "Second location", "selected": False},
    ]
    shapes = [
        {"id": 1, "name": "Rectangle", "selected": True},
        {"id": 2, "name": "Triangle", "selected": False},
    ]
    return render_template(
        "restaurants/tables/create_edit.html", action="create",
        floors=floors, shapes=shapes
    )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    floors = [
        {"id": 1, "name": "First location", "selected": True},
        {"id": 2, "name": "Second location", "selected": False},
    ]
    shapes = [
        {"id": 1, "name": "Rectangle", "selected": False},
        {"id": 2, "name": "Triangle", "selected": True},
    ]
    return render_template(
        "restaurants/tables/create_edit.html", action="edit",
        floors=floors, shapes=shapes
    )


@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("table.list"))
