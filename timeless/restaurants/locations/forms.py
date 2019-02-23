from timeless import forms
from timeless.restaurants import models


class LocationForm(forms.ModelForm):
    """ Base form for creating / updating Location """

    class Meta:
        """ Meta for Location form """
        model = models.Location
