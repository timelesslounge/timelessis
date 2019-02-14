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
    def dispatch_request(self):
        """Subclasses have to override this method to implement the
        actual view function code.  This method is called with all
        the arguments from the URL rule.
        """
        raise NotImplementedError()

    def get_template_name(self):
        """ Setup of template name """
        raise NotImplementedError()


class ListView(GenericView):
    def get_objects(self):
        """ Method for fetching list of objects from db"""
        raise NotImplementedError()

    def get_template_name(self):
        """ Setup of template name """
        raise NotImplementedError()

    def render_template(self, context):
        """ Render template and provide context """
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        """ Dispatch method for managing logic """
        context = {'objects': self.get_objects()}
        return self.render_template(context)


class DetailView(GenericView):
    def get_object(self):
        """ Method for fetching object from db """
        raise NotImplementedError()

    def get_template_name(self):
        """ Setup of template name """
        raise NotImplementedError()

    def render_template(self, context):
        """ Render template and provide context """
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        """ Dispatch method for managing logic """
        if request.POST:
            pass
        context = {'objects': self.get_object()}
        return self.render_template(context)
