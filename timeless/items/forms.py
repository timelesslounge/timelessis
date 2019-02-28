from timeless import forms
from timeless.items import models


class ItemForm(forms.ModelForm):
    """ Base form for creating / updating Items """

    class Meta:
        """ Meta for Item form """
        model = models.Item
