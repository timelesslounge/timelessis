""" Views for reservations """
from datetime import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)

from timeless import DB
from timeless.reservations.forms import ReservationForm
from timeless.restaurants.models import Reservation, ReservationStatus
from timeless import views
from timeless.access_control.views import SecuredView
from timeless.reservations import models


BP = Blueprint("reservations", __name__, url_prefix="/reservations")


class SettingsList(views.ListView):
    """
    List view set for Reservation Settings
    @todo #293:30min For SettingsCreateView, SettingsDetailView,
     SettingsDeleteView create correct templates for list, create/detail
     actions. When templates will be done, pls change `template_name` value
     in every View Class.
    """
    model = models.ReservationSettings
    template_name = "restaurants/tables/list.html"


SettingsList.register(BP, "/settings/")


class SettingsCreateView(views.CreateView):
    """ Create view for Reservation Settings """
    model = models.ReservationSettings
    template_name = "restaurants/tables/create_edit.html"
    success_view_name = "reservation_settings_list"
    form_class = ReservationForm


SettingsCreateView.register(BP, "/settings/create/")


class SettingsDetailView(views.DetailView):
    """ Detail view for Reservation Settings  """
    model = models.ReservationSettings
    template_name = "restaurants/tables/create_edit.html"


SettingsDetailView.register(BP, "/settings/edit/<int:setting_id>")


class SettingsDelete(views.DeleteView):
    """ Delete view for Reservation Settings  """
    model = models.ReservationSettings


SettingsDelete.register(BP, "/settings/delete/<int:setting_id>")


class CommentView(SecuredView, views.CrudAPIView):
    """API Resource for comments /api/comments

    """
    model = models.Comment
    url_lookup = "comment_id"
    list_reservations = "reservation_comment"


class ReservationsListView(views.CrudAPIView):
    """ Reservation JSON API /api/reservations

    """

    def get(self, company_id):
        """Retrieve reservations based on location, and date.
            @todo #28:30min Implement actual fetching of reservations. We need
             to return a JSON list, filtered by reservations based on location
             and date. We also need to password protect this API, and filter
             those belonging to the specific company ID. Let's implement the
             serialization and deserialization of JSON based on this API:
             https://flask-marshmallow.readthedocs.io/en/latest/

        :param self:
        :return:
        """
        reservations_json = {
            "items": [
                {
                    "id": 1,
                    "start_time": datetime(1, 1, 1),
                    "end_time": datetime(1, 1, 1),
                    "customer_id": 1,
                    "num_of_persons": 1,
                    "comment": "Test",
                    "status": 2
                }
            ]
        }
        return jsonify(reservations_json)


@BP.route("/list", methods=("GET",))
def list():
    """
        @todo #172:30min Refactor this after the implementation of GenericViews.
         Take a look at puzzles #134 and #173 where the requirements of generic
         views are described. Don't forget to cover the generated code with
         tests

    :param reservations:
    :return:
    """
    flash("List not yet implemented")
    return render_template("restaurants/tables/list.html")


@BP.route("/create", methods=("GET", "POST"))
def create():
    """ Create new reservation """
    """
    @todo #380:30min Continue. When we use the form.validate() function the
     status (enum: timeless/restaurants/models.py) is displaying the
     following error: 'status': ['Invalid Choice: could not coerce', 'Not a
     valid choice']. Removes the commented if to see the error. Also refactor
     the function using genericViews, as explained in puzzles #134 and #137.
    """
    form = ReservationForm(request.form)
    try:
        """if request.method == "POST" and form.validate():"""
        if request.method == "POST":
            reservation = Reservation(
                start_time=request.form["start_time"],
                end_time=request.form["end_time"],
                num_of_persons=request.form["num_of_persons"],
                comment=request.form["comment"],
                status=request.form["status"]
            )
            DB.session.add(reservation)
            DB.session.commit()
            return redirect(url_for("reservations.list"))
        else:
            flash("Error: ", form.errors)
    except Exception as error:
        flash("Error: ", error)

    return render_template("reservations/create_edit.html", error=form.errors,
                            action="create", form=form)


@BP.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    return render_template(
        "reservations/create_edit.html", action="edit",
        id=id
    )


@BP.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete reservation """
    reservation = Reservation.query.get(id)
    DB.session.delete(reservation)
    DB.session.commit()
    return redirect(url_for("reservations.list"))
