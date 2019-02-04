from http import HTTPStatus

from flask import Blueprint, views

bp = Blueprint("reservations", __name__, url_prefix="/reservations")


@bp.route("/settings")
def base():
    """
    @todo #32:30min Continue implementing Settings page for Reservations,
     it will be deployed on a different subdomain. Page should have set of
     fields from ReservationSettings model.
    """
    return "Settings API entry point"


class CommentView(views.MethodView):
    """API Resource for comments /api/comments"""

    def get(self, comment_id):
        """Get method of CommentView
        @todo #87:30min Continue implementation of view methods for get,
         create, edit and delete. In the index page it should be possible
         to sort and filter for every column.
        """
        if comment_id:
            return "Detail get method of CommentViewSet", HTTPStatus.OK
        return "Get method of CommentViewSet", HTTPStatus.OK

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



