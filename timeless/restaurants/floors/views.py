"""Floors views module.
@todo #95:30min Continue implementing list floors view. Floors index page
 must allow sorting and filtering of floors for every column and it has to be
 accessed by the Location page. Then remove skip annotation from
 FloorsListView test.
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
 We must use a mock floor model to avoid connecting to the database for these
 tests.
@todo #95:30min Implement delete floor view. Delete floor view is composed of
 two views: the first view must load the desired floor data onto the screen
 and show an button to delete the selected view, extending
 timeless/views.py::DetailView; second view must show the result message of
 floor deletion. We must use a mock floor model to avoid connecting to
 database for these tests.
"""
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from timeless.auth import views as auth
from timeless.views import ListView

BP = Blueprint("floor", __name__, url_prefix="/floors")


class FloorListView(ListView):
    """List all floors"""
    template_name = "restaurants/floors/list.html"
    model = None


FloorListView.register(BP, "/")


@BP.route("/create", methods=("GET", "POST"))
@auth.login_required
def create():
    """ Create new floor """
    if request.method == "POST":
        flash("Create not yet implemented")
    action = "create"
    return render_template(
        "restaurants/floors/create_edit.html",
        action=action
        )


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
