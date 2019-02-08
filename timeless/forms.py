import flask_wtf
import wtforms_alchemy

from timeless.db import DB


BaseModelForm = wtforms_alchemy.model_form_factory(flask_wtf.FlaskForm)


class ModelForm(BaseModelForm):
    """It's made to support working WTF-Alchemy with Flask-WTF, look at
    https://wtforms-alchemy.readthedocs.io/en/latest/advanced.html for
    details."""

    @classmethod
    def get_session(self):
        return DB.session
