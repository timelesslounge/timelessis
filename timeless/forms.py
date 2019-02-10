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

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

    @classmethod
    def get_session(cls):
        return DB.session

    def create(self, session):
        self.instance = self.Meta.model()
        self.populate_obj(self.instance)
        session.add(self.instance)

    def update(self):
        raise NotImplementedError

    def save(self, commit=True):
        session = self.get_session()

        if self.instance:
            self.update()
        else:
            self.create(session)

        if commit:
            session.commit()

        return self.instance
