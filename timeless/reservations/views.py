""" Views for reservations """
from datetime import datetime

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)

from timeless import views
from timeless.access_control.views import SecuredView
from timeless.reservations import models


bp = Blueprint("reservations", __name__, url_prefix="/reservations")


class SettingsList(views.ListView):
    """
    List view set for Reservation Settings
    @todo #186:30min For SettingsListView, SettingsCreateView,
     SettingsDetailView, SettingsDeleteView create correct templates
     for list, create/detail actions. When templates will be done, pls change
     `template_name` value in every View Class.
    @todo #173:30min Refactor (and uncomment) views below to use new
     base views once when they are avaiable. Current implementation is not
     generic enough.
    """
    model = models.ReservationSettings
    template_name = "restaurants/tables/list.html"


SettingsList.register(bp, "/settings/")

# class SettingsCreateUpdateView(views.CreateUpdateView):
#     """ Reservation settings create view """
#     template_name = "restaurants/tables/create_edit.html"
#     success_url_name = "reservation_settings_list"
#     form = forms.TableForm
#     model = models.ReservationSettings


# class SettingsDetailView(views.DetailView):
#     """ Reservation settings detail view"""
#     model = models.ReservationSettings
#     template_name = "restaurants/tables/create_edit.html"
#     success_url_name = "reservation_settings_list"
#     not_found_url_name = "reservation_settings_list"


# class SettingsDeleteView(views.DeleteView):
#     success_url_name = "reservation_settings_list"


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


@bp.route("/")
def list_reservations(reservations):
    reservations_result = []
    reservations_string = reservations.data['reservations']
    qry = db_session.query(Reservations).filter(Reservations.id.contains(reservations_string))
    reservations_result = qry.all()
    """
    flash("List not yet implemented")
    """
    if not reservations_result:
        flash('No results found!')
        return redirect('/')
    else:
        reservations_table = Results(reservations_result)

    return render_template(
        	"restaurants/tables/list.html", reservations=reservations_table
	)


@bp.route("/create", methods=("GET", "POST"))
def create(reservation):
    if request.method == "POST":
        flash("Create not yet implemented")

    return render_template(
        "restaurants/tables/create_edit.html", action="create",
        reservation=reservation
    )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    return render_template(
        "restaurants/tables/create_edit.html", action="edit",
        id=id
    )


@bp.route("/delete", methods=["POST"])
def delete():
    flash("Delete not yet implemented")
    return redirect(url_for("reservations.list_reservations"))
