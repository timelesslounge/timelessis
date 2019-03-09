"""Locations views module."""
from flask import Blueprint

from timeless import views
from timeless.restaurants.models import Location
from timeless.restaurants.locations.forms import LocationForm


BP = Blueprint("location", __name__, url_prefix="/locations")


class Create(views.CreateView):
    """ Create a new location instance"""
    template_name = "restaurants/locations/create_edit.html"
    success_view_name = "location.list"
    form_class = LocationForm


class Edit(views.UpdateView):
    """Update location"""
    template_name = "restaurants/locations/create_edit.html"
    form_class = LocationForm
    model = Location
    success_view_name = "location.list"


class Delete(views.DeleteView):
    """Delete location
    Deletes location using id and redirects to list page
    """
    success_view_name = "location.list"
    model = Location


class List(views.ListView):
    """List all locations"""
    template_name = "restaurants/locations/list.html"
    model = Location


List.register(BP, "/")
Create.register(BP, "/create")
Edit.register(BP, "/edit/<int:id>")
Delete.register(BP, "/delete/<int:id>")
