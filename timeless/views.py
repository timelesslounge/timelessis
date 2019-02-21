"""Generic classes for API views and Template views.
@todo #173:30min Implement checking for permissions (like is user logged in or
 is user in role) using decorators for view. For that, create new view which
 all other views will extend. Example would be:
 class AdminView(View):
 ....decorators = [auth.admin_required, auth.login_required]
 class UserView(AdminView):
@todo #173:30min Refactor all blueprint views to use ListView for getting the
 list of objects from db using model. Also, make sure list.html template is
 made generic to allow all other views to use it. Feel free to add more puzzles
 since there are a lot of views.
@todo #173:30min Once CreateView is implemented, refactor all blueprint views
 to use it for validating the form and storing the record in the database.
@todo #173:30min Once UpdateView is implemented, refactor all blueprint views
 to use it for validating the form and updating the record in the database.
 Reuse SingleObjectMixin to provide simple solution to fetch by id.
@todo #173:30min Once DeleteView is implemented, refactor all blueprint views
 to use it for validating the form and deleting the record in the database.
 Reuse SingleObjectMixin to provide simple solution to fetch by id.

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
import re
from http import HTTPStatus

from flask import views, redirect, render_template, request, url_for
from werkzeug.exceptions import abort


camel_to_underscore = re.compile("((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")


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


class GenericView(views.MethodView):
    """ Generic view with common logic """
    template_name = None
    methods = ["get", "post"]

    @classmethod
    def register(cls, blueprint, route, name=None):
        """
        A shortcut method for registering this view to an app or blueprint.
        Assuming we have a blueprint and a CompanyCreate view, then these two
        lines are identical in functionality:
            views.add_url_rule('/companies/create',
                               view_func=CompanyCreate.as_view(
                                   'company_create')
                               )
            CompanyCreate.register(views, '/companies/create',
                                   'company_create')
        """
        if not name:
            # Convert "ViewName" to "view_name" and use it
            name = camel_to_underscore.sub(r"_\1", cls.__name__).lower()
            blueprint.add_url_rule(route, view_func=cls.as_view(name))

    def dispatch(self):
        """
        Hook for a subclass to call before dispatch actually happens.
        """
        pass

    def dispatch_request(self, *args, **kwargs):
        """
        Save args and kwargs, then dispatch the request as a normal MethodView,
        calling get() or post().
        """
        self.args = args
        self.kwargs = kwargs

        # If dispatch returns a value, use it. This most likely means it was a
        # redirect, or a custom result entirely.
        return self.dispatch() or super().dispatch_request(*args, **kwargs)

    def get_template_name(self):
        """
        Get the template_name. If this method is not overwritten, then a
        template_name variable must be declared.
        """
        if not self.template_name:
            raise NotImplementedError(f"{self.__class__.__name__} must define "
                                      f"either 'template_name' or "
                                      f"'get_template_names()'")
        return self.template_name

    def get_default_context(self):
        """
        Get the default context, which contains this view instance along with
        the kwargs.
        """
        return {
            "view": self,
            "kwargs": self.kwargs,
        }

    def get_context(self, **context):
        """
        Hook for a sublcass to add variables to request context.
        """
        return {
            **context,
            **self.get_default_context()
        }

    def get(self, *args, **kwargs):
        """
        Simply render the template with the context.
        """
        return self.render_to_response(self.get_context())

    def render_to_response(self, context):
        return render_template(self.get_template_name(), **context)


class ListView(GenericView):
    """
    A view that will render a template with a list of objects.
    """

    model = None
    context_object_list_name = "object_list"

    def get_context_object_list_name(self):
        """
        Get context_object_list_name.
        """
        return self.context_object_list_name

    def get_object_list(self):
        """
        Get the list of objects. If this method is not overwritten, then a
        model variable must be declared, and it must have query.all().
        """
        if self.model is None:
            raise NotImplementedError(f"{self.__class__.__name__} must define "
                                      f"either 'model' or 'get_object_list()'")
        return self.model.query.all()

    def get_default_context(self):
        """
        Add the object list to the context.
        """
        context = super().get_default_context()
        context[self.get_context_object_list_name()] = self.get_object_list()
        return context


class SingleObjectMixin:
    """ Fetch model from database using id """
    model = None

    def get_object(self, id=None):
        """ Method fetch object from given model by id """
        assert self.model, "Model is not provided"
        return self.model.query.get(id)


class DetailView(GenericView):
    """
    A view that will display details in a template for a single object.
    """
    context_object_name = "object"

    def get_context_object_name(self):
        """
        Get context_object_name.
        """
        return self.context_object_name

    def get_object(self):
        """
        Get the object. We don't make any assumptions, so this must be
        overwritten by the subclass.
        """
        raise NotImplementedError(f"self.__class__.__name__ must define "
                                  f"'get_object()'")

    def get_default_context(self):
        """
        Add the object to the context.
        """
        context = super().get_default_context()
        context[self.get_context_object_name()] = self.get_object()
        return context


class CreateView(GenericView):
    """ Class which creates objects based on received POST data and provided
    form class """
    form_class = None
    success_view_name = None

    def get_form(self, *args, **kwargs):
        """ Create form instance """
        if self.form_class is None:
            raise NotImplementedError(f"{self.__class__.__name__} must define "
                                      f"'form_class' attribute")
        return self.form_class(*args, **kwargs)

    def get_success_url_redirect(self):
        """ Reverse URL based on view name """
        if self.success_view_name is None:
            raise NotImplementedError(f"{self.__class__.__name__} must define "
                                      f"'success_view_name' attribute")
        return url_for(self.success_view_name)

    def get_context(self, *args, **kwargs):
        """ Pass 'from' instance to context if it's not provided
        (basicaly for 'get' method). """
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
        return super().get_context(*args, **kwargs)

    def post(self):
        form = self.get_form(request.form)

        if not form.validate():
            return self.render_to_response(self.get_context(form=form))

        form.save()
        return redirect(self.get_success_url_redirect())


class UpdateView(GenericView):
    """ Base view for updating objects"""


class DeleteView(GenericView):
    """ BAse view for deleting objects """


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
