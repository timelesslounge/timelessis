"""Company views module."""

from timeless.access_control.views import SecuredView


class Resource(SecuredView):

    resource = "company"

    """API Resource for companies /api/companies"""
    def get(self, company_id):
        """
        Get method of Resource
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
