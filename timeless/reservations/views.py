""" Views for reservations """
from http import HTTPStatus

from flask import views

from timeless.reservations.controllers import SettingsController
from timeless.reservations.models import Comment


class SettingsView(views.MethodView):
    """ Reservation settings API """
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


class CommentView(views.MethodView):
    """API Resource for comments /api/comments"""

    def get(self, comment_id):
        """Get method of CommentView
        @todo #123:30min Continue implementation of view methods for get,
         create, edit and delete. In the index page it should be possible
         to sort and filter for every column.
        """
        if comment_id:
            return Comment.query.filter(Comment.id==comment_id).one().body, HTTPStatus.OK
        return "Get all method of CommentViewSet", HTTPStatus.OK

    def post(self):
        """Post method of CommentView"""
        return "Post method of CommentViewSet", HTTPStatus.CREATED

    def put(self, comment_id):
        """Put method of CommentView"""
        if comment_id:
            return "Detail put method of CommentViewSet", HTTPStatus.OK
        return "Put method of CommentViewSet", HTTPStatus.OK

    def delete(self, comment_id):
        """Delete method of CommentView"""
        if comment_id:
            return "Detail delete method of CommentViewSet", HTTPStatus.NO_CONTENT
        return "Delete method of CommentViewSet", HTTPStatus.NO_CONTENT
