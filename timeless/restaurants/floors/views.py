"""Floors views module.
@todo #421:30min Continue implementing list floors view. Floors index page
 must allow sorting and filtering of floors for every column and it has to be
 accessed by the Location page. Then remove skip annotation from
 FloorsListView tests for ordering and filtering. Authentication must be 
 faked in order to test work.
@todo #95:30min Continue on developing create floor view. After creation we 
 should render Detail view showing the newly inserted  floor information and 
 a message with the result of the insertion of this data to the repository.
 The tests must cover if the screen is being showed correctly and if the 
 errors are being displayed if any.
@todo #95:30min Implement edit / update floor views. Edit / update floor
 view is composed of two views: first view of edit / floor view must load the
 desired floor data onto the screen and must extend
 timeless/views.py::DetailView; second part of update view extends
 timeless/views.py::UpdateView, receives data from the first view and
 must save the data to the repository. The tests must include checking if the
 view screens were correctly built and if the data was saved to the repository.
@todo #424:30min The last step for deletion is to ask for confirmation before
 actually deleting the object. When clicking on link on list floors pages a
 javascript modal should appear asking user for confirmation. Also make sure
 that when a floor is deleted, all depending entities (like Tables, for 
 example) are deleted
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless import views
from timeless.auth import views as auth
from timeless.restaurants.floors.forms import FloorForm
from timeless.restaurants.models import Floor


BP = Blueprint("floor", __name__, url_prefix="/floors")


class List(views.ListView):
    """List all floors"""
    template_name = "restaurants/floors/list.html"
    model = Floor


@BP.route("/edit/<int:id>", methods=("GET", "POST"))
@auth.login_required
def edit(id):
    """ Edit floor with id """
    if request.method == "POST":
        flash("Edit not yet implemented")
    action = "edit"
    return render_template(
        "restaurants/floors/create_edit.html",
        action=action
        )


class Delete(views.DeleteView):
    """ Delete floor with id """  
    decorators = (auth.login_required,)
    model = Floor
    success_view_name = "floor.list"


class Create(views.CreateView):
    """ Create a new floor instance """
    decorators = (auth.login_required,)
    template_name = "restaurants/floors/create_edit.html"
    success_view_name = "floor.list"
    form_class = FloorForm


class Detail(views.DetailView):
    """ Detail view for Reservation Settings  """
    model = Floor
    template_name = "restaurants/floors/create_edit.html"


Create.register(BP, "/create")
List.register(BP, "/")
Delete.register(BP, "/delete/<int:id>")
Detail.register(BP, "/<int:id>")
