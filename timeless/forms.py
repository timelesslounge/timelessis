"""This file contains base form class which helps integrate WTF-Alchemy
and Flask-WTF, since it doesn't work properly ot of the box."""

import flask_wtf
import wtforms_alchemy

from timeless.db import DB


BaseModelForm = wtforms_alchemy.model_form_factory(flask_wtf.FlaskForm)


class ModelForm(BaseModelForm):
    """It's made to support working WTF-Alchemy with Flask-WTF, look at
    https://wtforms-alchemy.readthedocs.io/en/latest/advanced.html for
    details."""

    @classmethod
    def get_session(cls):
        return DB.session
