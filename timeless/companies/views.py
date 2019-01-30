from flask import views

from timeless.companies import models


class CompanyViewSet(views.MethodView):
    def get(self, company_id):
        """
        @todo #39:30min Bring marshmallow lib for serializing/deserializing
         objects see more here https://flask-marshmallow.readthedocs.io/en/latest/
         It's necessary for our API ViewSets,
         it helps validate data from request and deserialize it from objects to response
        """
        return "Get method of CompanyViewSet", 200

    def post(self):
        return "Post method of CompanyViewSet", 201

    def put(self, company_id):
        return "Put method of CompanyViewSet", 200

    def delete(self, company_id):
        return "Delete method of CompanyViewSet", 204
