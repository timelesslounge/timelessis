from timeless import forms
from timeless.restaurants.models import Reservation


class ReservationForm(forms.ModelForm):
    """Base form for reservation"""

    class Meta:
        model = Reservation
