"""TableShape views module.
 @todo #162:30min Update html templates when all
 methods are implemented.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless.db import DB
from timeless.restaurants import models
from timeless.restaurants.table_shapes import forms


bp = Blueprint("table_shape", __name__, url_prefix="/table_shapes")


@bp.route("/")
def list():
    """ List all table shapes"""
    """
    @todo #162:30min Implement ordering and sorting of TableShape model for
    all columns. Do not forget write tests.
    """
    return render_template(
        "restaurants/table_shapes/list.html",
        table_shapes=models.TableShape.query.all())


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    form = forms.TableShapeForm(request.form)

    if request.method == 'POST' and form.validate():
        table_shape = models.TableShape()
        form.populate_obj(table_shape)

        DB.session.add(table_shape)
        DB.session.commit()

        return redirect(url_for('table_shape.list'))
    return render_template(
        "restaurants/table_shapes/create_edit.html", form=form)


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """ Edit table shape with id """
    """
    @todo #162:30min Implement edit() method of TableShape model and
    update template. Do not forget write tests.
    """
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = "edit"
    return render_template(
        "restaurants/table_shapes/create_edit.html",
        action=action
        )


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete table shape with id """
    table_shape = models.TableShape.query.get(id)
    DB.session.delete(table_shape)
    return redirect(url_for("table_shape.list"))
