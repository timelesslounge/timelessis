from flask import abort, views, request
from http import HTTPStatus

from timeless.access_control import authorization


class SecuredView(views.MethodView):
    """Adds user access control to a specif view.
    Example:
        class Company(SecuredView):

            resource="company"

            def get(self, company_id):
                ...
    """

    def dispatch_request(self, *args, **kwargs):
        if self.resource and not authorization.is_allowed(
            method=request.method.lower(), resource=self.resource,
            *args, **kwargs
        ):
            abort(HTTPStatus.FORBIDDEN)
        return super().dispatch_request(*args, **kwargs)
