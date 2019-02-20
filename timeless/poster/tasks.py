"""Celery tasks for poster module"""
import os

from celery import shared_task

from timeless import DB
from timeless.poster.api import Authenticated, PosterAuthData, Poster
from timeless.restaurants.models import Table


@shared_task
def sync_tables():
    """
    Periodic task for fetching and saving tables from Poster
    @todo #187:30min Set up scheduler for celery,
     docs - http://docs.celeryproject.org/en/
     latest/userguide/periodic-tasks.html#id5
     Also should make small refactoring: celery.py should situated in
     timelessis/celery.py not in timelessis/sync/celery.py
    """
    auth_data = PosterAuthData(
        application_id=os.environ.get("poster_application_id"),
        application_secret=os.environ.get("poster_application_secret"),
        redirect_uri=os.environ.get("poster_redirect_uri"),
        code=os.environ.get("poster_code"),
    )
    auth_token = Authenticated(auth_data=auth_data).auth()
    poster = Poster(auth_token=auth_token)
    for poster_table in poster.tables():
        table = DB.session(Table).query.filter_by(
            name=poster_table["name"], floor_id=poster_table["floor_id"]
        ).first()

        if table:
            new_table = Table.merge_with_poster(table, poster_table)
            DB.session.add(new_table)
        else:
            new_table = Table.create_by_poster(poster_table)
            DB.session.merge(new_table)

        DB.session.commit()
