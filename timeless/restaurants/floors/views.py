"""Floors views module.
@todo #95:30min Continue implementing list floors view. Floors index page
 must allow sorting and filtering of floors for every column and it has to be
 accessed by the Location page. Then remove skip annotation from
 FloorsListView test. Authentication must be faked in order to test work.
@todo #95:30min Implement create floor view. Create floor view must extend
 timeless/views.py::CreateView and implement floor creation. First screen
 must show empty fields for floor data input and second view must show the
 newly inserted  floor information and a message with the result of the
 insertion of this data to the repository. The tests must cover if the
 screen is being showed correctly and if the errors are being displayed if any.
@todo #95:30min Implement edit / update floor views. Edit / update floor
 view is composed of two views: first view of edit / floor view must load the
 desired floor data onto the screen and must extend
 timeless/views.py::DetailView; second part of update view extends
 timeless/views.py::UpdateView, receives data from the first view and
 must save the data to the repository. The tests must include checking if the
 view screens were correctly built and if the data was saved to the repository.
@todo #95:30min Implement delete floor view. Delete floor view is composed of
 two views: the first view must load the desired floor data onto the screen
 and show an button to delete the selected view, extending
 timeless/views.py::DetailView; second view must show the result message of
 floor deletion.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from timeless import views
from timeless.auth import views as auth
from timeless.views import ListView
from timeless.restaurants.floors.forms import FloorForm
from timeless.restaurants.models import Floor


BP = Blueprint("floor", __name__, url_prefix="/floors")


class FloorListView(ListView):
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


@BP.route("/delete", methods=["POST"])
@auth.login_required
def delete():
    """ Delete floor with id """
    flash("Delete not yet implemented")
    return redirect(url_for("floor.list_floors"))


class Create(views.CreateView):
    """ Create a new floor instance """
    decorators = (auth.login_required,)
    template_name = "restaurants/floors/create_edit.html"
    success_view_name = "floor.list"
    form_class = FloorForm


Create.register(BP, "/create")
FloorListView.register(BP, "/")
