""" Views module for Items.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint("items", __name__, url_prefix="/items")

@bp.route("/")
def list_items():
    flash("Create not yet implemented")
    #return render_template("items/list", items=items)

@bp.route("/create", methods=("GET", "POST"))
def create():
    flash("Create not yet implemented")
    #return render_template("items/create.html")

@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    flash("Edit not yet implemented")
    #return render_template("items/edit.html")
  
@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("items.list_items"))
