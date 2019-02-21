"""Locations views module.
@todo #208:30min Remove function endpoints once the view classes are in place.
 See #173 for more details about generic views use CreateView, EditView and
 DeleteView as provided in the commented code templates. Uncomment and modify
 this code - create missing view templates and write ITs to verify behaviour.
@todo #208:30min Continue implementing List to enable sorting and filtering
 for every column. For this, probably there will be a need to create a new
 generic view that all other List views will extend. This generic view should
 use GenericFilter implemented in #317.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless.views import ListView
from timeless.restaurants.models import Location

bp = Blueprint("location", __name__, url_prefix="/locations")


# class Create(CreateView):
#     """Create location"""
#     template_name = "restaurants/locations/create_edit.html"
#     form_class  = LocationForm
#     model = Location
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        flash("Create not yet implemented")
    action = "create"
    return render_template("restaurants/locations/create_edit.html",
                           action=action)


# class Edit(UpdateView):
#     """Update location"""
#     template_name = "restaurants/locations/create_edit.html"
#     form_class  = LocationForm
#     model = Location
@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = "edit"
    return render_template("restaurants/locations/create_edit.html",
                           action=action)


# class Delete(DeleteView):
#     """Delete location
#     Deletes location using id and redirects to list page
#     """
#     form_class  = LocationForm
#     model = Location
@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("location.list"))


class List(ListView):
    """List all locations"""
    template_name = "restaurants/locations/list.html"
    model = Location


List.register(bp, "/")
# Create.register(bp, "/create")
# Edit.register(bp, "/edit/<int:id>")
# Delete.register(bp, "/delete")
