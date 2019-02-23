from timeless.views import ListView
from timeless.items.models import Item
""" Views module for Items.
    @todo #270:30min Continue implementation of views class using GenericViews.
     Use mocks from mock_items to make the tests, like tests for item list.
     Add authenticationannotation. Also, templates should be finished.
"""
from flask import (
    Blueprint, redirect, render_template, url_for
)

BP = Blueprint("items", __name__, url_prefix="/items")


class ItemListView(ListView):
    """ List the Items """
    model = None
    template_name = "items/list.html"
    items = None

    def __int__(self, **kwargs):
        items=kwargs.get("items")
        item=kwargs.get("item")
        self.register(
            Blueprint("items", __name__, url_prefix="/items"),
            "/"
        )

    def list_items(self):
        """ List the items """
        items = [{"id": 1}, {"id": 2}]
        return render_template("items/list.html", items=self.items)


@BP.route("/create", methods=("GET", "POST"))
def create():
    """ Create new item """
    return render_template("items/create.html")


@BP.route("/edit", methods=("GET", "POST"))
def edit():
    """ Edit an item by id """
    return render_template("items/edit.html")


@BP.route("/delete", methods=["POST"])
def delete():
    """ Delete an item by id """
    return redirect(url_for("items.list_items"))
