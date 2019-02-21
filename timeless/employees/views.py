"""Employees views module.
@todo #57:30min Continue implementing Create, Edit and Delete views once
 generic views from #173 are implemented. Templates are already provided below,
 so uncomment and modify - create templates and write ITs to verify behaviour
@todo #57:30min Continue implementing List to enable sorting and filtering
 for every column. For this, probably there will be a need to create a new
 generic view that all other List views will extend. This generic view should
 use GenericFilter implemented in #317.
"""
from flask import Blueprint
from timeless.views import ListView
from timeless.employees.models import Employee

bp = Blueprint("employee", __name__, url_prefix="/employees")


# class Create(CreateView):
#     """Create employee"""
#     template_name = "employees/create_edit.html"
#     form_class  = EmployeeForm
#     model = Employee


# class Edit(UpdateView):
#     """Update employee"""
#     template_name = "employees/create_edit.html"
#     form_class  = EmployeeForm
#     model = Employee


# class Delete(DeleteView):
#     """Delete employee
#     Deletes employee using id and redirects to list page
#     """
#     form_class  = EmployeeForm
#     model = Employee


class List(ListView):
    """List all employees"""
    template_name = "employees/list.html"
    model = Employee


List.register(bp, "/")
# Create.register(bp, "/create")
# Edit.register(bp, "/edit/<int:id>")
# Delete.register(bp, "/delete")
