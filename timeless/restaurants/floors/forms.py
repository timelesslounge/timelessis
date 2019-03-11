from timeless import forms
from timeless.restaurants import models
from wtforms import Form, TextField, HiddenField


class FloorForm(forms.ModelForm):
    """ Base form for creating / updating Floor """
    location_id = HiddenField("Location id")

    class Meta:
        """ Meta for Floor form """
        model = models.Floor
