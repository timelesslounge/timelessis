from flask import views, render_template, request


class CrudAPIView(views.MethodView):
    """View that supports generic crud operations.
    Example of using CrudAPIView:

    class CommentView(CrudView):

         model = Comment
         url_lookup = "comment_id"

    @todo #123:30min Continue with the implementation of CrudAPIView.
     Implement post, put and delete methods. We should return json
     representation of object model in methods.
    """
    model = None
    url_lookup = None

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
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
            raise Exception("Method is not allowed2")

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
        pls add here example of usage, when it will be
    """
    def get_objects(self):
        """ Method for fetching list of objects from db"""
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        """ Method for fetching object from db"""
        raise NotImplementedError()


class DetailView(GenericView):
    """
    Example:
        class TableView(DetailView):
            def get(self, pk=None, *args, **kwargs):
                if pk:
                    table = models.Table.query.get(id)
                    if not table:
                        return redirect(url_for("tables.list"))
                    form = forms.TableForm(request.form, instance=table)
                else:
                    form = forms.TableForm(request.form)
                return render_template(
                    "restaurants/tables/create_edit.html", form=form)

            def post(self, pk=None, *args, **kwargs):
                form = forms.TableForm(request.form)
                if form.validate():
                    form.save()
                    return redirect(url_for("tables.list"))
                return render_template(
                    "restaurants/tables/create_edit.html", form=form)
    """
    def get_object(self):
        """ Method for fetching object from db"""
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        """ Get method implementation """
        raise NotImplementedError()

    def post(self, *args, **kwargs):
        """ Post method implementation"""
        raise NotImplementedError()
