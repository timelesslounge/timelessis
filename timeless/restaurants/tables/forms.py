from timeless.forms import ModelForm
from timeless.restaurants import models


class TableForm(ModelForm):
    """ Base form for creating / updating Table """

    class Meta:
        """ Meta for Table form """
        model = models.Table
