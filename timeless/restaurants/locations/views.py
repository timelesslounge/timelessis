"""Locations views module.
@todo #208:30min Continue implementing Create, Edit and Delete views once
 generic views from #173 are implemented. Templates are already provided below,
 so uncomment and modify - create view templates and write ITs to verify
 behaviour.
@todo #208:30min Continue implementing List to enable sorting and filtering
 for every column. For this, probably there will be a need to create a new
 generic view that all other List views will extend. This generic view should
 use GenericFilter implemented in #317.
"""
from flask import Blueprint

from timeless.views import ListView
from timeless.restaurants.models import Location

bp = Blueprint("location", __name__, url_prefix="/locations")


# class Create(CreateView):
#     """Create location"""
#     template_name = "restaurants/locations/create_edit.html"
#     form_class  = LocationForm
#     model = Location


# class Edit(UpdateView):
#     """Update location"""
#     template_name = "restaurants/locations/create_edit.html"
#     form_class  = LocationForm
#     model = Location


# class Delete(DeleteView):
#     """Delete location
#     Deletes location using id and redirects to list page
#     """
#     form_class  = LocationForm
#     model = Location


class LocationList(ListView):
    """List all locations"""
    template_name = "restaurants/locations/list.html"
    model = Location


LocationList.register(bp, "/")
# Create.register(bp, "/create")
# Edit.register(bp, "/edit/<int:id>")
# Delete.register(bp, "/delete")
