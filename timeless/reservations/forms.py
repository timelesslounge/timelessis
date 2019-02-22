"""Forms for reservation blueprint"""

from timeless import forms
from timeless.reservations.models import ReservationSettings
from timeless.restaurants.models import Reservation


class ReservationForm(forms.ModelForm):
    """Base form for reservation"""

    class Meta:
        model = Reservation


class SettingsForm(forms.BaseModelForm):
    """ Base form for creating / updating Settings """

    class Meta:
        """ Meta for Table form
        @todo #186:30min excluding greeting_by_time is temporary solution.
         forms.BaseModelForm can't handle JSON field.
         Need to research how to fix this case and fix it.
        """
        model = ReservationSettings
        exclude = ["greeting_by_time"]
