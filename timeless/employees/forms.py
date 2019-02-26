"""Forms for employees blueprint"""

from timeless import forms
from timeless.employees.models import Employee


class EmployeeForm(forms.ModelForm):
    """Base form for employee"""

    class Meta:
        model = Employee
