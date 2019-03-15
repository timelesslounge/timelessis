"""This file contains all functions needed to create
a new Flask app for timeless
@todo #204:30min Continue implementing CSRF token protection for all create and
 edit templates. Implementation detail you can find on the following page:
 https://flask-wtf.readthedocs.io/en/stable/csrf.html
"""
# Since if import models / views inside methods, pylint complains
# about cyclic imports.
# pylint: disable=R0401
# pylint: disable=W0612
import os
from flask import Flask, url_for, render_template
from timeless.cache import CACHE
from timeless.mail import MAIL
from timeless.db import DB
from timeless.celery import make_celery
from timeless.csrf import CSRF
from timeless import uploads


def create_app(config):
    """Creates a new Timeless webapp given a config class"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    CACHE.init_app(
        app,
        config=app.config.get("CACHE_SETTINGS")
    )
    MAIL.init_app(app)
    CSRF.init_app(app)
    initialize_extensions(app)
    register_endpoints(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    uploads.IMAGES = uploads.images(app)

    @app.route("/")
    def main():
        return render_template("auth/login.html")
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
    # initialize celery
    app.celery = make_celery(app)


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
    """ Initalize application endpoints """
    from timeless.companies import views as companies_views
    from timeless.auth import views as auth_views
    from timeless.reservations import views as reservations_views
    from timeless.restaurants.locations import views as locations_views
    from timeless.restaurants.tables import views as tables_views
    from timeless.restaurants.floors import views as floors_views
    from timeless.roles import views as roles_views
    from timeless.restaurants.table_shapes import views as table_shapes_views
    from timeless.items import views as items_views
    from timeless.schemetypes import views as schemetypes_views
    from timeless.employees import views as employees_views

    app.register_blueprint(auth_views.BP)
    app.register_blueprint(tables_views.BP)
    app.register_blueprint(locations_views.BP)
    app.register_blueprint(roles_views.BP)
    app.register_blueprint(items_views.BP)
    app.register_blueprint(floors_views.BP)
    app.register_blueprint(table_shapes_views.BP)
    app.register_blueprint(reservations_views.BP)
    app.register_blueprint(schemetypes_views.BP)
    app.register_blueprint(employees_views.BP)
    register_api(
        app,
        companies_views.Resource,
        "companies.api",
        "/api/companies/",
        pk="company_id"
    )
    register_api(
        app,
        reservations_views.ReservationsListView,
        "reservations.api",
        "/api/reservations/",
        pk="company_id"
    )
    register_api(
        app,
        reservations_views.CommentView,
        "comments.api",
        "/api/comments/",
        pk="comment_id"
    )
