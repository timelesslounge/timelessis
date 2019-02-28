"""Forms for table shapes blueprint in order to support CRUD operations"""
from flask_wtf.file import FileRequired, FileAllowed, FileField

from timeless import forms
from timeless.restaurants import models
from timeless.uploads import IMAGES


class TableShapeForm(forms.ModelForm):
    """Base form for table shape"""

    picture = FileField(
        "Table Shape Image",
        validators=[FileRequired(), FileAllowed(IMAGES, "Images only!")])

    class Meta:
        model = models.TableShape
        exclude = ("picture",)

    def __init__(self, *args, **kwargs):
        self._file = kwargs.pop("files").get("picture")
        super(TableShapeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        Saves uploaded image
        :param commit: To commit flag
        :return: Saved instance
        @todo #205:30min Lets save only filename which is a static
         part of a url. Hostname, port and perhaps base path
         should be calculated dynamically for each table shape
         while being rendered to the template. See Configuration
         paragraph https://pythonhosted.org/Flask-Uploads/
        """
        filename = IMAGES.save(self._file)
        self.picture.data = IMAGES.url(filename)
        super(TableShapeForm, self).save(commit=commit)
