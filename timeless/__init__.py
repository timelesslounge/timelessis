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
from flask_sqlalchemy import SQLAlchemy

from timeless.companies import views as companies_views
from timeless.auth import views as auth_views
from timeless.reservations import views as reservations_views


DB = SQLAlchemy()


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
    import timeless.companies.models
    import timeless.restaurants.models
    import timeless.reservations.models
    import timeless.employees.models


def register_endpoints(app):
    app.register_blueprint(companies_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(reservations_views.bp)
