from timeless.views import ListView, CreateView
from timeless.items.forms import ItemForm
from timeless.items.models import Item
""" Views module for Items.
    @todo #270:30min Continue implementation of views class using GenericViews.
     Use mocks from mock_items to make the tests, like tests for item list. Add
     the methods to ItemQuery as needed for the tests. Add
     authenticationannotation. Also, templates should be finished.
"""
from flask import (
    Blueprint, redirect, render_template, url_for
)

BP = Blueprint("items", __name__, url_prefix="/items")


class ItemListView(ListView):
    """ List the Items """
    model = Item
    template_name = "items/list.html"


ItemListView.register(BP, "/")


class ItemCreateView(CreateView):
    """ Create a new Item """
    model = Item
    template_name = "items/create.html"
    success_view_name = "item.list"
    form_class = ItemForm


ItemCreateView.register(BP, "/create")


@BP.route("/edit", methods=("GET", "POST"))
def edit():
    """ Edit an item by id """
    return render_template("items/edit.html")


@BP.route("/delete", methods=["POST"])
def delete():
    """ Delete an item by id """
    return redirect(url_for("items.item_list_view"))
