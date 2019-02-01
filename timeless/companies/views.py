"""Company views module."""
from flask import views

from timeless.companies import models


class Resource(views.MethodView):
    """API Resource for companies /api/companies"""
    def get(self):
        """
        @todo #39:30min Bring marshmallow lib for serializing/deserializing
         objects see more here https://flask-marshmallow.readthedocs.io/en/latest/
         It's necessary for our API ViewSets,
         it helps validate data from request and deserialize it from objects to response
        """
        return "Get method of CompanyViewSet", 200

    def post(self):
        return "Post method of CompanyViewSet", 201

    def put(self):
        return "Put method of CompanyViewSet", 200

    def delete(self):
        return "Delete method of CompanyViewSet", 204
