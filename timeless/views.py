"""View that supports generic crud operations.
Example of using CrudAPIView:

class CommentView(CrudView):

     model = Comment
     url_lookup = "comment_id"

@todo #221:30min Remove references to database objects. we should not tie
 our view layer to our database objects. We should create some form of
 abstraction to handle the model calls, for example,
 model.query.get(object_id) that would decorate the real implementation,
 eliminating the coupling here.
"""
from http import HTTPStatus
from flask import views
from werkzeug.exceptions import abort


class CrudAPIView(views.MethodView):
    """View that supports generic crud operations.

    @todo #221:30min Continue with the implementation of CrudAPIView.
     Implement get, post, put and delete methods. We should return json
     representation of object model in methods. Use FakeModel for a fake
     database object, and implement the desired calls on FakeQuery to get,
     create, save / update and delete returning the result. Don't forget to
     implement the tests too, to test if CrudAPIView code is being called and
     returning the expected objects; please refer to #221 and #222 for
     documentation. After that remove the ignore annotation from tests on
     test_crud_api.py.
    """

    def get(self):
        """Calls the GET method."""
        pass

    def post(self):
        """Calls the POST method."""
        pass

    def put(self):
        """Calls the PUT method."""
        pass

    def delete(self):
        """Calls the DELETE method."""
        pass


class FakeModel():
    """Fake model for tests."""

    class FakeQuery:
        """Fake query for tests."""

        def get(self, object_id):
            """Fake response on get method."""
            if object_id == 5:
                return {"Found the object"}, HTTPStatus.OK
            abort(HTTPStatus.NOT_FOUND)

    query = FakeQuery()


class FakeAPIView(CrudAPIView):
    """Fake CrudAPI imoplementation for tests."""
    model = FakeModel
    url_lookup = "some_id"
