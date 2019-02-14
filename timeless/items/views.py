""" Views module for Items.
    @todo Continue implementation of views class.
     Use the database to get the data instead of dummy data.
     Also, templates should be finished.
"""
from flask import (
    Blueprint, redirect, render_template, url_for
)

BP = Blueprint("items", __name__, url_prefix="/items")

@BP.route("/")
def list_items():
    """ List the items """
    items = [{"id":1}, {"id":2}]
    return render_template("items/list.html", items=items)

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
