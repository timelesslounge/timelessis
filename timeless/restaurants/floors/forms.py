from timeless import forms
from timeless.restaurants import models


class FloorForm(forms.ModelForm):
    """ Base form for creating / updating Floor """

    class Meta:
        """ Meta for Floor form """
        model = models.Floor
