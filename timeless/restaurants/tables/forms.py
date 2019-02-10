from timeless import forms
from timeless.restaurants import models


class TableForm(forms.BaseModelForm):
    """ Base form for creating / updating Table """

    class Meta:
        """ Meta for Table form """
        model = models.Table
