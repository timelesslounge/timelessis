from http import HTTPStatus

from flask import views
from werkzeug.exceptions import abort


class CrudAPIView(views.MethodView):
    """View that supports generic crud operations.
    Example of using CrudAPIView:

    class CommentView(CrudView):

         model = Comment
         url_lookup = "comment_id"

    @todo #123:30min Continue with the implementation of CrudAPIView.
     Implement post, put and delete methods. We should return json
     representation of object model in methods.
    """
    model = None
    url_lookup = None

    def get(self, *args, **kwargs):
        object_id = kwargs.get(self.url_lookup)
        if object_id:
            result = self.model.query.get(object_id)
            if result is None:
                abort(404)
        return "", HTTPStatus.OK
