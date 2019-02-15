"""Forms for table shapes blueprint in order to support CRUD operations"""
from timeless import forms
from timeless.roles.models import Role


class RoleForm(forms.ModelForm):
    """Base form for role"""

    class Meta:
        model = Role
