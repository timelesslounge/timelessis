""" Views for reservations """
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, views
)
from http import HTTPStatus

from timeless import DB
from timeless.access_control.views import SecuredView
from timeless.reservations.controllers import SettingsController
from timeless.reservations.forms import ReservationForm
from timeless.reservations.models import Comment
from timeless.restaurants.models import Reservation
from timeless.views import CrudAPIView


bp = Blueprint("reservations", __name__, url_prefix="/reservations")


class SettingsView(SecuredView):
    """ Reservation settings API """

    resource = "reservation_settings"
    ctr = SettingsController()

    def get(self, id):
        """ GET method for reservation settings """
        if id:
            return self.ctr.get_settings_for_reservation(id), HTTPStatus.OK
        return self.ctr.get_all_reservation_settings(), HTTPStatus.OK

    def post(self):
        """ POST method for reservation settings """
        return self.ctr.create_settings_for_reservation(self), HTTPStatus.CREATED

    def put(self, id):
        """ PUT method for reservation settings """
        return self.ctr.update_reservation_settings(self, id), HTTPStatus.OK

    def delete(self, id):
        """ DELETE method for reservation settings """
        return self.ctr.delete_reservation_settings(id), HTTPStatus.NO_CONTENT


class CommentView(SecuredView, CrudAPIView):
    """API Resource for comments /api/comments

    """
    model = Comment
    url_lookup = "comment_id"
    list_reservations = "reservation_comment"


@bp.route("/")
def list_reservations(reservations):
    """
        @todo #172:30min Refactor this after the implementation of GenericViews.
         Take a look at puzzles #134 and #173 where the requirements of generic
         views are described. Don't forget to cover the generated code with
         tests

    :param reservations:
    :return:
    """
    flash("List not yet implemented")
    return render_template(
        "restaurants/tables/list.html", reservations=reservations
    )


@bp.route("/create", methods=("GET", "POST"))
def create():
    """ Create new reservation """
    form = ReservationForm(request.form)
    form.validate()
    if request.method == "POST" and form.validate():
        form.save()
        return redirect(url_for("reservations.list_reservations"))
    return render_template(
        "reservations/create_edit.html", action="create",
        form=form
    )


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    if request.method == "POST":
        flash("Edit not yet implemented")
    return render_template(
        "reservations/create_edit.html", action="edit",
        id=id
    )


@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    """ Delete reservation """
    reservation = Reservation.query.get(id)
    DB.session.delete(reservation)
    DB.session.commit()
    return redirect(url_for("reservations.list_reservations"))
