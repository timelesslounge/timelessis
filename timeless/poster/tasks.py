"""Celery tasks for poster module"""
import os

from flask import current_app

from celery import shared_task

from timeless import DB
from timeless.customers.models import Customer
from timeless.poster.api import Authenticated, PosterAuthData, Poster
from timeless.restaurants.models import Table, Location


def __poster_api():
    auth_data = PosterAuthData(
        application_id=current_app.config.get("poster_application_id"),
        application_secret=current_app.config.get("poster_application_secret"),
        redirect_uri=current_app.config.get("poster_redirect_uri"),
        code=current_app.config.get("poster_code"),
    )
    auth_token = Authenticated(auth_data=auth_data).auth()
    poster = Poster(auth_token=auth_token)
    return poster


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
    for poster_table in __poster_api().tables():
        table = DB.session(Table).query.filter_by(
            name=poster_table["name"], floor_id=poster_table["floor_id"]
        ).first()
        merge_data(
            model=Table, poster_data=poster_table, timelessis_data=table
        )


@shared_task
def sync_customers():
    """
    Periodic task for fetching and saving tables from Poster
    Docs - https://dev.joinposter.com/docs/api#clients-getclients
    """
    for poster_customer in __poster_api().customers().get("response", []):
        customer = Customer.query.filter_by(
            poster_id=poster_customer["client_id"]
        ).first()
        merge_data(
            model=Customer,
            poster_data=poster_customer,
            timelessis_data=customer
        )


@shared_task
def sync_locations():
    """
    Periodic task for fetching and saving location from Poster
    """
    for poster_location in __poster_api().locations():
        location = DB.session(Location).query.filter_by(
            name=poster_location["name"],
            code=poster_location["code"]
        ).first()
        merge_data(
            model=Location,
            poster_data=poster_location,
            timelessis_data=location
        )


def merge_data(model, poster_data, timelessis_data):
    if timelessis_data:
        DB.session.add(model.merge_with_poster(timelessis_data, poster_data))
    else:
        DB.session.merge(model.create_by_poster(poster_data))
    DB.session.commit()
