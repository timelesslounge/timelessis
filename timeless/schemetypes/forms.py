"""Forms for schema type blueprint in order to support CRUD operations"""
from timeless import forms
from timeless.schemetypes.models import SchemeCondition


class SchemeConditionForm(forms.ModelForm):
    """Base form for scheme types"""

    class Meta:
        model = SchemeCondition
