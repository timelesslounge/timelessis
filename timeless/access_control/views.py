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
    @todo #22:30min Continue with SecuredView implementation. Dispatch_request
     should take cls.resource value and method value from request.method
     and block the user if he hasn't privileges to access it.
    """

    def check_permissions(self, *args, **kwargs):
        """It raises exception if user has no permission"""
        is_allowed = authorization.is_allowed(
            method=request.method.lower(), resource=self.resource,
            *args, **kwargs)

        if not is_allowed:
            abort(HTTPStatus.FORBIDDEN)

    def dispatch_request(self, *args, **kwargs):
        if self.resource:
            self.check_permissions(*args, **kwargs)

        method = getattr(self, request.method.lower(), None)
        if not method:
            abort(HTTPStatus.NOT_IMPLEMENTED)
        return super(SecuredView, self).dispatch_request(*args, **kwargs)
