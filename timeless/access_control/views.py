from flask import views, request


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
    def dispatch_request(self, *args, **kwargs):
        method = getattr(self, request.method.lower(), None)
        assert method is not None, "Unimplemented method %r" % request.method
        return super(SecuredView, self).dispatch_request(*args, **kwargs)
