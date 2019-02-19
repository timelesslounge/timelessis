import os

from celery import shared_task

from timeless.poster.api import Authenticated, PosterAuthData, Poster
from timeless.restaurants import models


@shared_task
def sync_tables():
    """
    Periodic task for fetching and saving tables from Poster
    @todo #187:30min Implement integration tests for this periodic task.
     Create fixture and mock response from poster, and check how it will be
     saved in DB. API docs - https://dev.joinposter.com/en/docs/api
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
        table = models.Table.query.filter_by(
            name=poster_table["name"], floor_id=poster_table["floor_id"]
        ).first()

        if table:
            for key, value in table.items():
                setattr(table, key, value)
        else:
            table = models.Table(**poster_table)

        table.save()
