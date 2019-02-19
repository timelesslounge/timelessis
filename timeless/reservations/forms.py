from timeless import forms
from timeless.reservations import models


class SettingsForm(forms.BaseModelForm):
    """ Base form for creating / updating Settings """

    class Meta:
        """ Meta for Table form
        @todo #186:30min excluding greeting_by_time is temporary solution.
         forms.BaseModelForm can't handle JSON field.
         Need to research how to fix this case and fix it.
        """
        model = models.ReservationSettings
        exclude = ["greeting_by_time"]
