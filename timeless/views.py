from http import HTTPStatus

from flask import views
from werkzeug.exceptions import abort


class CrudAPIView(views.MethodView):
    """View that supports generic crud operations.
    Example of using CrudAPIView:

    class CommentView(CrudView):

         model = Comment
         url_lookup = "comment_id"

    @todo #221:30min Remove references to database objects. we should not tie our view layer to out database objects.
     We should create some form of abstraction to handle the model calls, for example, model.query.get(object_id) that
     would decorate the real implementation, eliminating the coupling here
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
