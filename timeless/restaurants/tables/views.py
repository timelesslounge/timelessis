"""tables views module.
@todo #169:30min Continue implementing list_tables(), create(), edit() and
 methods, using SQLAlchemy and Location model. In the index page it
 should be possible to sort and filter for every column. Location management
 page should be accessed by the Location page. Update html templates when
 methods are implemented. Create more tests for all methods.
 Table management pages should be accessed by the Location and Floor pages.
@todo #112:30min Modify this file and also all other views.py files so the
 endpoints are registered inside timeless/__init__.py file in register_api
 method. Just like it was done for companies management views.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless import DB
from timeless.restaurants import models
from timeless.restaurants.tables import forms


bp = Blueprint("table", __name__, url_prefix="/tables")


@bp.route("/")
def list_tables():
    """ Returns list of tables """
    # remove this dummy tables object and use db
    floors = {
        1: "Test location",
        2: "Second floor location",
    }
    shapes = {
        1: "Square",
        3: "Triangle",
    }
    return render_template(
        "restaurants/tables/list.html", tables=models.Table.query.all(),
        floors=floors, shapes=shapes
    )


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table """
    form = forms.TableForm(request.form)
    if request.method == "POST" and form.validate():
        print("FORM", form.data)
        form.save()
        return redirect(url_for("tables.list_tables"))
    return render_template(
        "restaurants/tables/create_edit.html", form=form)


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """ Edit existing table """
    table = models.Table.query.get(id)
    if not table:
        return redirect(url_for("tables.list"))

    form = forms.TableForm(request.form, instance=table)
    if request.method == "POST" and form.validate():
        form.save()
        return redirect(url_for("tables.list_tables"))

    return render_template(
        "restaurants/tables/create_edit.html", form=form)


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete table shape with id """
    table = models.Table.query.get(id)
    if table:
        DB.session.delete(table)
        DB.session.commit()
    return redirect(url_for("table.list_tables"))
