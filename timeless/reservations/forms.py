"""Module where all forms working with reservation are defined"""
from timeless import forms
from timeless.reservations import models


class Reservation(forms.ModelForm):
    """Base form for Reservation"""

    class Meta:
        model = models.Reservation
