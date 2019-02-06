"""This file contains all functions needed to create
a new Flask app for timeless
@todo #69:30min Enhance the "DoubleQuotesOnly" rule from checkstyle.sh,
 to allow single-quoted strings as long as they are contained within
 another double-quoted String.
@todo #50:30min After #37 is completed add execution of one test with migrations
 flag inside rultor so we can validate that any new migrations are done
 correctly and are in sync with master.
"""

import os
from flask import Flask

from timeless.db import DB
from timeless.companies import views as companies_views
from timeless.auth import views as auth_views
from timeless.reservations import views as reservations_views
from timeless.restaurants.locations import views as locations_views
from timeless.restaurants.floors import views as floors_views


def create_app(config):
    """Creates a new Timeless webapp given a config class"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    initialize_extensions(app)
    register_endpoints(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def main():
        return "Hello, World!"
    return app


def initialize_extensions(app):
    """Initialize extensions for the app"""
    DB.init_app(app)
    import timeless.schemetypes.models
    import timeless.restaurants.models
    import timeless.reservations.models
    import timeless.employees.models


def register_api(app, view, endpoint, url, pk="id", pk_type="int"):
    """
    This method was taken from official docs, more info by link
    http://flask.pocoo.org/docs/1.0/views/#method-views-for-apis
    """
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, view_func=view_func, methods=["POST"])
    app.add_url_rule(
        url,
        defaults={pk: None},
        view_func=view_func,
        methods=["GET"]
    )
    app.add_url_rule(
        "%s<%s:%s>" % (url, pk_type, pk),
        view_func=view_func,
        methods=["GET", "PUT", "DELETE"]
    )


def register_endpoints(app):
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(reservations_views.bp)
    app.register_blueprint(locations_views.bp)
    register_api(
        app,
        companies_views.Resource,
        "companies.api",
        "/api/companies/",
        pk="company_id"
    )
    register_api(
        app,
        reservations_views.CommentView,
        "comments.api",
        "/api/comments/",
        pk="comment_id"
    )
    app.register_blueprint(floors_views.bp)
