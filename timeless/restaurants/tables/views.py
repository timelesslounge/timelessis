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
@todo #309:30min Add mock authentication to TableListView. Currently
 TabeListView test is not working because it requires an authenticated user
 with permissions to show list tables. it is currently showing login screen.
 Add an mocked authenticated user so we can run the test, the remove skip
 annotation from it.
"""
from flask import (
    Blueprint, redirect, render_template, request, url_for
)

from timeless import DB, views
from timeless.restaurants import models
from timeless.restaurants.models import Table
from timeless.restaurants.tables import forms


BP = Blueprint("table", __name__, url_prefix="/tables")


class TableListView(views.ListView):
    """ List the tables """
    model = Table
    template_name = "restaurants/tables/list.html"


TableListView.register(BP, "/")

"""
@bp.route("/")
def list_tables():

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
"""


@BP.route("/edit/<int:id>", methods=("GET", "POST"))
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


@BP.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete table shape with id """
    table = models.Table.query.get(id)
    if table:
        DB.session.delete(table)
        DB.session.commit()
    return redirect(url_for("table.list_tables"))


class Create(views.CreateView):
    form_class = forms.TableForm
    success_view_name = "table.list_tables"
    template_name = "restaurants/tables/create_edit.html"


Create.register(BP, "/create")
