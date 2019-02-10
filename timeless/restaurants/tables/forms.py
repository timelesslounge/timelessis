from timeless import forms
from timeless.restaurants import models


class TableForm(forms.BaseModelForm):
    class Meta:
        model = models.Table
