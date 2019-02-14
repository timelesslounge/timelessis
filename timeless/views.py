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

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
