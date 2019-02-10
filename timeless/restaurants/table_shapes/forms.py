"""Forms for table shapes blueprint in order to support CRUD operations"""
from timeless import forms
from timeless.restaurants import models


class TableShapeForm(forms.ModelForm):
    """Base form for table shape"""

    class Meta:
        model = models.TableShape
