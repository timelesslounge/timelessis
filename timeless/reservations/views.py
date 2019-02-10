""" Views for reservations """
from http import HTTPStatus

from flask import views
from timeless.reservations.controllers import SettingsController, CommentsController


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
    ctr = CommentsController()

    def get(self, comment_id):
        """Get method of CommentView
        @todo #87:30min Continue implementation of view methods for get,
         create, edit and delete. In the index page it should be possible
         to sort and filter for every column.
        """
        if comment_id:
            return self.ctr.get_comment(comment_id), HTTPStatus.OK
        return self.ctr.get_all_comments(), HTTPStatus.OK

    def post(self):
        """Post method of CommentView"""
        return self.ctr.create_comment(comment=None), HTTPStatus.CREATED

    def put(self, comment_id):
        """Put method of CommentView"""
        return self.ctr.update_comment(comment_id=comment_id, comment=None), HTTPStatus.HTTPStatus.OK

    def delete(self, comment_id):
        """Delete method of CommentView"""
        return self.ctr.delete_comment(comment_id), HTTPStatus.HTTPStatus.NO_CONTENT
