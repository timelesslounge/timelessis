"""SchemeType views module.
@todo #56:30min Continue implementing Create, Edit and Delete views once
 generic views from #173 are implemented. Code templates are already provided
 below, so uncomment and modify - create templates and write ITs to verify
 behaviour.
@todo #56:30min Once #357 is finished, reuse the view (or better create a new
 generic one - if it doesn't exist) to enable sorting and filtering for every
 column. Also replace all other List views with this new generic one.
"""
from flask import Blueprint

from timeless.views import ListView
from timeless.schemetypes.models import SchemeType

bp = Blueprint("scheme_type", __name__, url_prefix="/schemetypes")


# class Create(CreateView):
#     """Create scheme type"""
#     template_name = "schemetypes/create_edit.html"
#     form_class  = SchemeTypeForm
#     model = SchemeType


# class Edit(UpdateView):
#     """Update scheme type"""
#     template_name = "schemetypes/create_edit.html"
#     form_class  = SchemeTypeForm
#     model = SchemeType


# class Delete(DeleteView):
#     """Delete scheme type
#     Deletes scheme type using id and redirects to list page
#     """
#     form_class  = SchemeTypeForm
#     model = SchemeType


class List(ListView):
    """List all scheme types"""
    template_name = "schemetypes/list.html"
    model = SchemeType


List.register(bp, "/")
# Create.register(bp, "/create")
# Edit.register(bp, "/edit/<int:id>")
# Delete.register(bp, "/delete")
