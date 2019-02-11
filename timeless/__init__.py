"""This file contains all functions needed to create
a new Flask app for timeless
"""
# Since if import models / views inside methods, pylint complains
# about cyclic imports.
# pylint: disable=R0401
# pylint: disable=W0612
import os
from flask import Flask
from flask_caching import Cache
from timeless.db import DB


def create_app(config):
    """Creates a new Timeless webapp given a config class"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    """
    @todo #21:30min Install redis in the docker.
     Also, Add Redis installation to the readme file for complete installation.
     Redis installation script can be taken from the scripts/install folder.
    """
    cache = Cache(app, config={"CACHE_TYPE": "redis"})
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
    import timeless.customers.models
    import timeless.schemetypes.models
    import timeless.restaurants.models
    import timeless.reservations.models
    import timeless.roles.models
    import timeless.items.models
    import timeless.employees.models
    import timeless.companies.models


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
    from timeless.companies import views as companies_views
    from timeless.auth import views as auth_views
    from timeless.reservations import views as reservations_views
    from timeless.restaurants.locations import views as locations_views
    from timeless.restaurants.tables import views as tables_views
    from timeless.restaurants.floors import views as floors_views
    from timeless.roles import views as roles_views
    from timeless.restaurants.table_shapes import views as table_shapes_views

    app.register_blueprint(auth_views.bp)
    app.register_blueprint(tables_views.bp)
    app.register_blueprint(locations_views.bp)
    app.register_blueprint(roles_views.bp)
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
    register_api(
        app,
        reservations_views.SettingsView,
        "settings.api",
        "/reservations/settings/"
    )
    app.register_blueprint(floors_views.bp)
    app.register_blueprint(table_shapes_views.bp)
