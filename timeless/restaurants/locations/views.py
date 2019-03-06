"""Locations views module.
@todo #208:30min Remove function endpoints once the view classes are in place.
 See #173 for more details about generic views use CreateView, EditView and
 DeleteView as provided in the commented code templates. Uncomment and modify
 this code - create missing view templates and write ITs to verify behaviour.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless import views
from timeless.restaurants.models import Location
from timeless.restaurants.locations.forms import LocationForm


BP = Blueprint("location", __name__, url_prefix="/locations")


class Create(views.CreateView):
    """ Create a new location instance"""
    template_name = "restaurants/locations/create_edit.html"
    success_view_name = "location.list"
    form_class = LocationForm


# class Edit(UpdateView):
#     """Update location"""
#     template_name = "restaurants/locations/create_edit.html"
#     form_class  = LocationForm
#     model = Location
@BP.route("/edit/<int:id>", methods=("GET", "POST"))
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
@BP.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("location.list"))


class List(views.ListView):
    """List all locations"""
    template_name = "restaurants/locations/list.html"
    model = Location


List.register(BP, "/")
Create.register(BP, "/create")
# Edit.register(bp, "/edit/<int:id>")
# Delete.register(bp, "/delete")
