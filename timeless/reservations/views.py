""" Views for reservations """
from datetime import datetime
from http import HTTPStatus

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, jsonify
)

from timeless import DB
from timeless.reservations.forms import ReservationForm, SettingsForm
from timeless.restaurants.models import Reservation
from timeless import views
from timeless.access_control.views import SecuredView
from timeless.reservations import models


BP = Blueprint("reservations", __name__, url_prefix="/reservations")


class ReservationsListView(views.ListView):
    """ List the reservations """
    model = Reservation
    template_name = "reservations/list.html"


class ReservationsViewCreate(views.CreateView):
    """ Create a new reservation instance"""
    template_name = "reservations/create_edit.html"
    success_view_name = "reservations.list"
    form_class = ReservationForm


class ReservationsEditView(views.UpdateView):
    """Update reservation"""
    template_name = "restaurants/create_edit.html"
    form_class = ReservationForm
    model = Reservation
    success_view_name = "reservations.list"


class ReservationsDeleteView(views.DeleteView):
    """Delete reservation
    Deletes location using id and redirects to list page
    """
    success_view_name = "reservations.list"
    model = Reservation


ReservationsListView.register(BP, "/", name="list")
ReservationsViewCreate.register(BP, "/create", name="create")
ReservationsEditView.register(BP, "/edit/<int:id>", name="edit")
ReservationsDeleteView.register(BP, "/delete/<int:id>", name="delete")


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
    success_view_name = "reservations.settings_list"
    form_class = SettingsForm


SettingsCreateView.register(BP, "/settings/create/")


class SettingsDetailView(views.DetailView):
    """ Detail view for Reservation Settings  """
    model = models.ReservationSettings
    template_name = "restaurants/tables/create_edit.html"


SettingsDetailView.register(BP, "/settings/edit/<int:setting_id>")


class SettingsDelete(views.DeleteView):
    """ Delete view for Reservation Settings  """
    model = models.ReservationSettings
    template_name = "reservations/settings/list.html"


SettingsDelete.register(BP, "/settings/delete/<int:setting_id>")


class CommentView(SecuredView, views.CrudAPIView):
    """API Resource for comments /api/comments

    @todo #267:30min Add resource property to CommentView class so that the
      /api/comments endpoint works and #267 can be solved. Look at CrudAPIView
      code to understand why resource property is needed.
    """
    model = models.Comment
    url_lookup = "comment_id"
    list_reservations = "reservation_comment"


class ReservationView(views.CrudAPIView):
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


class CreateReservation(views.CrudAPIView):
    """ Create a new reservation instance """

    def post(self):
        """ Create new reservation """
        """
        @todo #434:30min Continue the implementation of CreateReservation. 
         Add authentication and refactor using CrudAPIView also edit and 
         delete methods for Reservations. Tests for these are skipped.
         Created reservation should be returned as a JSON object
        """
        form = ReservationForm(request.form)
        try:
            if form.validate():
                reservation = Reservation(
                    start_time=request.form["start_time"],
                    end_time=request.form["end_time"],
                    num_of_persons=request.form["num_of_persons"],
                    comment=request.form["comment"],
                    status=request.form["status"]
                )
                DB.session.add(reservation)
                DB.session.commit()
                return jsonify(status="success"), HTTPStatus.CREATED

            return jsonify(
                status="error",
                errors=form.errors
            ), HTTPStatus.BAD_REQUEST

        except Exception as error:
            return jsonify(
                status="error",
                errors=error
            ), HTTPStatus.BAD_REQUEST


CreateReservation.register(BP, "/create")
