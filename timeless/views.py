from http import HTTPStatus

from flask import views
from werkzeug.exceptions import abort


class CrudView(views.MethodView):
    """View that supports generic crud operations.
      @todo #123:30min Continue with the implementation of CrudView.
       Implement post, put and delete methods.
       This view should render templates specified by user.
       Example of using CrudView:

       class CommentView(CrudView):

            model = Comment

            templates = {
                "create":"create.html",
                "edit":"edit.html",
                "list":"list.html",
                "delete:"delete.html"
            }
    """
    model = None

    def get(self, *args, **kwargs):
        object_id = next(iter(kwargs.values()))
        if object_id:
            result = self.model.query.get(object_id)
            if result is None:
                abort(404)
        return "", HTTPStatus.OK
