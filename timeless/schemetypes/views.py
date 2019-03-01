"""SchemeType views module.
@todo #386:30min Continue implementing Edit and Delete views once
 generic views. Code templates are already provided
 below, so uncomment and modify - create templates and write ITs to verify
 behaviour.
@todo #56:30min Once #357 is finished, reuse the view (or better create a new
 generic one - if it doesn't exist) to enable sorting and filtering for every
 column. Also replace all other List views with this new generic one.
@todo #97:30min Continue implementing SchemeConditionCreate,
 SchemeConditionEdit, SchemeConditionDelete views once generic views from #173
 are implemented. Code templates are already provided below, so uncomment and
 modify - create templates and write ITs to verify behaviour.
"""
from http import HTTPStatus
from flask import Blueprint, abort, url_for

from timeless.views import CreateView, ListView
from timeless.schemetypes.forms import SchemeConditionForm
from timeless.schemetypes.models import SchemeType, SchemeCondition


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


class SchemeConditionList(ListView):
    """List all scheme conditions for scheme type"""
    template_name = "schemetypes/schemeconditions/list.html"
    model = SchemeCondition

    def get(self, scheme_type_id):
        if not scheme_type_id:
            return abort(HTTPStatus.BAD_REQUEST)
        self.scheme_type_id = scheme_type_id
        return super().get(self, scheme_type_id)

    def get_object_list(self):
        return self.model.query.filter(
            SchemeCondition.scheme_type_id == self.scheme_type_id)


class SchemeConditionCreate(CreateView):
    """Create scheme condition"""
    template_name = "schemetypes/schemeconditions/create_edit.html"
    form_class = SchemeConditionForm

    def get_success_url_redirect(self):
        return url_for(
            "scheme_type.scheme_condition_list",
            scheme_type_id=self.kwargs["scheme_type_id"])


# class SchemeConditionEdit(UpdateView):
#     """Update scheme condition"""
#     template_name = "schemetypes/schemeconditions/create_edit.html"
#     form_class  = SchemeConditionForm
#     model = SchemeCondition


# class SchemeConditionDelete(DeleteView):
#     """Delete scheme condition
#     Deletes scheme condition using id and redirects to list page
#     """
#     form_class  = SchemeConditionForm
#     model = SchemeCondition

SchemeConditionList.register(
    bp, "/schemeconditions/<int:scheme_type_id>")
SchemeConditionCreate.register(
    bp, "/schemeconditions/<int:scheme_type_id>/create")
# SchemeConditionEdit.register(bp, "/schemeconditions/edit/<int:id>")
# SchemeConditionDelete.register(bp, "/schemeconditions/delete")
