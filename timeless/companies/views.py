"""Company views module."""
from flask import views

from timeless.companies import models


class Resource(views.MethodView):
    """API Resource for companies /api/companies"""
    def get(self, company_id):
        """
        Get method of Resource
        @todo #39:30min Bring marshmallow lib for serializing/deserializing
         objects see more here https://flask-marshmallow.readthedocs.io/en/latest/
         It's necessary for our API ViewSets,
         it helps validate data from request and deserialize it from objects to response
        """
        if company_id:
            return "Detail get method of CompanyViewSet", 200
        return "Get method of CompanyViewSet", 200

    def post(self):
        """Post method of Resource"""
        return "Post method of CompanyViewSet", 201

    def put(self, company_id):
        """Put method of Resource"""
        if company_id:
            return "Detail put method of CompanyViewSet", 200
        return "Put method of CompanyViewSet", 200

    def delete(self, company_id):
        """Delete method of Resource"""
        if company_id:
            return "Detail delete method of CompanyViewSet", 204
        return "Delete method of CompanyViewSet", 204
