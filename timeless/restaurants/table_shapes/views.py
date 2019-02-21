"""TableShape views module."""
from http import HTTPStatus

from flask import (
    Blueprint, redirect, abort, render_template, request, url_for
)

from timeless.db import DB
from timeless.restaurants import models
from timeless.restaurants.table_shapes import forms
from timeless.templates.views import order_by, filter_by

bp = Blueprint("table_shape", __name__, url_prefix="/table_shapes")


@bp.route("/")
def list():
    """List all table shapes
    @todo #260:30min Implement filtering of table shapes from the UI. It
     should be possible to filter for every column from the UI. Currently
     it is possible to filter using browser address bar only.
    """
    order_fields = request.args.getlist("order_by")
    filter_fields = request.args.getlist("filter_by")
    query = models.TableShape.query
    if order_fields:
        query = order_by(query, order_fields)
    if filter_fields:
        query = filter_by(query, filter_fields)
    return render_template(
        "restaurants/table_shapes/list.html",
        table_shapes=query.all())


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new table shape"""
    form = forms.TableShapeForm(request.form)

    if request.method == "POST" and form.validate():
        """
        @todo #162:30min This form currenly cannot save pictures. Need have a
         look how WTF form processes files. Implement generic solution to use
         it everywhere when it's needed.
        Uncomment after correction
        form.save()
        """
        return redirect(url_for("table_shape.list"))
    return render_template(
        "restaurants/table_shapes/create_edit.html", form=form)


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    """Edit table shape with id"""
    table = models.TableShape.query.get(id)
    if not table:
        return abort(HTTPStatus.NOT_FOUND)

    if request.method == "POST":
        form = forms.TableShapeForm(request.form, instance=table)
        if not form.validate():
            return abort(HTTPStatus.BAD_REQUEST)

        form.save()
        return redirect(url_for("table_shape.list"))

    form = forms.TableShapeForm(instance=table)
    return render_template(
        "restaurants/table_shapes/create_edit.html", form=form
    )


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete table shape with id """
    table_shape = models.TableShape.query.get(id)
    DB.session.delete(table_shape)
    DB.session.commit()
    return redirect(url_for("table_shape.list"))
