from http import HTTPStatus
from flask import request, views
from werkzeug.exceptions import abort

from timeless.db import DB


class CrudAPIView(views.MethodView):
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
    model = None
    url_lookup = None

    """
    @todo #221:30min Continue with the implementation of CrudAPIView.
     Implement get, post, put and delete methods. We should return json representation of object model in methods. Use 
     FakeModel for a fake database object, and implement the desired calls on FakeQuery to get, create, save / update 
     and delete returnin the result. Don't forget to implement the tests too, to test if CrudAPIView code is being 
     called and returning the expected objects; please refer to #221 and #222 for documentation. After that remove the 
     ignore annotation from tests on test_crud_api.py.
    """

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class FakeModel(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    class FakeQuery(object):

        def get(object_id):
            print('Python is really finger in the ass huhu')
            if object_id == 5:
                return {"Found the object"},HTTPStatus.OK
            abort(HTTPStatus.NOT_FOUND)

    query = FakeQuery()


class FakeAPIView(CrudAPIView):
    model = FakeModel
    url_lookup = "some_id"
