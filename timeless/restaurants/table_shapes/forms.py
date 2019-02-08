from timeless import forms
from timeless.restaurants import models


class TableShapeForm(forms.ModelForm):
    class Meta:
        model = models.TableShape
