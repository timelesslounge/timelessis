"""Celery tasks for poster module"""
import os

from celery import shared_task

from timeless import DB
from timeless.customers.models import Customer
from timeless.poster.api import Authenticated, PosterAuthData, Poster
from timeless.restaurants.models import Table


def __poster_api():
    auth_data = PosterAuthData(
        application_id=os.environ.get("poster_application_id"),
        application_secret=os.environ.get("poster_application_secret"),
        redirect_uri=os.environ.get("poster_redirect_uri"),
        code=os.environ.get("poster_code"),
    )
    auth_token = Authenticated(auth_data=auth_data).auth()
    poster = Poster(auth_token=auth_token)
    return poster


__poster = __poster_api()


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
    for poster_table in __poster.tables():
        table = DB.session(Table).query.filter_by(
            name=poster_table["name"], floor_id=poster_table["floor_id"]
        ).first()
        merge_data(model=Table, poster_data=poster_table, timelessis_data=table)


@shared_task
def sync_customers():
    """
    Periodic task for fetching and saving tables from Customer
    """
    for poster_customer in __poster.customers():
        customer = DB.session(Customer).query.filter_by(
            first_name=poster_customer["first_name"], last_name=poster_customer["last_name"]
        ).first()
        merge_data(model=Customer, poster_data=poster_customer, timelessis_data=customer)


def merge_data(model, poster_data, timelessis_data):
    if timelessis_data:
        DB.session.add(model.merge_with_poster(timelessis_data, poster_data))
    else:
        DB.session.merge(model.create_by_poster(poster_data))
    DB.session.commit()
