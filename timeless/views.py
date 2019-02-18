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
from werkzeug.exceptions import abort

from flask import views, render_template, request, redirect, url_for


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


class GenericView(views.View):
    """ Generic view with common logic """
    template_name = None
    methods = ["get", "post"]
    permissions = ()

    def dispatch_request(self, *args, **kwargs):
        """This method is called with all the arguments from the URL rule."""
        http_method = request.method.lower()
        if http_method not in self.methods:
            raise Exception("Method is not allowed")

        if not self.check_permissions():
            raise Exception("Permissions weren't passed")

        method = getattr(self, http_method, None)
        if not method:
            raise Exception(f"Provide {http_method} method")

        return method(*args, **kwargs)

    def check_permissions(self):
        """ Method for permissions checking """
        for permission in self.permissions:
            permission.check()
        return True

    def get_template_name(self):
        """ Setup of template name """
        return self.template_name

    def render_template(self, context):
        """ Render template and provide context """
        return render_template(self.get_template_name(), **context)


class ListView(GenericView):
    """ Example:
        class SettingsListView(views.ListView):
            template_name = "restaurants/tables/list.html"

            def get_query(self):
                return models.Table.query.all()
    """

    def get_query(self):
        """ Method determines query"""
        raise NotImplementedError()

    def get(self):
        """ Fetch list of objects and pass it to template"""
        objects_list = self.get_query()
        return self.render_template({"object_list": objects_list})


class SingleObjectMixin:
    model = None

    def get_object(self, id=None):
        """ Method fetch object from given model by id """
        assert self.model, "Model is not provided"
        return self.model.query.get(id)


class DetailView(SingleObjectMixin, GenericView):
    """
    Example:
        class SettingsDetailView(views.DetailView):
            model = models.ReservationSettings
            template_name = "restaurants/tables/create_edit.html"
            success_url_name = "reservation_settings_list"
            not_found_url_name = "reservation_settings_list"
    """
    not_found_url_name = None
    success_url_name = None

    def get(self, id=None):
        """
        Get method fetch object from db and render it into template
        """
        assert self.not_found_url_name, "not_found_url_name is required"

        instance = self.get_object(id)
        if not instance:
            return redirect(url_for(self.not_found_url_name))

        return self.render_template({"instance": instance})


class CreateUpdateView(SingleObjectMixin, GenericView):
    """Example
        class SettingsCreateUpdateViewView(views.CreateUpdateView):
            template_name = "restaurants/tables/create_edit.html"
            success_url_name = "reservation_settings_list"
            form = forms.SettingsForm
    """
    form = None
    success_url_name = None
    not_found_url_name = None

    def get(self, id=None):
        """Get method render create template """
        assert self.form, "Form is required"
        form = self.form()
        if id:
            instance = self.get_object(id)
            if not instance:
                return redirect(url_for(self.not_found_url_name))
            form = self.form.TableForm(instance=instance)

        return self.render_template({"form": form})

    def post(self, id=None):
        """
        Post method checks form validation,
        save into db and redirect to success_url
        """
        assert self.form, "Form is required"
        assert self.success_url_name, "Success_url_name is required"
        form = self.form(request.form)
        if form.validate():
            form.save()
        return redirect(url_for(self.success_url_name))


class DeleteView(SingleObjectMixin, GenericView):
    """
    Example:
    class SettingsDeleteView(views.DeleteView):
        success_url_name = "reservation_settings_list"
    """
    success_url_name = None

    def delete(self, id=None):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        instance = self.get_object(id)
        instance.delete()
        return redirect(url_for(self.success_url_name))

    def post(self, id=None):
        """ Post method for object delete"""
        return self.delete(id)


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
